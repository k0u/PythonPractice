import dice
import sys


try:
    six_side_dice = dice.Dice(int(sys.argv[1]))
except IndexError :
    print("python dice_user.py に続けて作成するサイコロの面数を数値で入力してください。")
except ValueError:
    print("数値で入力してください。")
else:

    while True:
        try:
            menu = input("サイコロ振りますか？ Yes:1 No:2 =>")
        except Exception as exc:
            print(type(exc))
            print("1か2を入力してください")
        else:
            if menu == "1":
                six_side_dice.dice_roll()
            elif menu == "2":
                print("See you...")
                break
            else :
                print(f"1か2を入力してください。入力値={menu}")