# date :2019-09-12
# author : shencheng
import threading
import time

list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


class myThread(threading.Thread):
    def __init__(self, threadId, name, counter):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.counter = counter

    def run(self):
        print("开始线程:{}", format(self.name))
        # 获得锁,成功后返回True
        # 可选的timeout 参数不填时将一直阻塞知道获得锁定
        # 否则超时后返回false
        threadLock.acquire()
        print_time(self.name, self.counter, list.__len__())     # list.__len__() 相当于len(list)
        # print("list.__len__():%s" % list.__len__())
        # 释放锁
        threadLock.release()

    def __del__(self):
        print("{}, 线程结束", format(self.name))


def print_time(threadNmae, delay, counter):
    while counter:
        time.sleep(delay)
        list[counter - 1] += 1
        print("[%s] %s 修改第 %d 个值, 修改后值为%d" % (time.ctime(time.time()), threadNmae, counter, list[counter - 1]))
        counter -= 1


threadLock = threading.Lock()
threads = []

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for i in threads:
    i.join()

print("主进程结束")
