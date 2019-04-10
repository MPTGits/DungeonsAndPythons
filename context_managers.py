# from contextlib import contextmanager
# import time

from contextlib import ContextDecorator
from contextlib import contextmanager
from time import sleep, time
import datetime

@contextmanager
def performance(filename):
    with open(filename, 'w') as f:
        start = time()
        yield 
        end = time()
        result = end - start
        x = datetime.datetime.now()
        f.write(str(x))
        f.write(' ')
        f.write(str(result))

def go():
    # Using the Class...
    with performance('log_file.txt'):
        print("sleeping for 2...")
        sleep(2)
go()
go()