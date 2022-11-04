"""
Created on 2022-11-04 14:38
@author: johannes
"""
import os
import time
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).parent.parent


def load_env():
    load_dotenv(BASE_DIR.joinpath('.env'))


def get_username():
    return os.getenv('SPOTIFY_USER_NAME')


def func_timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args,  **kwargs)
        print(f'Timer for {func.__name__}:--%.5f sec'
              f'' % (time.time() - start_time))
        return result
    return wrapper
