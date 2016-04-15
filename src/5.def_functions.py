#!/usr/bin/env python
print('Hello World!')

#Python通过位置，知道传入值对应的是函数定义中的第几个参数
#Python有丰富的参数传递方式，还有关键字传递、表传递、字典传递等

#在Python中，当程序执行到return的时候，程序将停止执行函数内余下的语句。
#return并不是必须的，当没有return, 或者return后面没有返回值时，函数将自动返回None。
#None是Python中的一个特别的数据类型，用来表示什么都没有，相当于C中的NULL。
#None多用于关键字参数传递的默认值。
def square_sum(a,b):
    c = a**2 + b**2
    return c 

print(square_sum(2,3))


#基本数据类型的参数：值传递
#表作为参数：指针传递
a = 1
b = [1,2,3]

def change_integer(a):
    a = a + 1
    return a
	
def change_list(b):
    b[0] = b[0] + 1
    return b

#将一个整数变量传递给函数，函数对它进行操作，但原整数变量a不发生变化
print (change_integer(a))
print (a)
a = change_integer(a)
print(a)

#将一个表传递给函数，函数进行操作，原来的表b发生变化。
print (change_list(b))
print (b)

input('Please enter a code to quit:')