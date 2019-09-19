import json

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

from common import *


def convert_nation_name(full_name: str) -> str:
    return "".join(c for c in full_name if c.isalpha()).lower()


def fetch_homepage_html(use_cache=True):
    if use_cache:
        try:
            with open_cache("homepage.html", mode="r") as fo:
                log("Skipping", "Use cache for home page")
                return
        except FileNotFoundError:
            pass

    log("Fetching", HOME_URL)
    resp = requests.get(HOME_URL)

    if resp.ok:
        soup = BeautifulSoup(resp.content, "html.parser")
        html = soup.prettify()

        with open_cache("homepage.html", mode="w") as fo:
            log("Writing", repr(html[:15]))
            fo.write(html)


def make_data_nations():
    with open_cache("homepage.html", mode="r") as fo:
        soup = BeautifulSoup(fo.read(), "html.parser")

    # This is currently the only way to find the nations table
    nations_table: Tag = soup.find("table", style="width: 100%")

    full_names = list(nations_table.stripped_strings)

    names = [
        convert_nation_name(fn) for fn in full_names
    ]

    urls = [
        ROOT_URL + nations_table.find("a", title=full_name).get("href")
        for full_name in full_names
    ]

    data_nations = [
        {"name": n, "full_name": fn, "url": u}
        for n, fn, u in zip(names, full_names, urls)
    ]

    with open_data("nations", mode="w") as fo:
        json.dump(data_nations, fo, indent=4)


if __name__ == '__main__':
    try:
        fetch_homepage_html()
    except requests.ConnectionError as e:
        log("Error", "ConnectionError, retrying with proxy")
        set_proxy()
        fetch_homepage_html()

    make_data_nations()
