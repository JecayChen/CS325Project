import requests
from bs4 import BeautifulSoup

class Webscraper:
    def __init__(self, url):
        self.url = url.strip()
    
#checks url connection response
#return true if successful
#return false if unsuccessful
    def testURL(self):
        try:
            response = requests.get(self.url) #attempts connection
        
            if response.status_code == 200: #connection successful
                print(f"Connection Successful: {self.url}")
                return True
            else: #connection unsuccessful
                print(f"Connection Unsuccessful: {self.url}")
                print(f"Error Code: {response.status_code}")
                return False

        except requests.exceptions.RequestException as e: #connection error
            print(f"Error in accessing {self.url}: {e}")
            return False

    #scrape webpage for article titles
    #returns a string array of titles
    def scrapeTitles(self):
        if self.testURL(): #restURL successful
            url = self.url
            try: #try-catch for errors in retrieving titles
                response = requests.get(url)
                soup = BeautifulSoup(response.content, 'html.parser')
                titles = []
                MIN_LENGTH = 50

                #scrapes the html for article title links that are at least a certain length long
                for links in soup.find_all('a', href=True): #searches for all <a href> links
                    text = links.get_text(strip=True) #get the raw text for each link
                    if text and len(text) >= MIN_LENGTH: #if the raw text exists and is over minimum characters
                        titles.append(text) #add if to the title list
                return titles
            
            except Exception as e:
                print(f"Error in scrapeTitles: {e}")
                return []
        else:
            print(f"Error in connection. Unable to perform scrapeTitles")
            return []
