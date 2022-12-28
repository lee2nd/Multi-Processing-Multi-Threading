# https://stackoverflow.com/questions/5442910/how-to-use-multiprocessing-pool-map-with-multiple-arguments
def multi_run_wrapper(args):
   return add(*args)

def add(x,y):
    return x+y

if __name__ == "__main__":
    from multiprocessing import Pool
    pool = Pool(4)
    results = pool.map(multi_run_wrapper,[(1,2),(2,3),(3,4)])
    print results

# https://superfastpython.com/threadpool-map-multiple-arguments/   
from time import sleep
from random import random
from multiprocessing.pool import ThreadPool
 
# task function executed in a worker thread
def task(arg1, arg2, arg3):
    # block for a moment
    sleep(random())
    # report values
    print(f'Task {arg1}, {arg2}, {arg3}.')
    # return a result
    return arg1 + arg2 + arg3
 
# protect the entry point
if __name__ == '__main__':
    # create the thread pool
    with ThreadPool() as pool:
        # issue multiple tasks each with multiple arguments
        async_results = [pool.apply_async(task, args=(i, i*2, i*3)) for i in range(10)]
        # retrieve the return value results
        results = [ar.get() for ar in async_results]
