import threading
import time
from .process import Process

class Ring:
    def __init__(self, num_of_processes):
        self.processes = [Process(i, self) for i in range(num_of_processes)]
        self.token_holder = 0
        self.processes[self.token_holder].token = True
        self.lock = threading.Lock()

    def pass_token(self, requester_id):
        with self.lock:
            while self.token_holder != requester_id:
                time.sleep(0.1)
            print(f"Process {requester_id} has the token and is entering the critical section.")
            self.processes[requester_id].section_execution()
            self.release_token(requester_id)
        
    
    def release_token(self, process_id):
        next_process_id = (process_id + 1) % len(self.processes)
        print(f"Process {process_id} has released the token. Passing it to Process {next_process_id}")

        self.processes[process_id].token = False
        self.token_holder = next_process_id
        self.processes[self.token_holder].token = True
        threading.Thread(target=self.pass_token, args=(next_process_id,)).start()  # Pass the token to the next process