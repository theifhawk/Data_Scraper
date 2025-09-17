import requests
import tag_finder
from bs4 import BeautifulSoup
import pandas as pd


def scrape():
    url = "https://onepiece.fandom.com/wiki/Episode_Guide/East_Blue_Saga"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tags = soup.find_all('table', class_="collapsible collapsed")
    episodes = []
    for tag in tags:
        episodes.append(tag)
    tag_finder.find_info(episodes)
    return(tag_finder.find_info(episodes))

def main():
    OP_table = ['Episode Number', 'English Title' , 'Japanese Title', 'Release Date', 'Color']
    OP_data = scrape()
    df = pd.DataFrame(columns = OP_table)
    for row in OP_data:
        length = len(df)
        df.loc[length] = row
    
    print(df)

if __name__ == "__main__":
    main()