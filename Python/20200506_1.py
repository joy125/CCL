# -*- coding: utf-8 -*-
"""
Created on Wed May  6 13:40:02 2020

@author: ASUS
"""

#------------------------------------------
'''

Python程式檔格式:*.py
jupyter程式檔格式:*.ipynb

'''
a=1
b=100
print("Sum =",a+b)

#----------------------------------------------
'''
num1=變數
int=資料型態(整數)
input=輸入
if=條件式
while=迴圈
print=輸出

'''
num1=int(input('請輸入第一個數值：'))
num2=int(input('請輸入第二個數值：'))
if num1<num2:
    tmp_num=num1
    num1=num2
    num2=tmp_num
while num2 !=0:
    tmp_num=num1 % num2
    num1 = num2    
    num2=tmp_num
print('最大公因數=',num1)

