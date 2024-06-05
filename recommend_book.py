import logging
import sys
from argparse import ArgumentParser
from pathlib import Path

import pandas as pd
import pandera as pa
from mip import Model, maximize, xsum

logger = logging.getLogger(__name__)


def validate_input_df(df: pd.DataFrame) -> pd.DataFrame:
    """入力データの形式をチェックする"""

    schema = pa.DataFrameSchema({
        "name": pa.Column(str),
        "title": pa.Column(str),
        "price": pa.Column(int),
    })

    return schema.validate(df)


def optimize_book_to_buy(
    df: pd.DataFrame,
    name: str,
    money: int
) -> pd.DataFrame:
    """数理最適化後、おすすめする書籍のリストを求める"""
    # 既読の書籍
    name_titles_set = df.loc[df["name"] == name, "title"].unique()
    # 未読の書籍
    df_filtered = df[~df["title"].isin(name_titles_set)]

    # 書籍ごとのタイトル、価格、読んだ人数を集計
    df_books = (
        df_filtered.groupby("title")
        .agg({"name": "nunique", "price": "first"})
        .reset_index()
        .rename(columns={"name": "n_readers"})
    )

    # モデルの作成
    m = Model()
    # 変数: 書籍をおすすめする=1、しない=0
    df_books["Var_x"] = m.add_var_tensor((len(df_books),), "x", var_type="B")
    # 目的関数: 同僚の多くが読んでいる書籍をなるべく多くおすすめする
    m.objective = maximize(xsum(df_books["n_readers"] * df_books["Var_x"]))
    # 制約条件
    m += xsum(df_books["price"] * df_books["Var_x"]) <= money

    # 最適化実行
    m.optimize()

    # 結果
    df_books["Var_x"] = df_books["Var_x"].astype(float)
    # 誤差による不具合を防ぐため0.5を境界に比較
    return df_books.loc[df_books["Var_x"] > 0.5, ["title", "n_readers", "price"]]
