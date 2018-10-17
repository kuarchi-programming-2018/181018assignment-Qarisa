# coding: utf-8
# 学生メソッドを作る

class Gakusei:
    def __init__(self, kokugo, sansu):
        self.kokugo = kokugo
        self.sansu  = sansu
        
    def sum(self):
        return self.kokugo+self.sansu

    # この下に、合計得点を戻り値として返すsumメソッドを記述する

yamada = Gakusei(70, 43)
sum=yamada.sum()
print("合計は" + str(sum) + "点です")
