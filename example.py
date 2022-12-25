from multiprocessing.pool import Pool
import uuid
import datetime

def handleTask(uuid_gen):
    return ''.join([uuid_gen().hex for i in range(16384)])

if __name__ == '__main__':
    start = datetime.datetime.now()
    tasks = [uuid.uuid4 for i in range(64)]

    enable_multiprocess = False # 改這個來切換循序跟平行
    if enable_multiprocess:
        pool = Pool()
        result = ''.join(pool.map(handleTask, tasks))
    else:
        result = ''.join([handleTask(task) for task in tasks])  
    # 由於 UUID 會產生隨機字串，在這邊確認兩個版本長度相同即可
    print('result length: ', len(result))
    print(datetime.datetime.now() - start)

# enable_multiprocess = True
# result length:  33554432
# 0:00:00.869642

# enable_multiprocess = False
# result length:  33554432
# 0:00:02.559713
