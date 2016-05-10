# Multiprocessing with Pipe
# Written by Vamei

import multiprocessing as mul

def proc1(pipe):
    pipe.send('hello')
    print('proc1 rec:',pipe.recv())

def proc2(pipe):
    print('proc2 rec:',pipe.recv())
    pipe.send('hello, too')

if __name__ == '__main__':
    #1) Pipe可以是单向(half-duplex)，也可以是双向(duplex)。
    #我们通过mutiprocessing.Pipe(duplex=False)创建单向管道 (默认为双向)。
    #一个进程从PIPE一端输入对象，然后被PIPE另一端的进程接收，单向管道只允许管道一端的进程输入，而双向管道则允许从两端输入。
    
    # Build a pipe
    #Pipe对象建立的时候，返回一个含有两个元素的表，每个元素代表Pipe的一端(Connection对象)。
    pipe = mul.Pipe()
    
    #我们对Pipe的某一端调用send()方法来传送对象，在另一端使用recv()来接收。
    # Pass an end of the pipe to process 1
    p1   = mul.Process(target=proc1, args=(pipe[0],))
    # Pass the other end of the pipe to process 2
    p2   = mul.Process(target=proc2, args=(pipe[1],))
    p1.start()
    p2.start()
    
    #p1.join()
    #p2.join()