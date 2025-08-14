import os
import time
import datetime
import psutil

logfile = "test.txt"

while True:
    with open(logfile, "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        file.write(f"{timestamp} - CPU Usage: {cpu_usage}% - Memory Usage: {memory_info.percent}%\n")
    time.sleep(7)
    



