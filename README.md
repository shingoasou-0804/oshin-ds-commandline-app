# oshin-ds-commandline-app

- これはPythonのコマンドラインアプリです。

## 必要環境

- docker version 20.10.x 以上

## セットアップ方法

```console
$ docker compose build --no-cache
$ docker compose up
```

## 実行方法
- `data` フォルダに `yomilog.csv` を配置する
- `dna -> tests` フォルダに `DNAヌクレオチド配列のテキストファイル` を配置する

```console
# ライブラリのインストール
$ docker compose run command-app bash
$ pip install library_name
$ pip freeze > requirements.txt

# レコメンドアルゴリズム実行
$ docker compose exec command-app python recommend_books.py susumuis 5000 -i data -o data -l DEBUG

# DNAヌクレオチドカウント実行
$ docker compose exec command-app python dna/dna.py dna/tests/inputs/input_dna_2.txt

# DNAヌクレオチドカウント テスト実行
$ docker compose exec command-app pytest dna/tests/dna_test.py

# fast-python
$ docker compose exec command-app python fast-python/load.py 01044099999,02293099999 2021-2021
$ docker compose exec command-app python -m cProfile -s cumulative fast-python/load.py 01044099999,02293099999 2021-2021 > profile_cache.txt

# snakevizのインストールと実行方法(Macの場合)
$ brew install snakeviz
$ snakeviz distance_cache.prof
```

- `data` フォルダに `result-susumuis-5000.csv` などの結果が出力される
