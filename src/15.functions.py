#!/usr/bin/env python
# coding: UTF-8

print('Hello World!')

#函数(function)。函数也是一个对象，具有属性（可以使用dir()查询）。作为对象，它还可以赋值给其它对象名，或者作为参数传递。

#lambda函数
#   lambda语句中,冒号前是参数,可以有多个,用逗号隔开,冒号右边的返回值
#   lambda返回值是一个函数的地址，也就是函数对象。
func = lambda x,y: x + y
print(func(3,4))

mat=  (lambda x: x**3)( func(3,5) ) 
print( mat )

def func1(fn, a, b):
    print( fn(a, b) )
func1( (lambda x,y: x**2 + y),  6,  9)


#map()函数
#map()是Python的内置函数。它的第一个参数是一个函数对象，一个是包含有多个元素的表。
#map()的功能是将函数对象依次作用于表的每一个元素，每次作用的结果储存于返回的表re中。
#在Python 3.X中，map()的返回值是一个循环对象(一次使用)。可以利用list()函数，将该循环对象转换成表。
map_result = map((lambda x,y: x*y),[1,2,3],[6,7,9])
print(list(map_result))


#filter()函数
#filter函数的第一个参数也是一个函数对象。它也是将作为参数的函数对象作用于多个元素。
#如果函数对象返回的是True，则该次的元素被储存于返回的表中。filter通过读入的函数来筛选数据。(filter()函数是剔除判断结果为False的值吧)
#在Python 3.X中，filter返回的不是表，而是循环对象。
filter_result = filter((lambda x: x>3),[1,2,3,6,7,9])
print(list(filter_result))
filter_result1 = filter((lambda x: x-3),[1,2,3,6,7,9]) # 3-3 = 0, false
print(list(filter_result1))


#reduce()函数
#reduce函数的第一个参数也是函数，但有一个要求，就是这个函数自身能接收两个参数。reduce可以累进地将函数作用于各个参数。
#依次调用lambda函数，每次lambda函数的第一个参数是上一次运算结果，而第二个参数为表中的下一个元素，直到表中没有剩余元素。
#在Python 3.X中，reduce()函数不能直接用的，它被定义在了functools包里面
import functools as tools
reduce_result = tools.reduce((lambda x,y: x+y),[1,2,5,7,9])
print(reduce_result)



input('Please enter a code to quit:')



 
 