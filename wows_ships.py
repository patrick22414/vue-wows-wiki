import json

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

from common import *


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


def fetch_nation_html(use_cache=True):
    with open_data("nations", mode="r") as fo:
        data_nations = json.load(fo)

    for nation in data_nations:
        # Skip fetch if the cache exists
        if use_cache:
            try:
                with open_cache(nation["name"] + ".html", mode="r") as fo:
                    log("Skipping", "Use cache for", nation["full_name"])
                continue
            except FileNotFoundError:
                pass

        log("Fetching", nation["url"])
        resp = requests.get(nation["url"])

        if resp.ok:
            soup: Tag = BeautifulSoup(resp.content, "html.parser")
            html = soup.prettify()

            with open_cache(nation["name"] + ".html", mode="w") as fo:
                log("Writing", repr(html[:15]))
                fo.write(soup.prettify())


def make_data_ships():
    with open_data("nations", mode="r") as fo:
        data_nations = json.load(fo)

    for nation in data_nations:
        filename = nation["name"] + ".html"

        with open_cache(filename, mode="r") as fo:
            soup = BeautifulSoup(fo.read(), "html.parser")

        # Each type of ships are in a <div class="wot-frame-1">
        for ship_type_div in soup.select(".wot-frame-1"):
            # The ship type is specified in <h2><span>Ship Type</...>
            ship_type = next(ship_type_div.select("h2 span")[0].stripped_strings)
            log("Processing", nation["full_name"], ship_type)

            ship_type = convert_ship_type(ship_type)

            names = []
            urls = []

            # Each ship is in a <div class="tleft">
            for ship_div in ship_type_div.select(".tleft"):
                ship_a = ship_div.select("center a")[0]

                names.append(next(ship_a.stripped_strings))
                urls.append(ROOT_URL + ship_a.get("href"))

            with open_data("ships", nation["name"], ship_type, mode="w") as fo:
                data_ships = [
                    {"name": fn, "url": u} for fn, u in zip(names, urls)
                ]

                json.dump(data_ships, fo, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    set_proxy()
    fetch_nation_html(use_cache=False)

    make_data_ships()
