import time
import os
import os.path
import sys

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
args = sys.argv

def watchdog(one, two, three):
    print('one:'+one+'two:'+two+'three:'+three)

if __name__ == '__main__':
    if len(args) == 4:
        watchdog(args[1], args[2], args[3])
    else:
        print('引数が足りません。')


