from threading import Thread

# 定义多线程
class MyThreads (Thread):
    def __init__(self,
            threadName, # 线程名
            que,        # 队列名
            function):  # 函数名
        Thread.__init__(self)
        self.name = threadName
        self.que = que
        self.function=function

    def run(self):
        print("开始：" + self.name)
        while True:
            try:
                self.function(self.que)
            except:
                break
        print("退出：" + self.name)


# 多线程使用方法：
    # 1.定义执行函数
        # def func(queue):
        #     try:
        #         pass
        #     except expression as identifier:
        #         pass
    # 2.建立线程名列表和数据队列
        # threadList = ['thread-1','thread-2',...]
        # dataQ = queue  # from queue import Queue
    # 3.构造多线程，启动并添加到线程列表
        # threads = []
        # for tName in threadList:
        #     thread = MyThreads(tName, dataQ, func)
        #     thread.start()
        #     threads.append(thread)
    # 4.阻塞主线程
    # for t in threads:
    #     t.join()

# 演示
def demo():
    print('-Begin-')
    from queue import Queue
    # 第一步
    def func(que):
        data = que.get(timeout=2)
        try:
            print(data + 1)
        except:
            print(0)
    # 第二步
    threadList = []
    for i in range(3):
        threadList.append("thread-"+str(i))
    dataQ = Queue()
    for i in range(100):
        dataQ.put(i)
    # 第三步
    threads = []
    for tName in threadList:
        thread = MyThreads(tName, dataQ, func)
        thread.start()
        threads.append(thread)
    # 第四步
    for t in threads:
        t.join()
    print('-End-')
# 
# demo()