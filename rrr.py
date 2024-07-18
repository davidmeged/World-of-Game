import time
import sys

# הדפסת שורה
print("This line will be deleted in 3 seconds...", end='', flush=True)
time.sleep(3)

sys.stdout.write('\r' + ' ' * len("This line will be deleted in 3 seconds...") + '\r')
sys.stdout.flush()