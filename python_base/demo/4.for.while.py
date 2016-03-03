#!/usr/bin/env python
print('Hello World!')

#介绍一个新的Python函数range()，来帮助你建立表。
#这个函数的功能是新建一个表。
#这个表的元素都是整数，从0开始，下一个元素比前一个大1， 直到函数中所写的上限 （不包括该上限本身）

idx = range(5)
print( idx, type(idx))


#for 元素 in 序列: 
#    statement
for a in [1,2,3,4,5]:
	print(a)


for a in range(10):
    print(a**2)

for a in list(range(10)):
    print(a*2)

	
	
#while 条件:
#    statement
i=0
while i < 10:
    print( i )
    i = i +3
print('While Finished')

# continue   # 在循环的某一次执行中，如果遇到continue, 那么跳过这一次执行，进行下一次的操作
# break      # 停止执行整个循环

for a in [1,2,3,4,5]:
	if a ==2:
		continue
	if a == 4:
		break
	print(a)



input('Please enter a code to quit:')