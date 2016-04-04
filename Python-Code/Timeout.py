#!/usr/bin/env python

import sys
import signal

class Timeout:
    def __init__(self, seconds, error_message='Timeout'):
        self.seconds = seconds
        self.error_message = error_message
    def handle_timeout(self, signum, frame):
        raise TimeoutError(self.error_message)
    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.setitimer(signal.ITIMER_REAL, self.seconds)
    def __exit__(self, type, value, traceback):
        signal.setitimer(signal.ITIMER_REAL,0)

class TimeoutError(Exception):
    def __init__(self, arg):
        self.msg = arg



def timed_function(seconds,func,*args,**kwargs):
        try:
            with Timeout(seconds):
                func(*args,**kwargs)
            return True
        except TimeoutError:
            return False
    



if __name__ == "__main__":
  
  import time
  print timed_function(.001,time.sleep,.003)


