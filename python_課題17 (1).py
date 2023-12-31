# -*- coding: utf-8 -*-
"""python 課題17

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OEKBkNKR_gucEgf0CJJJPz0MeyksJUxZ
"""

class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age

#check_adultメソッドの作成
  def check_adult(self):
    if self.age > 20:
      print("大人です。")
    else:
      print("まだ大人ではありません。")

#Humanクラスのインスタンスを複数作成
sato = Human("佐藤", 25)
tanaka = Human("田中", 19)
uchida = Human("内田", 29)
suzuki = Human("鈴木", 18)

#リストに追加する
humans = [
    sato,
    tanaka,
    uchida,
    suzuki
]

#check_adultメソッドを呼び出す。
for human in humans:
  human.check_adult()