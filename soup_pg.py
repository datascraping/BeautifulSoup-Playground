from bs4 import BeautifulSoup

import sys
import requests

headers = { "User-Agent":"Mozilla 5.0" }

page = requests.get(sys.argv[1], headers=headers)
soup = BeautifulSoup(page.text, "lxml")
