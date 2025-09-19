import requests
import tag_finder
import op_eps
from bs4 import BeautifulSoup
import pandas as pd

east_blue = "https://onepiece.fandom.com/wiki/Episode_Guide/East_Blue_Saga" # good
arabasta = "https://onepiece.fandom.com/wiki/Episode_Guide/Arabasta_Saga" # good
sky_island = "https://onepiece.fandom.com/wiki/Episode_Guide/Sky_Island_Saga" # good
water_7 = "https://onepiece.fandom.com/wiki/Episode_Guide/Water_7_Saga" # good
thriller_bark = "https://onepiece.fandom.com/wiki/Episode_Guide/Thriller_Bark_Saga" # good 
summit_war = "https://onepiece.fandom.com/wiki/Episode_Guide/Summit_War_Saga" # good
fishman = "https://onepiece.fandom.com/wiki/Episode_Guide/Fish-Man_Island_Saga" # good
dressrosa = "https://onepiece.fandom.com/wiki/Episode_Guide/Dressrosa_Saga" # good
whole_cake = "https://onepiece.fandom.com/wiki/Episode_Guide/Whole_Cake_Island_Saga" # good
wano = "https://onepiece.fandom.com/wiki/Episode_Guide/Wano_Country_Saga" # good
final = "https://onepiece.fandom.com/wiki/Episode_Guide/Final_Saga"

def scrape():
    url = "https://onepiece.fandom.com/wiki/Episode_Guide/Final_Saga"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tags = soup.find_all('table', class_="collapsible collapsed")
    episodes = []
    for tag in tags:
        episodes.append(tag)
    tag_finder.find_info(episodes)
    return(tag_finder.find_info(episodes))

def op_scrape():
    episodes_url = op_eps.together()
    episodes = []

    for url in episodes_url:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        tags = soup.find_all('table', class_="collapsible collapsed")
        for tag in tags:
            episodes.append(tag)

    
    all = tag_finder.find_info(episodes)

    print(all)


def main():
    OP_table = ['Episode Number', 'English Title' , 'Japanese Title', 'Release Date', 'Color']
    OP_data = scrape()
    df = pd.DataFrame(columns = OP_table)
    for row in OP_data:
        length = len(df)
        df.loc[length] = row
    #df.to_csv('output.csv', index=False)
    print(df)

if __name__ == "__main__":
    main()