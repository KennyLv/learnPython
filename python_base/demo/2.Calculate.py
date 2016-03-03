#!/usr/bin/env python
print('Hello World!')


print('数学运算')
print("加法: 1+9 = ", 1+9)        # 加法
print("减法: 1.3-4 = ", 1.3-4 )     # 减法
print("乘法:  3*5 = " ,3*5)        # 乘法
print("除法: 4.5/1.5 = ",  4.5/1.5 )   # 除法
print("乘方 : 3**2 = ", 3**2 )  # 乘方     
print("求余数: 10%3 = ",  10%3    )   # 求余数


print('判断')
print(" 5==6,  ",  5==6)              # =， 相等
print(" 8.0!=8.0  ",  8.0!=8.0 )         # !=, 不等
print(" 3<3, 3<=3  ", 3<3, 3<=3 )       # <, 小于; <=, 小于等于
print(" 4>5, 4>=0 ",  4>5, 4>=0 )      # >, 大于; >=, 大于等于
print(" 5 in [1,3,5]  ", 5 in [1,3,5]  )     # 5是list [1,3,5]的一个元素


print('逻辑运算:True/False之间的运算')
print("True and True, True and False", True and True, True and False)      # and, “与”运算， 两者都为真才是真
print( "True or False", True or False )                                 # or, "或"运算， 其中之一为真即为真
print( "not True", not True )                                         # not, “非”运算， 取反

print(" 5==6 or 3>=3 ", 5==6 or 3>=3)


print('True和False被当作两个整数对象。在进行比较的时候，没有进行类型转换。比如 -1 == True，相当于 -1 == 1. 如果在条件中，比如not -1中，由于not是boolean运算符，所以进行类型装换(not bool(-1)).')

print('0 == True  ....  ', 0 == True)
print('0 == False  ....  ', 0 == False)
print('not 0  ....  ', not 0)
print('1 == True  ....  ', 1 == True)
print('1 == False  ....  ', 1 == False)
print('not 1  ....  ', not 1 )
print('-1 == True   ....  ', -1 == True )
print('-1 == False  ....  ', -1 == False )
print('not -1  ....  ', not -1)
print( "bool(1) ", bool(1)  )
print( "bool(2)  ", bool(2)  )
print( "bool(-1) ", bool(-1)  )
print( "bool(0)", bool(0)  )

print('bool型竟然是int型的子类')
d=[1,2,2,3]
print("d=[1,2,2,3], d[1] = " , d[1])
d[True]="Hello"
print("d=[1,2,2,3], d[True]='Hello',  d[1] = " ,d[1])

print('True和False在判断里面跟在表达式里面是没有任何关系:')

if 2 :
    print('In (if 2 :) , 2 is True')
	
if 2!=True :
    print('In (if 2!=True : ) ,2 is not Ture')
	

input('Please enter a code to quit:')