"""
ファイルを整理整頓する
作業ディレクトリに散財するファイルを分類
拡張子で判別
.txt
.log
サブディレクトリに分けて移動する
textfiles logs
"""
import glob
import os
import shutil

def move_files(target_file, new_path):
    l = glob.glob(target_file)
    if l:
        # ディレクトリを作成
        os.makedirs(new_path, exist_ok=True)
        for file in l:

            print(file)
            # ファイル移動
            try:
                shutil.move(file, new_path)
            except Exception:
                print(f"移動先に同名のファイルが存在します。＝＞{file}")
    else:
        print(f"該当ファイルなし=>{target_file}")

def sort_textfiles():
    move_files("./*.txt", "./textfiles")

def sort_logfiles():
    move_files("./*.log", "./logs")


sort_textfiles()
sort_logfiles()