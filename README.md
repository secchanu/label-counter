# label-counter

## 開発

### 依存関係のインストール

Poetry がインストールされている場合

```sh
poetry install
```

そうでない場合

```sh
pip install .
```

### 実行

```sh
python label-counter
```

### ビルド

```sh
nuitka --follow-imports --standalone --onefile --remove-output --output-filename=LabelCounter.exe label-counter/__main__.py
```

## 使用

`label`フォルダの中に PascalVOC のアノテーションデータ(xml ファイル)を入れた状態で実行
