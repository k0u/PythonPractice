"""
日付時刻と文字列
日付時刻から文字列への変換
日時でーたから指定の情報を文字列として表現する
指定の情報だけを表示

文字列から日付変換
日付時刻を表す文字列から日時データを作成する
日時データとして扱いやすい形で操作できる

相互変換
相互に相互変換な方法を覚えておく
"""
import datetime

date_string = "2023-11-11 12:30:00"
date_object = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(f"{date_object} type:{type(date_object)}")


# 現在時刻を取得
current_time = datetime.datetime.now()

current_time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")
print(f"{current_time_string} type:{type(current_time_string)}")
