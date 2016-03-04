#!/usr/bin/env python
print('Hello World!')

print(dir(dict))
#词典 (dictionary)。与列表相似，词典也可以储存多个元素。这种储存多个元素的对象称为容器(container)。
#词典和表类似的地方，是包含有多个元素，每个元素以逗号分隔。
#但词典的元素包含有两部分，键和值
#键的数据类型是不可变的数据类型，常见的是以字符串来表示键，也可以使用数字或者真值来表示键。
#值可以是任意对象。键和值两者一一对应。
dic = {'tom':11, 'sam':57,'lily':100}
print(type(dic), dic)

#与表不同的是，词典的元素没有顺序,你不能通过下标引用元素。
#词典是通过键来引用。
print( dic['tom'] )
dic['tom'] = 30
print (dic)

#构建一个新的空的词典：
dic_1= {}
print( dic_1)

#在词典中增添一个新元素的方法：引用一个新的键，并赋予它对应的值。
dic_1['lilei'] = 99
print (dic_1)

#在循环中，dict的每个键，被提取出来，赋予给key变量。
dic_2 = {'lilei': 90, 'lily': 100, 'sam': 57, 'tom': 90}
print (dic_2) # 输出结果显示： dic中的元素是没有顺序的。
for key in dic_2:
    print( dic_2[key] ) 
for key in dic_2:
    print( key, dic_2[key] ) 


#dict的常用操作
dic_3 = {'lilei': 90, 'lily': 100, 'sam': 57, 'tom': 90}
print("dic_3 : ", dic_3)
print("返回dic所有的键 ,  dic_3.keys() :  ", dic_3.keys() )
print("返回dic所有的值,   dic_3.values() : ", dic_3.values() )
print("返回dic所有的元素（键值对）,  dic_3.items() : ", dic_3.items() )
print("用len()查询词典中的元素总数,  len(dic_3) :  ", len(dic_3) )
#另外有一个很常用的用法：del是Python中保留的关键字，用于删除对象。
del dic_3['tom'] 
print("删除 dic 的‘tom’元素, del dic_3['tom']  ", dic_3)
dic_3.clear() 
print("清空dic, dic_3.clear()    ", dic_3)


dic_4 = {1: 90, 2: 100, 3: 57, 4: 90}
print("dic_4 : ", dic_4)




input('Please enter a code to quit:')