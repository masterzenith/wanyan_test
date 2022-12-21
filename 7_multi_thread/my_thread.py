"""
Logic explanation is in multi_thread.md
"""
import threading
import time

instance_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


class my_thread(threading.Thread):
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.threadId = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print("开始线程:", self.name)
        # 获得锁，成功获得锁定后返回 True
        # 可选的timeout参数不填时将一直阻塞直到获得锁定
        # 否则超时后将返回 False
        threadLock.acquire()
        print_time(self.name, self.counter, instance_list.__len__())
        # 释放锁
        threadLock.release()

    def __del__(self):
        print(self.name, "线程结束！")


def print_time(thread_name, delay, counter):
    while counter:
        time.sleep(delay)
        instance_list[counter - 1] += 1
        print("[%s] %s 修改第 %d 个值，修改后值为:%d" % (time.ctime(time.time()), thread_name, counter, instance_list[counter - 1]))
        counter -= 1


threadLock = threading.Lock()
threads = []
# 创建新线程
thread1 = my_thread(1, "Thread-1", 1)
thread2 = my_thread(2, "Thread-2", 2)
# 开启新线程
thread1.start()
thread2.start()
# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)
# 等待所有线程完成
for t in threads:
    t.join()
print("主进程结束！")
