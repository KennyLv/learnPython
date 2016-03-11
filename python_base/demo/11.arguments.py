#!/usr/bin/env python
# coding: UTF-8

print('Hello World!')

##函数(function)参数(arguments)的传递
def fun1(a,b,c,d):
    print( a , '+' , d, '-' , b, '+', c)
    return a+d-b+c

#位置传递
print(fun1(1,2,3,4))
#关键字传递
print(fun1(c=3,b=2,a=1, d=4))
#关键字传递可以和位置传递混用。但位置参数要出现在关键字参数之前：
print(fun1(1,2,d=4,c=3))


##参数的默认值
#在定义函数的时候，使用形如a=19的方式，可以给参数赋予默认值(default)。如果该参数最终没有被传递值，将使用该默认值。函数参数的默认值只能放在参数的最后，
def fun2(a, b, c=10):
    print (a, '+', b, '+', c)
    return a+b+c

#使用默认值
print(fun2(3,2))
#使用传入值
print(fun2(3,2,1))


##包裹传递
#有时候并不知道调用的时候会传递多少个参数，包裹(packing)位置参数，或者包裹关键字参数，来进行参数传递，会非常有用。
#在func的参数表中，所有的参数被name收集，根据位置合并成一个元组(tuple)，这就是包裹位置传递。
#为了提醒Python参数，name是包裹位置传递所用的名，包裹传递的关键在于定义函数时，在相应元组或字典前加*或**。
#tuple
def fun3(*name):
    print( type(name))
    return name

print(fun3(1,4,6))
print(fun3(5,6,7,1,2,3))

#dict
def fun4(**name):
    print( type(name))
    return name

print( fun4(a=1, b=9))
print( fun4(sda="dads", c=9, m=20.151))

##解包裹
def fun5(a,b,c,d):
    print('--------------')
    print( a ,b, c, d)

args1=(1,2,3,4)
fun5(*args1)
args2 = {'a':1,'b':2,'c':3,'d':4}
fun5(**args2) #无序输出Value
fun5(*args2) #无序输出Key

##NOTE
# 1, 在定义或者调用参数时，参数的几种传递方式可以混合。但在过程中要小心前后顺序。基本原则是，先位置，再关键字，再包裹位置，再包裹关键字，并且根据上面所说的原理细细分辨。
#2, 注意定义时和调用时的区分。包裹和解包裹并不是相反操作，是两个相对独立的过程。


input('Please enter a code to quit:')



 
 