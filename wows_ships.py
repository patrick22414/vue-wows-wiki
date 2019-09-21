import json

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

from common import *


def fetch_nation_html(use_cache=True):
    with open_data("nations", mode="r") as fo:
        data_nations = json.load(fo)

    for nation in data_nations:
        # Skip fetch if the cache exists
        if use_cache:
            try:
                with open_cache(nation["name"] + ".html", mode="r") as fo:
                    log("Skipping", "Use cache for", nation["fullName"])
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
            # The ship type is specified in a "h2 span"
            ship_type = next(ship_type_div.h2.span.stripped_strings)
            log("Processing", nation["fullName"], ship_type)

            ship_type = convert_ship_type(ship_type)

            names = []
            urls = []
            tiers = []

            # Each ship is in a <div class="tleft">
            for ship_div in ship_type_div.select(".tleft"):
                # Ship name and url are in a "center a"
                ship_center_a: Tag = ship_div.center.a
                name = next(ship_center_a.stripped_strings)
                url = ROOT_URL + ship_center_a.get("href")

                # Ship tier is in a "center span b", in Roman numerals
                tier = next(ship_div.center.span.b.stripped_strings)
                tier = convert_ship_tier(tier)

                names.append(name)
                urls.append(url)
                tiers.append(tier)

            with open_data("ships", nation["name"], ship_type, mode="w") as fo:
                data_ships = [
                    {"name": fn, "tier": t, "url": u}
                    for fn, u, t in zip(names, urls, tiers)
                ]

                json.dump(data_ships, fo, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    set_proxy()
    fetch_nation_html()

    make_data_ships()
