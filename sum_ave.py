'''
数値のリストを入力を受付け、その数の合計と平均を計算し表示する
'''
while True:
    try :
        input_str = input("数値をスペース区切りで入力してください＝＞").split()
        num_list = list(map(int, input_str))
        break
    except ValueError:
        print("エラー：有効な数値をスペースで区切って入力してください")

num_list_length = len(num_list)

sum = 0
ave = 0.0
for i in range(num_list_length):
    sum += num_list[i]

print("合計: %d 平均: %.2f" %(sum, sum/num_list_length))