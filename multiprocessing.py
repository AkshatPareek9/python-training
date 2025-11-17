from multiprocessing import Process
import time

def compute_square(n):
    print(f"Processing {n}")
    total = n * n
    time.sleep(1)
    print(f"Square: {total}")

processes = []

for i in range(4):
    p = Process(target=compute_square, args=(i,))
    processes.append(p)
    p.start()

for p in processes:
    p.join()

print("All processes finished")
