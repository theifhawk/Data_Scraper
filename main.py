import requests
from bs4 import BeautifulSoup

def main():
    print("hello world")


def scrape():
    url = "https://archidekt.com/decks/6122714/sand_in_my_eyes"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    #title = soup.select_one('h1').text
    #text = soup.select_one('p').text
    #link = soup.select_one('a').get('href')
    #print(title)
    #print(text)
    #print(link)
    print(soup)

    #for link in soup.find_all('a'):
        #print(link.get('href'))


if __name__ == "__main__":
    scrape()