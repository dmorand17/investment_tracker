import os
import sys
import shutil
import argparse
import datetime

import requests
from bs4 import BeautifulSoup
import pyfiglet
import logging
import yaml
import json
from investment_logger import InvestmentLogger

#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Create logger for testing
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%Y-%m-%d %I:%M:%S')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)

logger.addHandler(handler)
# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')


def parse_args():
    parser = argparse.ArgumentParser(description='DESCRIPTION')
    parser.add_argument('-v','--verbose', help='Enable verbose logging', action='count', default=0)
    parser.add_argument('-i', '--input', help='help description', action='store')
    return parser.parse_args()

def get_yaml_app_cpg(default_path, env_key):
    path = default_path
    cfg_key = os.getenv(env_key,None)
    if cfg_key:
        path = cfg_key
    if os.path.exists(path):
        with open(path) as f:
            try:
                app_cpg = yaml.safe_load(f)
            except Exception as e:
                print(e)
                sys.exit("Error in app_cpguration")
    else:
        sys.exit(f"app_cpguration [{path}] not found!")

    return app_cpg

def get_logger_config(default_path='conf/logger.yaml', env_key='INVEST_LOG_CFG'):
    config = get_yaml_app_cpg(default_path,env_key)
    return config

def get_app_config(default_path='conf/config.yaml', env_key='INVEST_CFG'):
    config = get_yaml_app_cpg(default_path,env_key)
    return config
"""
Execution Script
"""
#custom_fig = pyfiglet.Figlet(font='graffiti')
custom_fig = pyfiglet.Figlet(font='slant')
if __name__ == '__main__':
    args = parse_args()
    
    print(custom_fig.renderText("Investment Tracker"))

    config = get_app_config()
    log_cfg = get_logger_config()

    logger.debug(log_cfg)
    logger = InvestmentLogger.getInstance(log_cfg).getLogger('dev')

    log_level = {
        2: logging.DEBUG
        ,1: logging.INFO
        ,0: logging.CRITICAL
    }

    logger.setLevel(log_level[args.verbose])
    if logger.isEnabledFor(logging.DEBUG):
        logger.info("testing isEnabled")

    # Used for debugging yaml app_cpguration
    logger.debug(json.dumps(config,indent=2))

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
    for i,tracker in enumerate(trackers,start=1):
        print("tracker [{0}] -> {1}".format(i,tracker))
    
    # Print yahoo tracker details
    logger.debug(trackers.get("yahoo"))
