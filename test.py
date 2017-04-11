import sys
import time
times = 0
while times < 10:
    m = '>'
    sys.stdout.write(m)
    sys.stdout.flush()
    time.sleep(1)
    times += 1
