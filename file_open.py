import os

path = "./test/user.txt"
# ファイルを作成（ディレクトリは作れない）
# f = open(path, 'w')
# f.write('')
# f.close


# ファイル削除(ディレクトリは消せない)
os.remove(path)