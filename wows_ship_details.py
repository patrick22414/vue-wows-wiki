import json
from typing import List, Tuple, Dict

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

from common import *


def list_nations() -> Tuple[List[str], List[str]]:
    with open_data("nations", mode="r") as fo:
        data_nations = json.load(fo)

    names = [nation["name"] for nation in data_nations]
    full_names = [nation["full_name"] for nation in data_nations]

    return names, full_names


def list_ship_types() -> List[str]:
    return ["dd", "cc", "bb", "cv"]


def fetch_ship_html(use_cache=True):
    for n, fn in zip(*list_nations()):
        for t in list_ship_types():
            with open_data("ships", n, t, mode="r") as fo:
                data_ships = json.load(fo)

            for ship in data_ships:
                name = ship["name"]
                url = ship["url"]

                html_filename = get_ship_html_name(name)

                # Log something like "U.S.A. DD"
                log_tag = f"{fn} {t.upper()}"

                # Skip fetch if the cache exists
                if use_cache:
                    try:
                        with open_cache(html_filename, mode="r") as fo:
                            log("Skipping", log_tag, name)
                        continue
                    except FileNotFoundError:
                        pass

                log("Fetching", log_tag, name)
                resp = requests.get(url)

                if resp.ok:
                    soup: Tag = BeautifulSoup(resp.content, "html.parser")

                    with open_cache(html_filename, mode="w") as fo:
                        fo.write(soup.prettify())


def parse_ship_detail(ship: Dict[str, str]):
    name = ship["name"]
    html_filename = get_ship_html_name(name)

    with open_cache(html_filename, mode="r") as fo:
        soup = BeautifulSoup(fo.read(), "html.parser")

    switcher_divs = soup.select(".topStockSwitcher")

    print(len(switcher_divs))


if __name__ == '__main__':
    parse_ship_detail({"name": "Worcester"})
