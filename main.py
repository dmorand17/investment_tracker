
import os
from pathlib import Path
import shutil
import argparse
import datetime

import requests
from bs4 import BeautifulSoup
import pyfiglet

def parse_args():
    parser = argparse.ArgumentParser(description='This script will generate a file based on a template and csv file')
    parser.add_argument('-v','--verbose', help='Enable verbose logging', action='store_true')
    parser.add_argument('-i', '--input', help='input file containing mapping to be used in template', required=True, action='store')
    parser.add_argument('--template-dir', help='template directory to find templates', default='templates', action='store')
    parser.add_argument('-t', '--templates', help='template filename', required=True, action='store', nargs='+')
    return parser.parse_args()



"""
Execution Script
"""
custom_fig = pyfiglet.Figlet(font='graffiti')
if __name__ == '__main__':
    print(custom_fig.renderText("Investment Tracker"))
