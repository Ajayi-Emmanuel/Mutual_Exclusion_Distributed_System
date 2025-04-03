import time
import random

class Process:
    def __init__(self, process_id, ring):
        self.process_id = process_id
        self.ring = ring
        self.token = False

    def make_request(self):
        if self.token:
            print(f"Process {self.process_id} is requesting critical section.")
            self.ring.pass_token(self.process_id)

    def section_execution(self):
        print(f"Process {self.process_id} is executing critical section.")
        time.sleep(random.uniform(1, 3))
        print(f"Process {self.process_id} has exited critical section.")
