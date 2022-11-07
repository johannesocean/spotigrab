"""
Created on 2022-11-04 14:38
@author: johannes
"""
import time


def func_timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args,  **kwargs)
        print(f'Timer for {func.__name__}:--%.5f sec'
              f'' % (time.time() - start_time))
        return result
    return wrapper
