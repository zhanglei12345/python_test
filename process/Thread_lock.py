import threading, time

count = 0
#创建锁
lock = threading.Lock()

def doAdd():
    '''
	将全局变量count 逐一的增加1。
    '''
    global count, lock
    #加锁
    lock.acquire()
    count = count + 1
    #释放锁
    lock.release()

for i in range(5):
    threading.Thread(target = doAdd, args = (), name = 'thread-' + str(i)).start()

time.sleep(2)#确保线程都执行完毕
print('count=[%s]' %  count)

#用于实现多线程同步，在修改全局变量count之前加锁，这样在修改时其他线程就会等待。最后记得释放锁。

#lock = threading.Lock()  创建锁
#lock.acquire()  获取锁
#lock.release()  释放锁
