#!/usr/bin/env python
print('Hello World!')

print (dir(list))

nl = [1,2,5,3,5]
print(nl)
print("计数，看总共有多少个5, nl.count(5)  ", nl.count(5) ) 
print("查询 nl 的第一个3的下标,  nl.index(3)  ",  nl.index(3) )  

nl.append(6)
print("在 nl 的最后增添一个新元素6 , nl.append(6)  ", nl)

nl.sort() 
print("对nl的元素排序, nl.sort()   ", nl)

print("从nl中去除最后一个元素，并将该元素返回。nl.pop()  ",  nl.pop() ) 

nl.remove(2)
print("从nl中去除第一个2, nl.remove(2)  " , nl)

nl.insert(0,9)
print("在下标为0的位置插入9, nl.insert(0,9)  ",  nl)

#使用dir(list)的时候，能看到一个属性，是__add__()。从形式上看是特殊方法（下划线，下划线）。
#这个方法定义了"+"运算符对于list对象的意义，两个list的对象相加时，会进行的操作。
ml = [8,7,2,4]
print("nl +  [8,7,2,4]  =  ", nl + ml)

#继承list类，添加对"-"的定义
#__sub__这个方法是个内置方法，对应与减法运算，是基类定义的，在这里只不过是实现了这个接口
class superList(list):
    def __sub__(self, b):
        a = self[:]     # 这里，self是supeList的对象。由于superList继承于list，它可以利用和list[:]相同的引用方法来表示整个对象。
        b = b[:] 
        while len(b) > 0:
            element_b = b.pop()
            if element_b in a:
                a.remove(element_b)
        #return a
        return superList(a)
            
print( superList([1,2,3]) - [3,4] )
print( superList([1,2,3]) - superList([3,4])-[2,2] )



input('Please enter a code to quit:')