"""
サイコロプログラム
"""
import random

class Dice() :
    def __init__(self, side) :
        self.side = side
        print(f"{side}面ダイスをつくりました。")

    
    def dice_roll(self):
        result = random.randint(1, self.side)
        print(f"{result}がでました。")
        
