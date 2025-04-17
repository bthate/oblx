# This file is placed in the Public Domain.


"uptime"


import time


from ..client import elapsed
from ..thread import STARTTIME


def upt(event):
    event.reply(elapsed(time.time()-STARTTIME))
