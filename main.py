import requests
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
    
    episode_titles = []
    # For each table, find the A tag
    for episode in episodes:
        print("\n")
        if episode:
            for row in episode.find_all('tr'):
                for cell in row.find_all(['td', 'th']):
                    target_tag = cell.find('a')
                    if target_tag:
                        # print(f"Found tag: {target_tag.name} with text: {target_tag.get_text()}")
                        episode_titles.append(target_tag.get_text())

    print(episode_titles)



if __name__ == "__main__":
    scrape()