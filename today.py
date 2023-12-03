# today.txt is 13.1
  
# 13.2
file = open("today.txt", "r")
today_string = file.read()
print(today_string)
file.close()

#13.3
import time
fmt = "%b %d %Y"
time.strptime(today_string, fmt)

#15.1
import multiprocessing
from datetime import datetime
import random

def cur_time():
    time.sleep(random.uniform(0,1))
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)

if __name__ == "__main__":
    for n in range(3):
        p = multiprocessing.Process(target=cur_time())
           # args =("Completed at", cur_time()) )
        p.start()

   
