# Written by Vamei
import multiprocessing as mul

def f1(x):
    return x**2

def f2(n, a):
    n.value   = 3.14
    a[0]      = 5

def f3(x, arr, l):
    x.value = 3.14
    arr[0] = 5
    l.append('Hello')
    
if __name__ == '__main__':
    # 进程池
    #我们创建了一个容许3个进程的进程池 (Process Pool) 。
    #Pool还有下面的常用方法。
    #   apply_async(func,args)  从进程池中取出一个进程执行func，args为func的参数。它将返回一个AsyncResult的对象，你可以对该对象调用get()方法以获得结果。
    #   close()  进程池不再创建新的进程
    #   join()   wait进程池中的全部进程。必须对Pool先调用close()方法才能join。
    pool = mul.Pool(3) 
    #利用map()方法，将f1()函数作用到表的每个元素上。用5个进程并行处理。
    #如果进程运行结束后，还有需要处理的元素，那么的进程会被用于重新运行f1()函数。
    rel  = pool.map(f1,[1,2,3,4,5,6,7,8,9,10]) 
    print(rel)
    
    # 共享资源
    #这里我们实际上只有主进程和Process对象代表的进程。
    #在Process进程中，我们修改了Value和Array对象。回到主程序，打印出结果，主程序也看到了两个对象的改变，说明资源确实在两个进程之间共享。
    num   = mul.Value('d', 0.0)
    arr   = mul.Array('i', range(10))
    p = mul.Process(target=f2, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])
    
    # Manager
    #Manager对象类似于服务器与客户之间的通信 (server-client)，与我们在Internet上的活动很类似。
    #我们用一个进程作为服务器，建立Manager来真正存放资源。
    #其它的进程可以通过参数传递或者根据地址来访问Manager，建立连接后，操作服务器上的资源。
    #在防火墙允许的情况下，我们完全可以将Manager运用于多计算机，从而模仿了一个真实的网络情境。
    #下面的例子中，我们对Manager的使用类似于shared memory，但可以共享更丰富的对象类型。
    server = mul.Manager()
    x    = server.Value('d', 0.0)
    arr  = server.Array('i', range(10))
    #Manager利用list()方法提供了表的共享方式。
    #实际上你可以利用dict()来共享词典，Lock()来共享threading.Lock(注意，是threading.Lock，而不是进程的mutiprocessing.Lock。后者本身已经实现了进程共享)等。 
    #这样Manager就允许我们共享更多样的对象。
    l    = server.list()

    proc = mul.Process(target=f3, args=(x, arr, l))
    proc.start()
    proc.join()
    print(x.value)
    print(arr)
    print(l)
    
    
    