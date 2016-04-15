#!/usr/bin/env python
# coding: UTF-8

print('Hello World!')

#一般生成表的方式
L = []
for x in range(10):
    L.append(x**2)
 
print(L)

#表推导(list comprehension)是快速生成表的方法:
L1= [x**2 for x in range(10)]

#这与生成器表达式类似，只不过用的是中括号。（表推导的机制实际上是利用循环对象，有兴趣可以查阅。）
print(L1)

#Demo：
xl = [1,3,5]
yl = [9,12,13]
L2  = [ x**2 for (x,y) in zip(xl,yl) if y > 10]
print(L2)

input('Please enter a code to quit:')



 
 