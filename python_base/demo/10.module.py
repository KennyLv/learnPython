#!/usr/bin/env python
# coding: UTF-8

print('Hello World!')

# Python引入模块的引入方式
# import a as b             # 引入模块a，并将模块a重命名为b
#from a import function1   # 从模块a中引入function1对象。调用a中对象时，我们不用再说明模块，即直接使用function1，而不是a.function1。
#from a import *           # 从模块a中引入所有对象。调用a中对象时，我们不用再说明模块，即直接使用对象，而不是a.对象。

#Python会在以下路径中搜索它想要寻找的模块：
#        程序所在的文件夹
#        标准库的安装路径
#        操作系统环境变量PYTHONPATH所包含的路径
#如果你有自定义的模块，或者下载的模块，可以根据情况放在相应的路径，以便Python可以找到。

#可以将功能相似的模块放在同一个文件夹（比如说this_dir）中，构成一个模块包。
#        通过import this_dir.module 引入this_dir文件夹中的module模块。
#        该文件夹中必须包含一个__init__.py的文件，提醒Python，该文件夹为一个模块包。
#        __init__.py可以是一个空文件。
#        3.x版本不需要__init__.py这个文件，但是文件夹中自动新建了__pycache__文件夹

# import 文件夹.模块名 的方式貌似只可以从父目录调用子目录中的模块
#        import sys
#        sys.path.append('父目录路径')
#        import c
#这种方式无论从父目录模块调用子目录模块，还是从子目录模块调用父目录模块都可以

#import sys 
#print(sys.getdefaultencoding())

import modules.fileOperater as fileHelper

#引入模块后，可以通过模块.对象的方式来调用引入模块中的某个对象。
files = fileHelper.openFiles("D:\\HBuild_WorkSpace\\learnPython\\python_base\\demo\\test3.txt")
stringLines = files. readlines()
files.close()

for strline in stringLines:
    strline = strline.encode("utf-8")
    print(strline.upper())
    #strline.replace('\n','')
    #strline.replace('','')
    #print(strline)


input('Please enter a code to quit:')



 
 