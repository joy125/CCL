# -*- coding: utf-8 -*-
"""
Created on Fri May  8 13:11:37 2020

@author: ASUS
"""

#------------------20200508-----------------------
'''
20200507
函式:function
內建函式:將特定功能與以包裝,並以參數帶入資料運算.執行
        Python已定義完成,直接依功能使用
        函數格式:函數名稱(參數...)
                參數:帶入函式執行的資料
input():供使用者輸入資料之用
    格式:變數=input([提示字串])
    輸入時按下Enter及表示輸入完畢,
        將輸入資料存到變數中
    score=input("請輸入國文成績")
    print(score)
eval():將字串轉為數值
    格式:eval(資料)
    ex:                        
        score=eval(input(\
            "請輸入國文成績"))
        sum=score+20
        print("國文成績=",score,sum)
print():輸出(格式化)
    格式:
        print(資料1,資料2,....,\
              sep=分隔字元預設為空白,
              end=結束字元預設為\n)
            \n=換行
            \t=1個tab
            print()=print("\n")
                   ex:print(1,"Python","\n3"\
                    ,sep="+")
print():輸出(格式化)
    格式:
        print(格式參數1 格式參數2...
              .. % (資料1,資料2,....))
        格式參數:
            %s:字串
                %5s:輸出5個字元
                    小於5個字元,於左方填入空白
                    大於5個字元,則全數輸出
            %d:整數
                %5d:輸出5個整數
                    小於5個整數,於左方填入空白
                    大於5個整數,則全數輸出
            %f:浮點數
                %8.2f:輸出8位數字(含小數點),小數2位
                     若整數位小於5位(8-3(小數&小數點))
                         ,則在數字左方填入空白
                     若小數小於2位,則在右方填入0
                    大於,則全數輸出
            +:於格式數值前方加入+
              若數值為正,則在資料左方加上"+"
            -:輸出格式資料空間有多餘時,則資料靠左對齊
                        
                    
'''
score=eval(input("請輸入國文成績"))
sum=score+20
print("國文成績=",score,sum)
#---------------------------
print(1,2,3)
print(1,"Python","\n",3)
print(1,"Python","\n3",sep="+")

#------------
a=100
print("a=/%-6d/"%a)
b=12.3
print("b=/%-7.2f/"%b)
c="deep"
print("c=/%-6s/"%c)
d=50
print("d=/%+6d/"%d)
e=62213.3333
print("e=/%+6.2f/"%e)
#--------------
'''
a=eval(input("請輸入國文成績"))
b=eval(input("請輸入英文成績"))
c=eval(input("請輸入數學成績"))
sum=a+b+c
aa=sum/3
print("總成績:%-3d ,平均成績:%6.2f" % (sum,aa))
'''
chi=input("請輸入國文成績:")
eng=input("請輸入英文成績:")
math=input("請輸入數學成績:")
sum=int(chi)+int(eng)+int(math)
avg=sum/3
print("總成績:%d,平均成績:%5.2f" % (sum,avg))
'''
流程控制:
  以特定結構控制程式的執行方式
 條件式:
     必須以縮排進行程式結構化
     **條件式下的敘述式一定要往右縮排
  (1)if 
  if 條件式:(結果必須為布林值(Ture,False))
      敘述式(若條件成立,則執行敘述式)
  (2)if else
  if 條件式:
      敘述式1
  else:
      敘述式2
      若條件成立,則執行敘述1,否則執行敘述2
  (3)if elif
  if 條件1:
      敘述式1
  elif 條件2:
      敘述式2
      ....
  elif 條件n:
      敘述式n
  else:
      敘述式n+1
    逐一判斷條件,若成立則執行敘述式後離開if,
    當所有條件都不成立則執行n+1
  (4)巢狀if:可套用到任何的if條件
  if 條件1:
      if 條件2:
          if 條件3:
              
 迴圈:重複執行的敘述
  (1)for:
      for 變數 initerator :
          敘述式
              initerator>>使用range()函式
              range(起始值,終止值,間隔值)
                  起始值,間隔值可不指定
                  起始值預設為0,間隔值預設為1
        ex:印出0~10的整數
        for i in range(11):
            print(i)
  (2)while:
      while 條件式:
          敘述式
          條件不成立跳出
        ex:印出0~10的整數
        i=0
        while i<11:
            print(i)
            i+=1
 巢狀迴圈:
     迴圈中的敘述式為另一回圈結構
     巢狀層數不限
     for,while皆可構成巢狀結構
 中斷迴圈:
     break:中斷後直接離開回圈
     continue:中斷後回到迴圈開頭繼續執行
 亂數產生器:     
   import random
   randnum=random.randint(1,100)
   
函式:
 定義:
     將一組具有特定程式功能的程式碼,以獨立的程式結構建\
         立為一個單元,並賦予一個名稱,供後續程式使用
 優點:
     (1)重複性:使用時以呼叫名稱方式執行,不需重複撰寫程\
              式碼
     (2)精簡:無需重覆相同的程式碼
     (3)可讀性:程式不複雜,可讀性高
 宣告函式:
     def 函式名稱(參數....):
         敘述式
         ...
         reture 傳回值
 呼叫:
     函式必須呼叫方可被執行
     呼叫格式:
         無傳回值→函式名稱(參數...)
         有傳回值→變數=函數名稱(參數...)
 函式預設參數值:
     函數宣告時,可指定參數的預設值
     當呼叫函式時,若無指定參數值,則會採用預設參數值
     呼叫函式時全不指定參數,則全部以預設參數值帶入
     預設參數值有設定,不可寫在無預設參數值的前面
'''
print()
#num=eval(input("請輸入整數值"))
num=int(input("請輸入整數值"))
if(num<0):
    num=abs(num)
print("絕對值是%d" % num)
#abs(x):計算x之絕對值
#------------------------------------------
print()
num=eval(input("請輸入任意整數值"))
ren=num%2                   #ren=num除2取餘數
if (ren==0):
    print("%d是偶數" % num)
else:
    print("%d是奇數" % num)
#-----------------------------------------------
'''
ex:輸入圓半徑,計算圓面積
輸出如下:
    圓半徑=~,圓面積=~
    若輸入的半徑直為負數,則輸出:圓半徑不能為負數 
'''
pi=3.14159
radius=eval(input("請輸入圓半徑"))
if radius<0 :
    print("圓半徑不能為負數")
else:
    area=(radius**2*pi)
    print("圓半徑=%d,圓面積=%d" % (radius,area))
    print("圓半徑=",radius,"圓面積",area)
#-------------------------------------------------
a , b , c =eval(input("請輸入a,b,c的值"))
d = b ** 2 - 4*a*c
if d>0:
    print("一元二次方程式有兩個不同的解")
elif d==0:
    print("一元二次方程式只有一個解")
else:
    print("一元二次方程式無解")
print("結束")
'''
ex:
    90分以上>優等
    80分以上>甲等
    70分以上>乙等
    60分以上>丙等
    其餘>不及格
'''
score=eval(input("請輸入考試成績(0~100):"))
if (score>100):
    print("不及格!")
elif (score>=90):
    print("分數評等為優等")
elif score>=80:
    print("分數評等為甲等")
elif score>=70:
    print("分數評等為乙等")
elif score>=60:
    print("分數評等為丙等")
else:
    print("不及格!")
'''
ex:
    輸入  輸出
    1    one   
    2    two
    3    three
    4    four
    5    five
'''
num=eval(input("請輸入1~5的整數"))
if num==1:
    print("one")
elif num==2:
    print("two")
elif num==3:
    print("three")
elif num==4:
    print("four")
elif num==5:
    print("five")
else:
    print("您輸入的資料超出範圍")
#--------------------------------------------
score=eval(input("請輸入考試成績(0~100):"))
if (score<=60):
    print("不及格")
else:
    if (score<=70):
        print("分數評等為丙等")
    else:
        if (score<=80):
            print("分數評等為乙等")
        else:
            if(score<=90):
                print("分數評等為甲等")
            else:
                if(score<=100):
                    print("分數評等為優等")
                else:
                    print("輸入錯誤")
#---------------------------------------------
num=eval(input("請輸入1~5的整數"))
if (num==1):
    print("one")
else:
    if (num==2):
        print("two")
    else:
        if(num==3):
            print("three")
        else:
            if(num==4):
                print("four")
            else:
                if(num==5):
                    print("five")
                else:
                    print("輸入錯誤")
#-------------------------------------------for
#ex:計算1+2+3....+100
sum=0
for a in range(1,101):
    sum+=a              #--敘述1
else:       #敘述1執行完敘述1後才執行
    print("sum=",sum)
#-------------------------------------------
#ex:計算1+2+3....+n
n=eval(input("請輸入終止值"))
sum=0
for a in range(1,n+1):
    sum+=a
else:
    print("sum=",sum)
#-------------------------------------------
#ex:4+9+13+18+22+...+85+90+94+99
#自己想的-----
b=0
sum=0
for a in range(1,23):
    if (a%2==0):
        sum=sum+a/2*9
    else:
        sum=sum+(a-b)*9-5
        b+=1
else:
    print("sum=",sum)

#解1--------
sum=0
for a in range(4,95,9):
    sum+=a
for a in range(9,100,9):
    sum+=a
print("sum=",sum)

#解2---------
'''
sum=0
for a in range(4,95,9):
    sum=sum+a+(a+5)
print("sum=",sum)
'''
#----------------------------------------
#請輸入正整數:6
#6!=720
b=1
sum=eval(input("請輸入正整數"))
for a in range(1,sum+1):
    b=b*a
print("%d階層=%d" % (sum,b))
#---------------------------------------while
#成績登錄系統
#請輸入第X位學生成績(輸入-1結束):
#本班成績:XX分,平均XX分(小數2位)

#自己想的-----
i=0
sum=0
avg=1
buf=0
while buf!=-1:
    i+=1
    sum=sum+buf
    buf=eval(input("請輸入第%d位學生成績 \
(輸入-1結束):"))
i-=1
avg=sum/i 
i=0
print("本班成績:%-5d分,平均%5.2f分" % (sum,avg))

#解
total=person=score=0
while (score!=-1):
    person+=1
    total+=score
    score=int(input("請輸入第%d位學生成績 \
(輸入-1結束):" % person))
average=total/person
print("本班成績:%-5d分,平均%5.2f分" % (total,average))

#------------------20200508-----------------------

#------------------20200511-----------------------
#-------------------------------------------
ex:九九乘法表
#part1
for a in range(1,10):
    for b in range(1,10):
#        print("%1d*%1d=%2d" % (a,b,ans))
        print("%1d*%1d=%2d" % (a,b,a*b),'\t'\
,sep='',end='')
    print()
    
#part2 
for a in range(1,10):
    for b in range(1,10):
        print(a,"*",b,"=",a*b,'\t',sep='',end='')
    print()
    
#part3 
for i in range(1,10):
    for j in range(1,10):
        s=i*j
        if s<10:
            s='0'+str(s)
            #數值不能與字串相+
        print(i,"*",j,"=",s,'\t',sep='',end='')
    print()

#---------------------------------------
ans=input("請輸入[電腦]的英文(輸入QUIT結束)")
while ans.upper()!="COMPUTER":
    if ans.upper()=="QUIT":
        print("不玩了")
        break
    ans=input("請重新請輸入[電腦]英文:")
else:
    print("恭喜!您答對了")
#--------------------------------------
#ex:輸入大樓的樓層數並印出樓層數
n=int(input("請輸入大樓的樓層數:"))
print("本大樓具有的樓層為:")
if n>3:
    n+=1
for i in range(1,n+1): 
    if(i==4):
        continue
    print(i,end=" ")
print()
#--------------------------------------
#ex:輸入層數,以*列印出該層數的直角三角形
#自己想的
n=int(input("請輸入直角三角形層數:"))
for i in range(1,n+1):
    for j in range(i):
        print("*",sep='',end='')
    print()
#解
n=eval(input("請輸入直角三角形層數:"))
for a in range(1,n+1):
    for b in range(0,a):
        print('*',end='')
    print()
'''
a    a<=n    b     b<=a-1    結果
1    v       0     0<=1-1v    *
             1     1<=1-1x     
2    v       0     0<=2-1v    *
             1     1<=2-1v    **
             2     2<=2-1x    
3    v       0     0<=3-1v    *
             1     1<=3-1v    **
             2     2<=3-1v    ***
             3     3<=3-1x

'''
#--------------------------------------------
#自己想的
n=eval(input("請輸入倒直角三角形層數:"))
for a in range(0,n):
    for b in range(0,n-a):
        print('*',end='')
    print()
#解
n=eval(input("請輸入直角三角形層數:"))
for a in range(n,-1,-1): #for a in range(n,0,-1):
    for b in range(1,a+1):
        print('*',end='')
    print()

#-------------------------------------------
#ex:輸入三位整數,判斷此三位式是否為迴文數
#迴文數:又稱對稱數,將數值正.反向排列,如16861
#解
number=eval(input("Enter a three-digit integer:"))
revernumber=(number%10)*100+(number//10%10)*10+\
(number//100)
#//100:除以100後取整數
if number==revernumber:
    print(number,'is a palindrome number.')
else:
    print(number,'is not a palindrome number.')
#---------------------------------------------
#輸入3個數字,由小排到大
num1,num2,num3=eval(input('Enter three integers:'))
if num1>num2:
    num1,num2=num2,num1
if num2>num3:
    num2,num3=num3,num2
if num1>num2:
    num1,num2=num2,num1
print('The sorted numbers are',num1,num2,num3)
#--------------------------------------------
#亂數產生器
import random
x=y=0
for i in range(1,11):
    randnum=random.randint(1,100)
    if randnum % 2 == 0 :
        x+=1
    else:
        y+=1
    print('%-4d' % randnum,end='')
print('\n'"其中有%d個奇數和%d個偶數" % (y,x))
#---------------------------------------------
#用函式印出星號
for i in range(1,21):
    print('*',end='')
print()
for i in range(1,31):
    print('*',end='')
print()
for i in range(1,51):
    print('*',end='')
print()
#---------------------
def start_1(x):
    for i in range(1,x+1):
        print('*',end='')
    print()
def main():
    start_1(20)
    start_1(30)
    start_1(50)
main()

#-------------------------------------------
#ex:建立函式,求出1~100總和(無參數,無傳回值)
def sum1_100():
    a=0
    for i in range(1,101): 
        a+=i
    print("1~100總和為%d" % a)
def main():
    sum1_100()
main()

#ex:建立函式,求出1~100總和(無參數,有傳回值)
def sum2_100():
    a=0
    for i in range(1,101): 
        a+=i
    return a
def main():
    b=sum2_100()
    print("1~100總和為%d" % b)
main()

#ex:建立函式,求出n~m總和(有參數,有傳回值)
def sum2(n,m):
    a=0
    for i in range(n,m+1): 
        a+=i
    return a
def main():
    c,d=eval(input("請輸入整數區間(小,大)"))
    b=sum2(c,d)
    print("%d~%d總和為%d" % (c,d,b))
main()

#ex:建立函式,求出1~100總和(有參數,多個傳回值)
def sumandAverage(n1,n2):
    total = 0
    average=0.0
    for i in range(n1,n2+1): 
        total+=i
    average=total/(n2-n1+1)
    return total,average
def main():
    s,a=sumandAverage(1,100)
    print("Sum = %d , Aveeage = %.2f" % (s,a))
main()

#ex:建立函式,求出1~100總和(有預設參數,多個傳回值)
def sumandAverage(n1,n2=100):
    total = 0
    average=0.0
    for i in range(n1,n2+1): 
        total+=i
    average=total/(n2-n1+1)
    return total,average
def main():
    s,a=sumandAverage(1)
    print("Sum = %d , Aveeage = %.2f" % (s,a))
    s,a=sumandAverage(1,10)
    print("Sum = %d , Aveeage = %.2f" % (s,a))
main()

#-----------------------------------------------   
#ex:請輸入攝氏溫度:36
#攝氏36度=華式96.8度
#公式:華氏=(9/5)*攝氏+32
#1.請以無傳回值方式撰寫
#2.請以有傳回值方式撰寫
#---------------------------
def change():
    s=eval(input("請輸入攝氏溫度:"))
    w=(9/5)*s+32
    print("攝氏%d度=華式%.1f度" % (s,w))
def main():
    change()
main()
#------------------------------
def change():
    s=eval(input("請輸入攝氏溫度:"))
    w=(9/5)*s+32
    return w,s
def main():
    w,s=change()
    print("攝氏%d度=華式%.1f度" % (s,w))
main()


#------------------20200511-----------------------



