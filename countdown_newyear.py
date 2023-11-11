"""
今日はOO年OO月OO日
OO年まで残りOO日
あとOO％
"""
import datetime

d_today = datetime.date.today()
this_year= int(d_today.strftime("%Y")) + 1
# 年初めの日時を取得
start_of_year = datetime.date(d_today.year, 1, 1)
# 年末の日時を取得
last_of_year = datetime.date(d_today.year, 12, 31)
# 今年の経過日数を計算
days_passed = (last_of_year - start_of_year).days

new_year = datetime.date(year=this_year, month=1, day=1)
d = abs(new_year - d_today).days
print(f"今日は{d_today}です")
print(f"{new_year}まで残り{d}日 ({(d / days_passed) * 100:.1f}%)")
