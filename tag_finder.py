
def find_a(table):
    episode_titles = []
    # For each table, find the A tag
    for episode in table:
        if episode:
            for row in episode.find_all('tr'):
                for cell in row.find_all(['td', 'th']):
                    target_tag = cell.find('a')
                    if target_tag:
                        # print(f"Found tag: {target_tag.name} with text: {target_tag.get_text()}")
                        episode_titles.append(target_tag.get_text())

    for title in episode_titles:
        print(title)