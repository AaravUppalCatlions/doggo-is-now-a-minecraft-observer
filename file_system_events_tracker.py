import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "D:\Downloads"

# Event Hanlder Class
class FileEventHandler(FileSystemEventHandler):

    #1_on_created
    def on_created(self, event):
        print(f"A dreadnought" + {event.src_path} + "has been summoned into this realm")
    #2_on_deleted
    def on_deleted(self, event):
        print(f"The leader" + {event.src_path} + "has been oblibarated by a kulfi")
    #3_on_modified
    def on_modified(self, event):
        print(f"The dreadnut " + {event.src_path} + "is now upgraded to the next tier")
    #4_on_moved
    def on_moved(self, event):
        print(f"A hecker" + {event.src_path} + "used $sudo teleport to reach" + {event.dest_path})

        


# Initialize Event Handler Class
event_handler = FileEventHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()


#5_Write a exception for keyboardInterrupt
try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped")      
    observer.stop() 







