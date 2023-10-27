print("数値を入力してください＝＞", end=str())
num = 0
while True:
    num = input()
    if num.isdigit() :
        num = int(num)
        break
    print("整数値を入力してください＝＞", end=str())
if num % 2 == 0 :
    print("偶数です")
else :
    print("奇数です")