#!/usr/bin/env python
# coding: UTF-8

print('Hello World!')
import pickle

# define class
class Bird(object):
    have_feather = True
    way_of_reproduction  = 'egg'

summer = Bird()                 # construct an object
picklesbytes = pickle.dumps(summer)   # serialize object

storePath = 'D:\\HBuild_WorkSpace\\learnPython\\src\\bird.txt'
with open(storePath, 'wb') as newfile:                     # open file with write-mode
    pickleDumpString = pickle.dump(summer, newfile)   # serialize and save object

with open(storePath, 'rb') as existFile:
    newSummer = pickle.load(existFile)   # read file and build object
    print(newSummer.way_of_reproduction)
    

input('Please enter a code to quit:')



 
 