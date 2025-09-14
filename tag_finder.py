
import re


def find_a(episodes):
    episode_titles = []
    # For each table, find the A tag
    for episode in episodes:
        if episode:
            for row in episode.find_all('tr'):
                for cell in row.find_all(['td', 'th']):
                    target_tag = cell.find('a')
                    if target_tag:
                        # print(f"Found tag: {target_tag.name} with text: {target_tag.get_text()}")
                        episode_titles.append(target_tag.get_text())
    print(len(episode_titles))
    for title in episode_titles:
        print(title)

def find_background_color(episodes):
    colors = []
    for episode in episodes:
        if episode:
            tag = episode.find('th')
            style = tag.get('style')
            match = re.search(r'background\s*:\s*([^;]+)', style)
            if match:
                background_color = match.group(1).strip()
                colors.append(background_color)
    print(len(colors))

def find_ep_number(episodes):
    for episode in episodes:
        if episode:
            tag_td = episode.find_all('td')
            print()
            print("ep num is:", tag_td[0].get_text())
            print("air date is:", tag_td[1].get_text())

            tag_a = episode.find_all('a')
            print("Eng Title: ", tag_a[0].get_text())

            tag_th = episode.find('th')
            contents = tag_th.contents
            print("Jap Title: ", contents[2])


        

            