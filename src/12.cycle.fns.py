#!/usr/bin/env python
# coding: UTF-8

print('Hello World!')

print("range()")
#在Python中，for循环后的in跟随一个序列的话，循环每次使用的序列元素，而不是序列的下标。
#之前我们已经使用过range()来控制for循环。现在，我们继续开发range的功能，以实现下标对循环的控制：
#在range函数中，分别定义上限，下限和每次循环的步长。
S = 'abcdefghijk'
for i in range(0,len(S),2):
    print(S[i]) 

print("enumerate()")
#利用enumerate()函数，可以在每次循环中同时得到下标和元素：
#实际上，enumerate()在每次循环中，返回的是一个包含两个元素的定值表(tuple)，两个元素分别赋予index和char
S = 'abcdefghijk'
for (index,char) in enumerate(S):
    print( index )
    print( char )


 
print("zip()")
#如果你多个等长的序列，然后想要每次循环时从各个序列分别取出一个元素，可以利用zip()方便地实现：
#每次循环时，从各个序列分别从左到右取出一个元素，合并成一个tuple，然后tuple的元素赋予给a,b,c
#zip()函数的功能，就是从多个列表中，依次各取出一个元素。每次取出的(来自不同列表的)元素合成一个元组，合并成的元组放入zip()返回的列表中。
#zip()函数起到了聚合列表的功能。
ta = [1,2,3]
tb = [9,8,7]
tc = ['a','b','c']
for (a,b,c) in zip(ta,tb,tc):
    print(a,b,c)
  
 
input('Please enter a code to quit:')



 
 