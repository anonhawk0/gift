import subprocess
import sys
import time

FILE_TO_RUN = "350.py"

while True:
    print("Starting worker...")
    process = subprocess.Popen([sys.executable, FILE_TO_RUN])

    # Wait until the process exits
    process.wait()

    print("Worker stopped. Restarting in 2 seconds...")
    time.sleep(10)

