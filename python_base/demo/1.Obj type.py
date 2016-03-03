#!/usr/bin/env python
print('Hello World!')

a=10         # int 整数
print( a,type(a))

a=1.3        # float 浮点数
print( a,type(a))

a=True       # 真值 (True/False)
print( a,type(a))

a='Hello!'   # 字符串
print( a,type(a))

s1 = (2, 1.3, 'love', 5.6, 9, 12, False)   #tuple（定值表； 也有翻译为元组,tuple元素不可变
print (s1, type(s1))


print("字符串是一种特殊的tuple，可以执行元组的相关操作。")
s1_1 = 'abcdef'
print( "s1_1[2:4] =", s1_1[2:4])


s2 = [True,5,'Smile']                       #list (表),list元素可变
print (s2, type(s2))

#由于list的元素可变更，你可以对list的某个元素赋值
#如果你对tuple做这样的操作，会得到错误提示。
s3=[1,2, [3,4,5,6], 7]
print (s3, type(s3))
print (s3[2][3])

s3[2][3]= [0.2,0.3,0.4]
print (s3)

s4=[]                  #空列表
print (s4, type(s4))

s5 = [1,2, 3,4,5,6, 7,8,9,10]
print("s5 =" , s5)
print ("序列的引用通过s[<int>]实现， int为下标: s5[2] = " , s5[2])
print("范围引用： 基本样式[下限:上限:步长]", 
"在范围引用的时候，如果写明上限，那么这个上限本身不包括在内。",
"步长，只得是每隔多少取一个元素 ")
print("s5[:5]:", s5[:5])
print("s5[2:]:", s5[2:])
print("s5[::3]:", s5[::3])
print("s5[0:5:2] :", s5[0:5:2] )
print("s5[0:4:2] :", s5[0:4:2] )
print("如果写明上限，那么这个上限本身不包括在内 , s5[2:0:-1] :", s5[2:0:-1] , ",  s5[2::-1] :", s5[2::-1] )
print("s5[2:0] :", s5[2:0] )
print("尾部元素引用:下标为负数，如果s1[0:-1], 那么最后一个元素不会被引用 （不包括上限元素本身） ")
print("s5[-2]:", s5[-2])
print("s5[0:-3]:", s5[0:-3])




input('Please enter a code to quit:')