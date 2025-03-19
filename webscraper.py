import requests
from bs4 import BeautifulSoup

class Webscraper:
    def __init__(self, url):
        self.url = url
    
#checks url connection response
def testURL(self):
    response = requests.get(self.url)
    
    if(response == 200):
        return True