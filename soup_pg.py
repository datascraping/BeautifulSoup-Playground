from bs4 import BeautifulSoup

import sys
import requests

page = requests.get(sys.argv[1])
soup = BeautifulSoup(page.text, "lxml")
