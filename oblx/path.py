# This file is placed in the Public Domain.


"path utilities"


import datetime
import os
import pathlib


p = os.path.join


from .object import fqn


class Workdir:

    name = __file__.rsplit(os.sep, maxsplit=2)[-2]
    wdr  = ""


def long(name) -> str:
    split = name.split(".")[-1].lower()
    res = name
    for names in types():
        if split == names.split(".")[-1].lower():
            res = names
            break
    return res


def moddir():
    return p(Workdir.wdr, "mods")


def pidname(name) -> str:
    return p(Workdir.wdr, f"{name}.pid")


def skel() -> str:
    "basic directories"
    path = pathlib.Path(store())
    path.mkdir(parents=True, exist_ok=True)
    path = pathlib.Path(moddir())
    path.mkdir(parents=True, exist_ok=True)
    return path


def setwd(path):
    Workdir.wdr = path


def store(pth="") -> str:
    return p(Workdir.wdr, "store", pth)


def strip(pth, nmr=2) -> str:
    return os.sep.join(pth.split(os.sep)[-nmr:])


def types() -> [str]:
    return os.listdir(store())


def wdr(pth):
    return p(Workdir.wdr, pth)


def ident(obj) -> str:
    return p(fqn(obj),*str(datetime.datetime.now()).split())


def path(obj):
    return p(store(ident(obj)))


def __dir__():
    return (
        'Workdir',
        'ident',
        'long',
        'moddir',
        'path',
        'pidname',
        'skel',
        'store',
        'types',
        'wdr'
    )
