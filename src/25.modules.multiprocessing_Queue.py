# Written by Vamei
import os
import multiprocessing
import time
#==================
# input worker
def inputQ(queue):
    #一些进程使用put()在Queue中放入字符串，这个字符串中包含PID和时间。
    info = str(os.getpid()) + '(put):' + str(time.time())
    queue.put(info)

# output worker
def outputQ(queue,lock):
    #另一些进程从Queue中取出，并打印自己的PID以及get()的字符串
    info = queue.get()
    lock.acquire()
    print (str(os.getpid()) + '(get):' + info)
    lock.release()
#===================

if __name__ == '__main__':
    # Main
    record1 = []   # store input processes
    record2 = []   # store output processes
    lock  = multiprocessing.Lock()    # To prevent messy print
    
    # Queue与Pipe相类似，都是先进先出的结构。
    #但Queue允许多个进程放入，多个进程从队列取出对象。
    #Queue使用mutiprocessing.Queue(maxsize)创建，maxsize表示队列中可以存放对象的最大数量。
    queue = multiprocessing.Queue(5)

    # input processes
    for i in range(3):
        process = multiprocessing.Process(target=inputQ,args=(queue,))
        process.start()
        record1.append(process)

    # output processes
    for i in range(3):
        process = multiprocessing.Process(target=outputQ,args=(queue,lock))
        process.start()
        record2.append(process)

    for p in record1:
        p.join()
    
    print("=====queue closed========")
    queue.close()  # No more object will come, close the queue

    for p in record2:
        p.join()