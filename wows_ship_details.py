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
            try:
                # Open the data-ships-*-*.json file if found
                with open_data("ships", n, t, mode="r") as fo:
                    data_ships = json.load(fo)
            except FileNotFoundError:
                # Some nations may not some types of ship, such as U.S.S.R. CV
                continue

            for ship in data_ships:
                name = ship["name"]
                url = ship["url"]

                html_filename = get_ship_html_name(name)

                # Log something like "U.S.A. DD"
                log_prefix = f"{fn} {t.upper()}"

                # Skip fetch if the cache exists
                if use_cache:
                    try:
                        with open_cache(html_filename, mode="r") as fo:
                            log("Skipping", log_prefix, name)
                        continue
                    except FileNotFoundError:
                        pass

                log("Fetching", log_prefix, name)
                resp = requests.get(url)

                if resp.ok:
                    soup = BeautifulSoup(resp.content, "html.parser")

                    with open_cache(html_filename, mode="w") as fo:
                        fo.write(soup.prettify())


def build_ship_modules(soup: BeautifulSoup) -> Dict:
    modules = {
        "mainBattery": [],
        "hull"       : [],
        "torpedoes"  : [],
        "fireControl": [],
        "engine"     : [],
    }

    tables: List[Tag] = soup.select(".t-modules")

    for table in tables:
        title = table.find("a").get("href")
        table_rows: List[Tag] = table.select("tr")[1:]
        if title == "Main Battery":
            for tr in table_rows:
                entries = list(tr.stripped_strings)
                modules["mainBattery"].append({
                    "title"   : entries[0],
                    "turnTime": entries[2],
                    "heAlpha" : entries[4],
                    "apAlpha" : entries[6],
                })
        elif title == "Hull":
            for tr in table_rows:
                entries = list(tr.stripped_strings)
                modules["mainBattery"].append({
                    "title"    : entries[0],
                    "hitPoints": entries[1],
                })
        elif title == "Torpedoes":
            pass
        else:
            raise NotImplementedError

    return modules


def build_ship_upgrades():
    pass


def build_ship_consumables():
    pass


def parse_ship_detail(ship: Dict[str, str]):
    name = ship["name"]
    html_filename = get_ship_html_name(name)

    with open_cache(html_filename, mode="r") as fo:
        soup = BeautifulSoup(fo.read(), "html.parser")

    modules_table = soup.select(".t-modules")

    modules = {}
    for module_table in modules_table:
        a_title: Tag = module_table.find("a")
        module_tr = module_table.select("tr")[1:]

        module_type = a_title.get("title")
        module_variants = [
            next(mtr.find("td").stripped_strings) for mtr in module_tr
        ]

        modules[module_type] = module_variants

    print(modules)


def make_ship_details_data():
    for n, fn in zip(*list_nations()):
        for t in list_ship_types():
            try:
                # Open the data-ships-*-*.json file if found
                with open_data("ships", n, t, mode="r") as fo:
                    data_ships = json.load(fo)
            except FileNotFoundError:
                # Some nations may not some types of ship, such as U.S.S.R. CV
                continue

            for ship in data_ships:
                parse_ship_detail(ship)
                break


if __name__ == '__main__':
    make_ship_details_data()
