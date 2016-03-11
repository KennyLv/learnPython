#!/usr/bin/env python
print('Hello World!')

#Python 文本文件操作
# f = open(文件名，模式)
#最常用的模式有：
# "r"                 # 只读
# "w"                # 写入，如果文件不存在, 会创建这个文件; 如果文件存在, 则将其覆盖，原有的文档内容全抹掉
# "a"                 #追加，打开一个文件用于追加, 文件指针将会指向文件的结尾; 当然, 如果这个文件不存在, 也是会创建这个文件的.
#  r+  w+   a+    # 'r+' --> 'wr'    'w+' --> 'wr'
# 'rb', 'wb', and 'r+b'       #以二进制的形式读写文件, 'b' appended to the mode opens the file in binary mode
#以a+方式打开的文件，指向结尾，以r的方式打开文件，在文件头。

f = open("D:\\HBuild_WorkSpace\\learnPython\\python_base\\demo\\test1.txt","r")

#读取：
#print("f.read()   ", f.read())                      #参数缺省的话是读入所有行，得到的结果是原文（自动换行，不是列表）
#print("f.read(4)   ",f.read(4))                   # 读取N bytes的数据
#print("f.readline()   ",f.readline())           # 读取一行
print("f.readlines()   ", f.readlines() )      # 读取所有行，储存在列表中，每个元素是一行。而f.readlines()得到的结果是元素包含'\n'的列表。

#清空缓冲区：
#f.flush()  

#关闭：
f.close()  

f = open("D:\\HBuild_WorkSpace\\learnPython\\python_base\\demo\\test2.txt","w")
#写入：
f.write('I like apple')      # 将'I like apple'写入文件,write只能写入一行
f.writelines(['a\n','b','c']) #写入list需用f.writelines(['a\n','b','c'])，且不标明\n不予换行
f.write('''
        aa
        bbb
        cc
''') #另外也可以写成所见格式（实质是带编辑器的换行符，因此注意编码）

f.close()


f = open("D:\\HBuild_WorkSpace\\learnPython\\python_base\\demo\\test1.txt","r")
#测试文件偏移位置
f.read(3)
print( f.tell()   )



input('Please enter a code to quit:')