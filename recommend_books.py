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
    # 変数: 書籍をおすすめする=1, しない=0
    df_books["Var_x"] = m.add_var_tensor((len(df_books),), "x", var_type="B")
    # 目的関数: 同僚の多くが読んでいる書籍をなるべく多くおすすめする
    m.objective = maximize(xsum(df_books["n_readers"] * df_books["Var_x"]))
    # 制約条件: 金額が予算以内
    m += xsum(df_books["price"] * df_books["Var_x"]) <= money

    # 最適化実行
    m.optimize()

    # 結果の取得
    df_books["Val_x"] = df_books["Var_x"].astype(float)
    # 誤差による不具合を防ぐため0.5を境界に比較
    return df_books.loc[df_books["Val_x"] > 0.5, ["title", "n_readers", "price"]]


def parse_args():
    """コマンドラインを読み込む"""

    parser = ArgumentParser()
    parser.add_argument(
        "name",
        help="対象の名前",
        type=str,
    )
    parser.add_argument(
        "money",
        help="予算",
        type=int,
    )
    parser.add_argument(
        "-i",
        "--input_dir",
        help="入力ディレクトリ",
        type=Path,
        required=True,
    )
    parser.add_argument(
        "-o",
        "--output_dir",
        help="出力ディレクトリ",
        type=Path,
        required=True,
    )
    parser.add_argument(
        "-l",
        "--log_level",
        help="ログレベル",
        default=logging.INFO
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    logging.basicConfig(
        level=args.log_level,
        format="%(asctime)s %(levelname)7s %(message)s",
        force=True,
    )

    input_file = args.input_dir / "yomilog.csv"

    logger.info("データを入力します。")
    logger.debug("入力ファイル: %s", input_file)
    input_df = pd.read_csv(input_file)

    logger.info("入力ファイルのデータ形式をチェックします。")
    try:
        input_df = validate_input_df(input_df)
    except pa.errors.SchemaError as e:
        logger.error("入力ファイルの形式に問題がありました: %s", e)
        sys.exit(1)

    logger.info("おすすめ書籍を求める処理を開始します。")
    output_df = optimize_book_to_buy(input_df, args.name, 5000)
    logger.debug("結果:\n%s", output_df)

    output_file = args.input_dir / f"result-{args.name}-{args.money}.csv"

    logger.info("データを出力します。")
    logger.debug(f"出力ファイル: {output_file}")
    output_df.to_csv(output_file)
    logger.info("データを出力しました。")
