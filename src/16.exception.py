#!/usr/bin/env python
# coding: UTF-8

print('Hello World!')

#如果try中有异常发生时，将执行异常的归属，执行except。
#异常层层比较，看是否是exception1, exception2...，直到找到其归属，执行相应的except中的语句。
#如果except后面没有任何参数，那么表示所有的exception都交给这段程序处理。
re1 = iter(range(5))
try:
    #当循环进行到第6次的时候，re.next()不会再返回元素，而是抛出(raise)StopIteration的异常。
    for i in range(100):
        print( re1.__next__())
except StopIteration:
    print ('here is end ',i)
except TypeError:
    print("TypeError")
except:
    print("UnHandled Error")   
print( '=======with exception handle==')


def func():
    try:
        re = iter(range(5))
        for i in range(20):
            print(re.__next__()) 
    except ZeroDivisionError:
         print("ZeroDivisionError")
#如果无法将异常交给合适的对象，异常将继续向上层抛出，直到被捕捉或者造成主程序报错。
#如果try中没有异常，那么except部分将跳过，执行else中的语句。
#finally是无论是否有异常，最后都要做的一些事情。
try:
    print ('----------------------Call func')
    func()
except  StopIteration:
    print ('func   StopIteration')
except  NameError:
    print ('func   NameError')
except:
    print("func   UnHandled Error")   
else:
    print ("func   No exception")
finally:
    print( 'func   running out')

    
#raise exception
def func_ex():
    print( '----------------------Begin func_ex' )
    raise StopIteration()
    print( 'Finished func_ex' )
    
try:
    func_ex()
except  StopIteration:
    print ('func_ex StopIteration')

#自定义异常
class ShortInputException(Exception):
    '''A user -defined exception class'''
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length=length
        self.atleast=atleast

import traceback
try:
    s=input('Enter soemthing --> ')
    if len(s) < 3:
        raise ShortInputException(len(s),3)
except ShortInputException:
    print(traceback.format_exc())
else:
    print( 'Done')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# return 是用于函数返回的，不能打断程序执行，所以try中不能用return。
def func_break(x):
    try:
        print('-----------Begin func_try_return')
        return  x+3
        #return x
    finally:
        print('-----------finally func_try_return')
        return ++x #在Python中++x不会改变x的值x++根本就是错的。。。
   
#无论如何都会执行finally， try的return没有用。
print (func_break(11))

#在中断点并不会退出，而是继续执行finally后，才退出。
import sys
def func_break1(x):
    try:
        print('-----------Begin func_try_return')
        sys.exit()
    finally:
        print('-----------finally func_try_return')
        return ++x  #11
print (func_break1(11))

input('Please enter a code to quit:')



 
 