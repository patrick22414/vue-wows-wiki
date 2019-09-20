import re
from os import path, environ, makedirs
from typing import IO

from unidecode import unidecode

__all__ = [
    "ROOT_URL",
    "HOME_URL",
    "log",
    "open_cache",
    "open_data",
    "set_proxy",
    "get_ship_html_name",
]

ROOT_URL = "http://wiki.wargaming.net"
HOME_URL = "http://wiki.wargaming.net/en/World_of_Warships"


def log(verb, *args):
    verb = f"{verb:12}:"
    print(verb, *args)


def _open(filename: str, mode: str) -> IO:
    # Enforcing UTF-8
    if "b" in mode:
        encoding = None
    else:
        encoding = "utf-8"

    # Enforcing LF line ending
    if "w" in mode:
        newline = "\n"
    else:
        newline = None

    return open(filename, mode, encoding=encoding, newline=newline)


def open_cache(filename: str, *, mode: str) -> IO:
    """Open a file in the cache folder"""
    ext = path.splitext(filename)[1][1:]
    folder = path.join("cache", ext)

    if not path.exists(folder):
        makedirs(folder)

    filename = path.join(folder, filename)

    log("Opening", filename)

    return _open(filename, mode)


def open_data(*args, mode: str) -> IO:
    folder = "data"

    if not path.exists(folder):
        makedirs(folder)

    filename = "data-" + "-".join(args) + ".json"
    filename = path.join(folder, filename)

    log("Opening", filename)

    return _open(filename, mode)


def set_proxy():
    environ["http_proxy"] = "http://127.0.0.1:1080"
    environ["https_proxy"] = "http://127.0.0.1:1080"


def get_ship_html_name(name: str) -> str:
    name = unidecode(name).lower()
    name = re.sub(r"[^0-9a-zA-Z]+", "_", name)

    return "ship-" + name + ".html"
