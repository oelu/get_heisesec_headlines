#!/usr/local/bin/python2.7
"""Usage: get_heise_sec_headline.py

   Options:
        -h, --help  print help message
"""
__author__ = 'olivier'

# import statements
from docopt import docopt
from lxml import html
import requests
from pprint import pprint


def get_lxml_tree(endpoint):
    """
    gets website lxml tree
    """
    response = requests.get(endpoint)
    data = response.text
    tree = html.fromstring(data)
    return tree


def get_heise_sec_headlines(tree):
    """
    gets heise security headlines
    """
    headlines = tree.xpath('//*[@id="mitte_links"]/div/div/div/section/header/h3/a/text()')
    return headlines


def main():
    """
    main function
    """
    # gets arguments from docopt
    arguments = docopt(__doc__)
    print arguments
    endpoint = 'http://www.heise.de/security/'
    tree = get_lxml_tree(endpoint)
    headlines = get_heise_sec_headlines(tree)
    for headline in headlines:
        print headline


if __name__ == "__main__":
    main()
