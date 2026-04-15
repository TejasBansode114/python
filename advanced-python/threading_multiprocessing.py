import threading
import time

def task(name):
    print(f"Starting task {name}")
    time.sleep(2)
    print(f"Finished task {name}")
    
# Creating two "workers"
t1=threading.Thread(target=task, args=("Task-1",))
t2=threading.Thread(target=task, args=("Task-2",))

#.start(): This tells the thread to begin its work in the background.
t1.start()
t2.start()
#.join(): This tells the main thread to wait for the thread to finish before proceeding.
t1.join()
t2.join()
