#!/usr/bin/env python
# coding: UTF-8

print('Hello World!')

import os

path = 'D:\\HBuild_WorkSpace\\learnPython\\src\\testdata.txt'

print( os.getcwd() ) #获取当前工作目录
os.chdir("目标目录") #更换当前工作目录


print('basename : ' , os.path.basename(path))    # 查询路径中包含的文件名
print('dirname     : ' , os.path.dirname(path))     # 查询路径中包含的目录
print('split path     : ' , os.path.split(path))   # 将路径分割成文件名和目录两个部分，放在一个表中返回
print(os.path.exists(path))    # 查询文件是否存在
print(os.path.getsize(path))   # 查询文件大小
print(os.path.getatime(path))  # 查询文件上一次读取的时间
print(os.path.getmtime(path))  # 查询文件上一次修改的时间
print(os.path.isfile(path))    # 路径是否指向常规文件
print(os.path.isdir(path))     # 路径是否指向目录文件

path2 = os.path.join( 'D:', '\\', 'HBuild_WorkSpace', 'learnPython', 'src', 'testdata.txt')  # 使用目录名和文件名构成一个路径字符串
print('-----', path2);

p_list = [path, path2]
print(os.path.commonprefix(p_list))    # 查询多个路径的共同部分

'''
os包包括各种各样的函数，以实现操作系统的许多功能。这个包非常庞杂。os包的一些命令就是用于文件管理。我们这里列出最常用的:

mkdir(path)

创建新目录，path为一个字符串，表示新目录的路径。相当于$mkdir命令

rmdir(path)

删除空的目录，path为一个字符串，表示想要删除的目录的路径。相当于$rmdir命令

listdir(path)

返回目录中所有文件。相当于$ls命令。

 

remove(path)

删除path指向的文件。

rename(src, dst)

重命名文件，src和dst为两个路径，分别表示重命名之前和之后的路径。 

 

chmod(path, mode)

改变path指向的文件的权限。相当于$chmod命令。

chown(path, uid, gid)

改变path所指向文件的拥有者和拥有组。相当于$chown命令。

stat(path)

查看path所指向文件的附加信息，相当于$ls -l命令。

symlink(src, dst)

为文件dst创建软链接，src为软链接文件的路径。相当于$ln -s命令。

 

getcwd()

查询当前工作路径 (cwd, current working directory)，相当于$pwd命令。
'''

dirPath = os.path.dirname(path)
os.mkdir(dirPath + "\\new_dir")

'''
glob包最常用的方法只有一个, glob.glob()。
该方法的功能与Linux中的ls相似(参看Linux文件管理命令)，接受一个Linux式的文件名格式表达式(filename pattern expression)，列出所有符合该表达式的文件（与正则表达式类似），将所有文件名放在一个表中返回。
所以glob.glob()是一个查询目录下文件的好方法。

该文件名表达式的语法与Python自身的正则表达式不同 (你可以同时看一下fnmatch包，它的功能是检测一个文件名是否符合Linux的文件名格式表达式)。 
'''
import  glob
print(glob.glob('D:\\HBuild_WorkSpace\\learnPython\\src\\*'))

import shutil
shutil.copy(path, 'D:\\HBuild_WorkSpace\\learnPython\\src\\testdata_copy.txt')



input('Please enter a code to quit:')



 
 