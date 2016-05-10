# A program to simulate selling tickets in multi-thread way
# Written by Vamei
import os
import threading
import multiprocessing

#multiprocessing的很大一部份与threading使用同一套API，只不过换到了多进程的情境。

#但在使用这些共享API的时候，我们要注意以下几点:
#在UNIX平台上，当某个进程终结之后，该进程需要被其父进程调用wait，否则进程成为僵尸进程(Zombie)。
#所以，有必要对每个Process对象调用join()方法 (实际上等同于wait)。对于多线程来说，由于只有一个进程，所以不存在此必要性。

#multiprocessing提供了threading包中没有的IPC(比如Pipe和Queue)，效率上更高。
#应优先考虑Pipe和Queue，避免使用Lock/Event/Semaphore/Condition等同步方式 (因为它们占据的不是用户进程的资源)。

#多进程应该避免共享资源。
#在多线程中，我们可以比较容易地共享资源，比如使用全局变量或者传递参数。
#在多进程情况下，由于每个进程有自己独立的内存空间，以上方法并不合适。
#此时我们可以通过共享内存和Manager的方法来共享资源。但这样做提高了程序的复杂度，并因为同步的需要而降低了程序的效率。
#Process.PID中保存有PID，如果进程还没有start()，则PID为None。

# worker function
def worker(sign, lock):
    lock.acquire()
    print(sign, os.getpid())
    lock.release()

# Main
print('Main:',os.getpid())

'''
# Multi-thread
record = []
lock  = threading.Lock()
for i in range(5):
    thread = threading.Thread(target=worker,args=('thread',lock))
    thread.start()
    record.append(thread)

for thread in record:
    thread.join()
'''
if __name__ == '__main__':
    # Multi-process
    record = []
    lock = multiprocessing.Lock()
    for i in range(5):
        process = multiprocessing.Process(target=worker,args=('process',lock))
        process.start()
        record.append(process)

    for process in record:
        process.join()