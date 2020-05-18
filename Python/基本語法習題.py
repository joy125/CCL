# -*- coding: utf-8 -*-
"""
Created on Mon May 11 16:36:46 2020

@author: ASUS
"""
#01
'''
請撰寫一程式，請使用者輸入華氏溫度，然後輸出其對應的攝氏溫度。
提示：攝氏溫度 = (華氏溫度-32)*5/9

輸入與輸出範例：
    輸入：212
    輸出：
        Fahrenheit 212.00 ---> Celsius 100.0
'''
def change(temp_f):
    temp_c=(temp_f-32)*5/9
    return temp_c
temp_f=eval(input("請輸入華氏溫度"))
temp_c=change(temp_f)
print("Fahrenheit %.2f ---> Celsius %.1f" % \
(temp_f,temp_c))

#02
'''
請撰寫一程式，以下一公式計算五邊形的面積：
 area = 5s^2/(4tan⁡(𝜋/5))，其中 s =2rsin(𝜋/5)，
 r 為五邊形的中心點到頂點的距離。
請使用者輸入 r，然後計算五邊形的面積(輸出到小數點後 2 位)。

輸入與輸出範例：
    輸入：5.5
    輸出：
        Area is 71.92
'''
r=eval(input("請輸入五邊形的中心點到頂點的距離"))
import math
s =2*r*math.sin(math.pi/5)
area = 5*s**2/(4*math.tan⁡(math.pi/5))
print("Area is ",area)
#03
'''
給定飛機的加速度 a，
以及起飛的速度 v，
在不考慮外力耗損下(如輪胎磨擦力、空氣阻力等)，
則要讓飛機起飛的最短跑道長度為 length = v^2 / 2a 。
試寫一程式，提示使用者輸入以公尺 / 秒為單位的速度 v，
以及以公尺 / 秒平方為單位的加速度 a，
然後輸出最短的跑道長度(輸出到小數點後 2 位)。

輸入與輸出範例：
    輸入：70  , 4.3
    輸出：
        Minimum runway length is 569.77 meters
'''
v,a=eval(input("請輸入速度與加速度(v,a):"))
length=v**2/(2*a)
print("Minimum runway length is %.2f meters"\
% length)

#04
'''
請撰寫一程式，計算從起始溫度到最後溫度時熱水所需要的\
能量。
在程式中提示使用者輸入熱水量(公斤)、起始溫度與最後溫度。
計算能量的公式如下：
Q = M * (finalT – initial) * 4184
其中 M 式熱水的公斤數，
finalT 是最後溫度，
initial 是起始溫度，
Q 是以焦耳(joules)來衡量的能量(輸出到小數點後 2 位)

輸入與輸出範例：
    輸入：10  , 12 , 100
    輸出：
        Q = 3681920.00
        
    (表示輸入 10 公斤的熱水，
    溫度從 12 度 到 100 度，
    所需的能量是 3681920.00 焦耳)
'''

m,initial,finalT=eval(input("請輸入熱水量(公斤)\
,起始溫度,最後溫度:"))
Q=m * (finalT-initial) * 4184
print(" %d 公斤的熱水，溫度從 %d 度 到 %d 度，\
所需的能量是 %.2f 焦耳" % (m,initial,finalT,Q))


#05
'''
請撰寫一程式，計算圓柱體的底面積與體積(輸出到小數點後 \
    2 位)。
在程式中提示使用者輸入圓柱的半徑和高。
 area = 𝜋r^2
 volume = area * height
其中 area 是底面積，
volume 是體積，
r 是圓柱體半徑，height 是圓柱體的高度。

輸入與輸出範例：
    輸入：6.5 , 10
    輸出：
        area : 132.73 , volume : 1327.32

'''
import math
r,h=eval(input("請輸入圓柱的半徑和高:"))
area = math.pi*r**2
volume = area * h
print("area : %.2f , volume : %.2f" % (area,volume))