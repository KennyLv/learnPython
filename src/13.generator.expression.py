#!/usr/bin/env python
# coding: UTF-8

print('Hello World!')

#循环对象是这样一个对象，它包含有一个next()方法(__next__()方法，在python 3x中)， 这个方法的目的是进行到下一个结果，而在结束一系列结果之后，举出StopIteration错误。
#当一个循环结构（比如for）调用循环对象时，它就会每次循环的时候调用next()方法，直到StopIteration出现，for循环接收到，就知道循环已经结束，停止调用next()。

#生成器(generator)的主要目的是构成一个用户自定义的循环对象。
#生成器的编写方法和函数定义类似，只是在return的地方改为yield。生成器中可以有多个yield。
#当生成器遇到一个yield时，会暂停运行生成器，返回yield后面的值。
#当再次调用生成器的时候，会从刚才暂停的地方继续运行，直到下一个yield。
def gen():
    a = 100
    yield a
    a = a*8
    yield a
    yield 1000

for i in gen():
    print(i)


#生成器自身又构成一个循环器，每次循环使用一个yield返回的值。
def genRan():
    for i in range(4):
        yield i

gR = genRan()
for i in gR:
    print(i)
print('====只能迭代一次===')
for i in gR:
    print(i)


 # 生成器表达式(Generator Expression): 
print('====生成器表达式===')
G = (x for x in range(4))

for i in G:
    print(i)
print('====只能迭代一次===')
# generator expression只能迭代一次，同iterator和generator不同
for i in G:
    print(i)
 
input('Please enter a code to quit:')



 
 