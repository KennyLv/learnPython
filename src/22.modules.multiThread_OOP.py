# A program to simulate selling tickets in multi-thread way
# Written by Vamei

import threading
import time
import os

# This function could be any function to do other chores.
def doChore():
    time.sleep(0.5)

# Function for each thread
#自己定义了一个继承自thread.Threading的类BoothThread
class BoothThread(threading.Thread):
    def __init__(self, tid, monitor):
        self.tid          = tid
        self.monitor = monitor
        threading.Thread.__init__(self)
    def run(self):
        while True:
            monitor['lock'].acquire()                          # Lock; or wait if other thread is holding the lock
            if monitor['tick'] != 0:
                monitor['tick'] = monitor['tick'] - 1          # Sell tickets
                print(self.tid,':now left:',monitor['tick'])   # Tickets left
                doChore()                                      # Other critical operations
            else:
                print("Thread_id",self.tid," No more tickets")
                os._exit(0)                                    # Exit the whole process immediately
            monitor['lock'].release()                          # Unblock
            # print("Thread_id",self.tid," ideal now")
            doChore()            # Non-critical operations

# Start of the main function
#使用了一个词典monitor存放全局变量，然后把词典作为参数传递给线程函数。
#由于词典是可变数据对象，所以当它被传递给函数的时候，函数所使用的依然是同一个对象，相当于被多个线程所共享。
monitor = {'tick':34, 'lock':threading.Lock()}

# Start 10 threads
for k in range(5):
    new_thread = BoothThread(k, monitor)
    new_thread.start()