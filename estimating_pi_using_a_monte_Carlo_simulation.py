# https://medium.com/analytics-vidhya/multiprocessing-made-easy-ier-with-databricks-bbe9d444ecbd

# Serial Implementation
from random import random
from time import time
import sys

def throw_dart():
    x = random()
    y = random()

    if (x * x) + (y * y) <= 1:
        return 1

    return 0

def main(iterations: int):
    hits = 0
    start = time()

    for i in range(0, iterations):
        hits = hits + throw_dart()

    end = time()
    pi = (4 * hits) / iterations
    print(pi)
    print(f"Execution time: {end - start} seconds.")

if __name__ == "__main__":
    main(1000000*n)
    
# n = 1
# 3.13908
# Execution time: 0.2518298625946045 seconds.  
# n = 10  
# 3.1410916
# Execution time: 2.8721232414245605 seconds.  
# n = 100 
# 3.14140504
# Execution time: 26.821621417999268 seconds.  
# n = 300
# 3.14168808
# Execution time: 83.27661967277527 seconds.    
  
  
# Parallel Implementation using Multiprocessing
from random import random
from time import time
from multiprocessing import Pool
import sys

def throw_dart(iterations: int) -> int:
    hits = 0

    for i in range(iterations):
        x = random()
        y = random()

        if (x * x) + (y * y) <= 1:
            hits = hits + 1

    return hits

def main(iterations: int, process_count: int):
    pool = Pool(processes=process_count)
    trials_per_process = [int(iterations / process_count)] * process_count

    start = time()

    hits = pool.map(throw_dart, trials_per_process)
    pi = (sum(hits) * 4) / iterations

    end = time()

    print(pi)
    print(f"Execution time: {end - start} seconds.")

if __name__ == "__main__":
    main(1000000*n, core_cnt)  

# 可看出電腦 CPU 數量
multiprocessing.cpu_count()    

# n = 100, core_cnt = 1
# 3.14178588
# Execution time: 21.616569757461548 seconds.
# n = 100, core_cnt = 4
# 3.14158252
# Execution time: 5.387383460998535 seconds.
# n = 100, core_cnt = 16
# 3.14135244
# Execution time: 1.3953862190246582 seconds.
# n = 1000, core_cnt = 16
# 3.1416742
# Execution time: 13.793019771575928 seconds.
# n = 5000, core_cnt = 16
# 3.141573156 (已非常接近實際圓周率)
# Execution time: 68.29774641990662 seconds.

   
