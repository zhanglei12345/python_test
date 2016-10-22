from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()    #返回当前时间的纪元值，秒
    time.sleep(random.random() * 3)   #返回随机生成的一个实数，它在[0,1)范围内
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)     #最多同时执行4个进程
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()   #调用close()之后就不能继续添加新的Process了
    p.join()    #对Pool对象调用join()方法会等待所有子进程执行完毕
    print('All subprocesses done.')

#如果要启动大量的子进程，可以用进程池的方式批量创建子进程
