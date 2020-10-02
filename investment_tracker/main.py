import os
from pathlib import Path
import shutil
import argparse
import datetime

import requests
from bs4 import BeautifulSoup
import pyfiglet
import logging
import yaml
import json

#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Create logger
logging.basicConfig()
logger = logging.getLogger(__name__)

def parse_args():
    parser = argparse.ArgumentParser(description='DESCRIPTION')
    parser.add_argument('-v','--verbose', help='Enable verbose logging', action='count', default=0)
    parser.add_argument('-i', '--input', help='help description', action='store')
    return parser.parse_args()

def get_config(cfg):
    return config.get(cfg)

"""
Execution Script
"""
#custom_fig = pyfiglet.Figlet(font='graffiti')
custom_fig = pyfiglet.Figlet(font='slant')
if __name__ == '__main__':
    args = pargs_args()

    print(custom_fig.renderText("Investment Tracker"))

    cur_dir = Path(os.getcwd())
    config_file = cur_dir / "config.yaml"

    log_level = {
        2: logging.DEBUG
        ,1: logging.INFO
        ,0: logging.CRITICAL

    logger.setLevel(log_level[args.verbose])
    if logger.isEnabledFor(logging.INFO):
        logger.info("testing")

    with open(config_file) as yaml_file:
        config = yaml.full_load(yaml_file)

    # Used for debugging yaml configuration
    print('Json output')
    print(json.dumps(config,indent=2))
    logger.debug(json.dumps(config,indent=2))
    print()

    # Print out each top level key
    for cfg, item in config.items():
        print("{} : {}".format(cfg,item))

    # Print each stock
    print("\nStocks from config (as-is)")
    for stock in config.get("stocks"):
        print(stock)

    print()

    stocks = get_config("stocks")
    stocks.sort()
    print(stocks)

    # Print out tracker details
    trackers = get_config("trackers")
    print("type(trackers): {}".format(type(trackers)))
    for i,tracker in enumerate(trackers,start=1):
        print("tracker [{0}] -> {1}".format(i,tracker))
