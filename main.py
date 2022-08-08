import os
import time
import threading
import multiprocessing

NUM_WORKERS = 4


def only_sleep():
    print("PID' %s, Process Name: %s, Thread Name: %s" % (os.getpid(),
                                                          multiprocessing.current_process().name,
                                                          threading.current_thread().name))
    time.sleep(1)


def crunch_numbers():
    print("PID' %s, Process Name: %s, Thread Name: %s" % (os.getpid(),
                                                          multiprocessing.current_process().name,
                                                          threading.current_thread().name))
    x = 0
    while x < 10000000:
        x += 1


start_time = time.time()
for i in range(NUM_WORKERS):
    only_sleep()
    end_time = time.time()
serial_time = end_time-start_time

start_time = time.time()
threads = [threading.Thread(target=only_sleep) for _ in range(NUM_WORKERS)]
[thread.start() for thread in threads]
[thread.join() for thread in threads]
end_time = time.time()
thread_time = end_time-start_time

start_time = time.time()
processes = [multiprocessing.Process(target=only_sleep) for _ in range(NUM_WORKERS)]
[process.start() for process in processes]
[process.join() for process in processes]
end_time = time.time()
process_time = end_time-start_time


print('Serial time= ', serial_time)
print('Thread time= ', thread_time)
print('Process time= ', process_time)
