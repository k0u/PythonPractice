"""
ファイルを整理整頓する
作業ディレクトリに散財するファイルを分類
拡張子で判別
.py
.txt
.log
上記以外の拡張子
サブディレクトリに分けて移動する
scripts textfiles logs others
"""
import glob
import re

for name in glob.glob('./'):
    if re.search(r"^.*\.py", name) :
        print("match")