"""
Created on 2022-11-07 09:47
@author: johannes
"""
import os
from pathlib import Path
from dotenv import load_dotenv
from routes import *
from src import *

BASE_DIR = Path(__file__).parent.parent


def load_env():
    load_dotenv(BASE_DIR.joinpath('.env'))


def get_db_path():
    return os.getenv('SPOTIGRAB_DATABASE')


def get_spotify_username():
    return os.getenv('SPOTIFY_USER_NAME')
