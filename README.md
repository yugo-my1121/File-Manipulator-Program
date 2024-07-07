# 概要
ファイルの内容を反転・コピー・複製・文字列の置き換えをした新しいファイルを作成するプログラムです。

# 操作方法

### reverse
```
python3 file_manipulator.py reverse inputpath outputpath
```
inputpath にあるファイルを受け取り、outputpath に inputpath の内容を逆にした新しいファイルを作成します。
<br>

### copy
```
python3 file_manipulator.py copy inputpath outputpath

```
inputpath にあるファイルのコピーを作成し、outputpath として保存します。
<br>

### duplicate-contents
```
python3 file_manipulator.py duplicate-contents inputpath n
```
inputpath にあるファイルの内容を読み込み、その内容を複製し、複製された内容を inputpath に n 回複製します。
<br>

### replace-string
```
python3 file_manipulator.py replace-string inputpath needle newstring
```

inputpath にあるファイルの内容から文字列 'needle' を検索し、'needle' の全てを 'newstring' に置き換えます。
