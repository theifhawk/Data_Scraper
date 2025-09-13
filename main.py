import requests
from bs4 import BeautifulSoup

def main():
    print("hello world")


def scrape():
    url = "https://onepiece.fandom.com/wiki/Episode_Guide/East_Blue_Saga"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tags = soup.find_all('table', class_="collapsible collapsed")
    episodes = []
    for tag in tags:
        episodes.append(tag)
        
    
    for episode in episodes:
        print(episode)



if __name__ == "__main__":
    scrape()