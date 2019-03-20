import os
import platform
import sys
import time
from datetime import datetime
from pytz import timezone

"""
Simple proof of concept python application
"""


def looper():
    """
    Simple proof of concept function.
    Loops indefinitely, prints to stdout and writes to file.
    :return:
    """
    while True:
        string = (f"Hello var1:{os.getenv('VAR1')} var2:{os.getenv('VAR2')} var3:{os.getenv('VAR3')}! "
                  f"the time now is {datetime.now(tz=timezone('Europe/Athens'))} "
                  f"and I am going to sleep for 1 second.")
        print(string)

        with open("/data/out.txt", "a") as f:
            f.write(string + '\n')
            f.flush()

        time.sleep(1)


if __name__ == "__main__":
    print(f"python: {platform.python_version()} "
          f"now: {datetime.now(tz=timezone('Europe/Athens')).strftime('%Y-%m-%dT%H:%M:%S')}")
    sys.exit(looper())
