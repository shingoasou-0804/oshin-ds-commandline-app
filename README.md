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
# レコメンドアルゴリズム実行
$ docker compose exec command-app python recommend_books.py susumuis 5000 -i data -o data -l DEBUG

# DNAヌクレオチドカウント実行
$ docker compose exec command-app python dna/dna.py dna/tests/inputs/input_dna_2.txt
```

- `data` フォルダに `result-susumuis-5000.csv` などの結果が出力される
