# Goal: Compare multithreading vs multiprocessing speed for a CPU-heavy task.

import time
import threading
from multiprocessing import Process

def cpu_task(n):
    total = 0
    for i in range(10000000):
        total += i*n
    return total

# ---------------------
# Multithreading
# ---------------------
def run_threads():
    print("Running with Threads...")
    threads = []
    start = time.time()

    for i in range(4):
        t = threading.Thread(target=cpu_task, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Thread time:", time.time() - start)

# ---------------------
# Multiprocessing
# ---------------------
def run_processes():
    print("Running with Processes...")
    processes = []
    start = time.time()

    for i in range(4):
        p = Process(target=cpu_task, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("Process time:", time.time() - start)


if __name__ == "__main__":
    run_threads()
    run_processes()
