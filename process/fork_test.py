import os
print('Process(%s) start...' % os.getpid())
pid = os.fork()
if pid == 0:
    print('I am child process(%s) and my parent is %s.' % (os.getpid(),os.getppid()))
else:
    print('I (%s) just cerated a child process(%s).' % (os.getpid(),pid))

#子进程永远返回0，而父进程返回子进程的ID
