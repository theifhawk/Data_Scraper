
import re

def find_info(episodes):
    for episode in episodes:
        if episode:
            tag_td = episode.find_all('td')
            tag_a = episode.find_all('a')
            tag_th = episode.find('th')
            contents = tag_th.contents
            style_attr = tag_th['style']

            style_dict = dict(
                item.strip().split(':', 1)
                for item in style_attr.split(';')
                    if ':' in item
                )
            background_value = style_dict.get('background')

            print()
            print(background_value)
            print("ep num is:", tag_td[0].get_text())
            print("air date is:", tag_td[1].get_text())
            print("Eng Title: ", tag_a[0].get_text())
            print("Jap Title: ", contents[2])


        

            