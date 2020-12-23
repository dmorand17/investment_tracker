import os
import sys
import shutil
import argparse
import datetime

import requests
from bs4 import BeautifulSoup
import pyfiglet
import logging
import logging.config
import yaml
import json

import tracker
from core import Ticker

#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def parse_args():
    parser = argparse.ArgumentParser(description='DESCRIPTION')
    parser.add_argument('-v','--verbose', help='Enable verbose logging', action='count', default=0)
    parser.add_argument('-i', '--input', help='help description', action='store')
    return parser.parse_args()

def load_config(default_path, env_key):
    path = default_path
    cfg_key = os.getenv(env_key,None)
    if cfg_key:
        path = cfg_key
    if os.path.exists(path):
        with open(path) as f:
            try:
                app_cfg = yaml.safe_load(f)
            except Exception as e:
                print(e)
                sys.exit("Error in app configuration")
    else:
        sys.exit(f"app configuration [{path}] not found!")

    return app_cfg

def get_logger_config(default_path='conf/logger.yaml', env_key='INVEST_LOG_CFG'):
    config = load_config(default_path,env_key)
    return config

def get_app_config(default_path='conf/config.yaml', env_key='INVEST_CFG'):
    config = load_config(default_path,env_key)
    return config

def configure_logging():
    logging.config.dictConfig(get_logger_config())
    logger = logging.getLogger(__name__)

    log_level = {
        2: logging.DEBUG
        ,1: logging.INFO
        ,0: logging.CRITICAL
    }

    logger.setLevel(log_level[args.verbose])
    if logger.isEnabledFor(logging.DEBUG):
        logger.debug("testing isEnabled...")

    # Used for debugging yaml app_cpguration
    logger.debug(json.dumps(config,indent=2))
    return logger

"""
Execution Script
"""
#custom_fig = pyfiglet.Figlet(font='graffiti')
custom_fig = pyfiglet.Figlet(font='slant')
if __name__ == '__main__':
    args = parse_args()

    print(custom_fig.renderText("Investment Tracker"))

    config = get_app_config()
    logger = configure_logging()

    # Print out each top level key
    for cfg, item in config.items():
        print("{} : {}".format(cfg,item))
    
    # Print each stock
    print("\nStocks from config (as-is)")
    for stock in config.get("stocks"):
        print(stock)

    print()
    
    stocks = config.get("stocks")
    stocks.sort()
    print(stocks)

    # Print out tracker details
    trackers = config.get("trackers")
    print("type(trackers): {}".format(type(trackers)))
    for i,trkr in enumerate(trackers,start=1):
        print("tracker [{0}] -> {1}".format(i,trkr))
    
    # Print yahoo tracker details
    logger.debug(trackers.get("yahoo"))

    tracker = tracker.YahooTracker()
    """ Add stocks from config into tracker"""
    [tracker.add_ticker(Ticker(stock)) for stock in stocks]
