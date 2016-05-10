# Written by Vamei
import itertools
import math
import random

'''
##itertools 包
# iter()内置函数，可以将诸如表、字典等容器变为循环器:
for i in iter([2, 4, 5, 6]):
    print(i)

print("无穷循环器: ")
#itertools.count(5, 2)     #从5开始的整数循环器，每次增加2，即5, 7, 9, 11, 13, 15 ...
#itertools.cycle('abc')                    #重复序列的元素，既a, b, c, a, b, c ...
#itertools.repeat(1.2)                     #重复1.2，构成无穷循环器，即1.2, 1.2, 1.2, ...
#repeat也可以有一个次数限制:
#itertools.repeat(10, 5)                 #重复10，共重复5次

#imap函数,与map()函数功能相似，只不过返回的不是序列，而是一个循环器。
#pow(内置的乘方函数)
rlt = itertools.imap(pow, [1, 2, 3], [1, 2, 3])
for num in rlt:
    print(num)

rltu = itertools.starmap(pow, [(1, 1), (2, 2), (3, 3)])
for ult in rltu:
    print(ult)

'''
##math 包
print("math包常数: ")
print(math.e)   # 自然常数e
print(math.pi)  # 圆周率pi

print("运算函数: ")
#可以参考数学手册
print(math.ceil(1.2))       # 对x向上取整，比如x=1.2，返回2
print(math.floor(1.2))      # 对x向下取整，比如x=1.2，返回1
print(math.pow(3, 5))      # 指数运算，得到x的y次方
print(math.log(100))        # 对数，默认基底为e。可以使用base参数，来改变对数的基地。比如math.log(100,base=10)
print(math.sqrt(2))       # 平方根

print("三角函数: ")
#这些函数都接收一个弧度(radian)为单位的x作为参数。
#x = math.pi / 6
x = math.radians(30)
y = math.degrees(x)
print(math.sin(x))
print(math.cos(x)) 
print(math.tan(x)) 
print(math.asin(x)) 
print(math.acos(x)) 
print(math.atan(x) )

print("角度和弧度互换: ")
print(math.degrees(x))
print( math.radians(30))


print("双曲函数:  ")
print(math.sinh(x))
print(math.asinh(y))
print(math.cosh(x))
print(math.acosh(y))
print( math.tanh(x))
print(math.atanh(x))

print("特殊函数:  ")
print(math.erf(x))
print( math.gamma(x))


##random 包
#print("设置随机种子: ")
#print(random.seed(x))
 
print("随机挑选和排序: ")
# 从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
seq = ['1','sdf34','r34rc','f6yh','ver54','dsf45','vce34','er2r','324d','ve','re','2w3','2we']
print(random.choice(seq) )
print(random.sample(seq, 3)) # 从序列中随机挑选k个元素
random.shuffle(seq) # 将序列的所有元素随机排序
for i, name in enumerate(seq):
    print( 'index ', i, ' is '+name)
 
print("随机生成实数: ")
#下面生成的实数符合均匀分布(uniform distribution)，意味着某个范围内的每个数字出现的概率相等:
print(random.random())          # 随机生成下一个实数，它在[0,1)范围内。
print(random.uniform(3,71) )     # 随机生成下一个实数，它在[a,b]范围内。
#下面生成的实数符合其它的分布 (你可以参考一些统计方面的书籍来了解这些分布):
#print(random.gauss(mu,sigma))    # 随机生成符合高斯分布的随机数，mu,sigma为高斯分布的两个参数。 
#print(random.expovariate(lambd)) # 随机生成符合指数分布的随机数，lambd为指数分布的参数。





