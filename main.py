import requests
import tag_finder
from bs4 import BeautifulSoup

def main():
    print("hello world")


def scrape():
    url = "https://onepiece.fandom.com/wiki/Episode_Guide/East_Blue_Saga"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tags = soup.find_all('table', class_="collapsible collapsed")
    # These will be the tables
    episodes = []
    for tag in tags:
        episodes.append(tag)
    
    #tag_finder.find_a(episodes)
    #tag_finder.find_background_color(episodes)
    tag_finder.find_ep_number(episodes)



if __name__ == "__main__":
    scrape()