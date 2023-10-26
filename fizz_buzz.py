'''
1から100までの数をプリントするプログラムを書く
3の倍数のときは数の代わりに「Fizz」、5の倍数のときは「Buzz」、3と5の両方の倍数のときには「FizzBuzz」とプリントする
'''
for number in range(1, 101):
    if number % 15 == 0 :
        print("FizzBuzz", end=str())
    elif number % 5 == 0 :
        print("Buzz", end=str())
    elif number % 3 == 0 :
        print("Fizz", end=str())
    else :
        print(number, end=str())
    print(" ", end=str())