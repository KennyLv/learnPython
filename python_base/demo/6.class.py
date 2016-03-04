#!/usr/bin/env python
print('Hello World!')

#定义（其实是继承自object）
class Bird(object):
    #变量属性(attribute)
    have_feather = True
    way_of_reproduction  = 'egg'
    
    #方法属性(method)
    #它的参数中有一个self，它是为了方便我们引用对象自身。
    #类中的方法第一个参数必须是调用该方法的对象本身，可以指定为任何名字的参数，取为sel、this、it等等都可以
    
    #初始化函数 ： __init__(),如果你在类中定义了__init__()这个方法，创建对象时，Python会自动调用这个方法。
    def __init__(self):
        print("Bird is initinalized")
    #类函数
    def move(self, dx, dy):
        position=[0,0]
        position[0] = position[0] + dx
        position[1] = position[1] + dy
        return position
    def have_f(this):
        return this.way_of_reproduction + ' is good!'
 
    
class Fish(object):
    swimming = True
        
#单继承(inheritance)
class Chicken(Bird):
    way_of_move = 'walk'
    possible_in_KFC = True
    
summer = Chicken()
print(type(summer), summer.way_of_reproduction)
print('after move: ', summer.move(5,8))
print('after move: ', summer.have_f())

#多继承
class FishBird(Bird, Fish):
    def getMethods():
        print('-----------')
        
winter = FishBird()
print(type(winter), winter.swimming)
print('after move: ', summer.move(5,8))

#共享对象
#1、对象不能修改类的属性，只能修改自己的，也就是说，修改了之后对同类的其他对象没有影响；
#2、动态修改类属性可以用类名.属性 = xxx来进行修改；
#3、修改的类属性一般会影响所辖对象的属性，除非对象在此之前对该属性进行过修改。

#属性都是immutable的(比如整数、字符串)，在更改对象属性时，如果属性是immutable的，该属性会被复制出一个副本，存放在对象的__dict__中。
#如果属性是mutable的话(比如list)，在更改属性值时，并不会有新的副本。所以更改会被所有的对象看到。
#为了避免混淆，最好总是区分类属性和对象的属性，而不能依赖上述的immutable属性的复制机制。

class Human(object):
    gender = ''  
    name = ["", ""]
    def __init__(self, input_gender,input_name):
        if input_gender:
            self.gender = input_gender
        self.name[0] = input_name
    def printGender(self):
        print(self.gender,self.name)

li_lei = Human('male','LI') # 这里，'male'作为参数传递给__init__()方法的input_gender变量。
hanmeimei = Human('female', 'HAN') 
kk_unknow = Human(False, 'KK')  #gender不做修改, 名称都被改掉

li_lei.printGender()
hanmeimei.printGender()
kk_unknow.printGender()
print(li_lei.gender)
print(hanmeimei.gender)
print(kk_unknow.gender)

Human.gender='unknow' #类属性变更
print(kk_unknow.gender)

#内置函数
#dir()用来查询一个类或者对象所有属性
print (dir(Bird))




input('Please enter a code to quit:')