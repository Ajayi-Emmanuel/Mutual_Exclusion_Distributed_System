import time
import random
import threading
from classes.ring import Ring

def process_task(process):
    time.sleep(random.uniform(1, 3))
    process.make_request()

num_processes = 5
ring = Ring(num_processes)

ring.processes[ring.token_holder].make_request()

threads = []

for process in ring.processes:
    if not process.token: 
        t = threading.Thread(target=process_task, args=(process,))
        threads.append(t)
        t.start()

for t in threads:
    t.join()
