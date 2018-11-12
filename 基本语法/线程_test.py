
import  threading
from time import sleep
def thread_func(x):
    print ('%d\n' % (x * 100))
    sleep(10)
threads = []

for i in range(5):
    print (i)
    threads.append(threading.Thread(target = thread_func ,args = (i,)))

for thread in threads:
    thread.start()

#for thread in threads:
#    thread.join()

