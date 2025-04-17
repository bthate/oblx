# This file is placed in the Public Domain.


"clients"


import threading


from .handler import Handler


lock = threading.RLock()


class Client(Handler):

    def __init__(self):
        Handler.__init__(self)
        Fleet.add(self)

    def announce(self, txt) -> None:
        pass

    def raw(self, txt) -> None:
        raise NotImplementedError("raw")

    def say(self, channel, txt) -> None:
        self.raw(txt)


class Fleet:

    clients = {}

    @staticmethod
    def add(clt) -> None:
        Fleet.clients[repr(clt)] = clt

    @staticmethod
    def all() -> []:
        yield from Fleet.clients.values()

    @staticmethod
    def announce(txt) -> None:
        for clt in Fleet.clients.values():
            clt.announce(txt)

    @staticmethod
    def display(evt) -> None:
        with lock:
            for tme in sorted(evt.result):
                Fleet.say(evt.orig, evt.channel, evt.result[tme])
            evt.ready()

    @staticmethod
    def first() -> None:
        clt =  list(Fleet.clients.values())
        res = None
        if clt:
            res = clt[0]
        return res

    @staticmethod
    def get(orig) -> None:
        return Fleet.clients.get(orig, None)

    @staticmethod
    def say(orig, channel, txt) -> None:
        clt = Fleet.get(orig)
        if clt:
            clt.say(channel, txt)

    @staticmethod
    def wait() -> None:
        for clt in Fleet.clients.values():
            if "wait" in dir(clt):
                clt.wait()


"utilities"

def elapsed(seconds, short=True) -> str:
    txt = ""
    nsec = float(seconds)
    if nsec < 1:
        return f"{nsec:.2f}s"
    yea = 365*24*60*60
    week = 7*24*60*60
    nday = 24*60*60
    hour = 60*60
    minute = 60
    yeas = int(nsec/yea)
    nsec -= yeas*yea
    weeks = int(nsec/week)
    nsec -= weeks*week
    nrdays = int(nsec/nday)
    nsec -= nrdays*nday
    hours = int(nsec/hour)
    nsec -= hours*hour
    minutes = int(nsec/minute)
    nsec -= int(minute*minutes)
    sec = int(nsec)
    if yeas:
        txt += f"{yeas}y"
    if weeks:
        nrdays += weeks * 7
    if nrdays:
        txt += f"{nrdays}d"
    if short and txt:
        return txt.strip()
    if hours:
        txt += f"{hours}h"
    if minutes:
        txt += f"{minutes}m"
    if sec:
        txt += f"{sec}s"
    txt = txt.strip()
    return txt


def spl(txt) -> str:
    try:
        result = txt.split(',')
    except (TypeError, ValueError):
        result = txt
    return [x for x in result if x]


"interface"


def __dir__():
    return (
        'Client',
        'Fleet',
        'elapsed',
        'spl'
    )
