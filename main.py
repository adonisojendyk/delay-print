import time
import sys

def delay_print(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.25)

def ddelay_print(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.5)


delay_print("hello world\n")

ddelay_print("World Hello")
