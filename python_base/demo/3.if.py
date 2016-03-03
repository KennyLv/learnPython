#!/usr/bin/env python
print('Hello World!')

i = 1
print ('i = 1')
if i > 0:
    print ('positive i')
    i = i + 1
elif i == 0:
    print ('i is 0')
    i = i * 10
else:
    print ('negative i')
    i = i - 1
print( 'new i:', i )

j  = 5
print ('j = 5')
if j > 1:
    print ('j bigger than 1')
    print ('good')
    if j > 2:
        print ('j bigger than 2')
        print ('even better')

input('Please enter a code to quit:')