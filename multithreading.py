import threading
import time

def fetch_data(name):
    print(f"Thread {name} started")
    time.sleep(2)  # simulating network delay
    print(f"Thread {name} finished")

threads = []

for i in range(3):
    t = threading.Thread(target=fetch_data, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All threads finished")
