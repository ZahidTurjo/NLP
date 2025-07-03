import threading
from concurrent.futures import ThreadPoolExecutor
import time
def func(seconds):
    print(f'tik {seconds}')
    time.sleep(seconds)
    # print(f"after{seconds} seconds ok")

def main():
    t1=threading.Thread(target=func,args=[7])
    t2=threading.Thread(target=func,args=[2])
    t3=threading.Thread(target=func,args=[1])

    t1.start()
    t2.start()
    t3.start()
def thrdPool():
    with ThreadPoolExecutor(max_workers=1) as executor:
        future1 = executor.submit(func,3)
        future2 = executor.submit(func,2)
        future1.result()
        future2.result()


thrdPool()