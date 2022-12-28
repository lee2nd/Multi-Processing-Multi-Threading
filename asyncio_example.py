# https://stackoverflow.com/questions/50757497/simplest-async-await-example-possible-in-python

# sequential
import time

def count():
    time.sleep(1)
    print('1')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('3')

def main():
    for i in range(3):
        count()

if __name__ == "__main__":
    t = time.perf_counter()
    main()
    t2 = time.perf_counter()
    
    print(f'Total time elapsed: {t2:0.2f} seconds')

# parallel    
import asyncio
import time

async def count():
    await asyncio.sleep(1)
    print('1')
    await asyncio.sleep(1)
    print('2')
    await asyncio.sleep(1)
    print('3')

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    t = time.perf_counter()
    asyncio.run(main())
    t2 = time.perf_counter()

    print(f'Total time elapsed: {t2:0.2f} seconds')
