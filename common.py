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
    "convert_ship_type",
    "convert_ship_tier"
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


def convert_ship_type(s: str) -> str:
    if s == "Destroyers":
        return "dd"
    elif s == "Cruisers":
        return "cc"
    elif s == "Battleships":
        return "bb"
    elif s == "Aircraft Carriers":
        return "cv"
    elif s == "dd":
        return "Destroyers"
    elif s == "cc":
        return "Cruisers"
    elif s == "bb":
        return "Battleships"
    elif s == "cv":
        return "Aircraft Carriers"
    else:
        raise ValueError(f"Ship type not found: {s}")


def convert_ship_tier(roman: str) -> int:
    if roman == "I":
        return 1
    elif roman == "II":
        return 2
    elif roman == "III":
        return 3
    elif roman == "IV":
        return 4
    elif roman == "V":
        return 5
    elif roman == "VI":
        return 6
    elif roman == "VII":
        return 7
    elif roman == "VIII":
        return 8
    elif roman == "IX":
        return 9
    elif roman == "X":
        return 10
    else:
        return -1
