from bs4 import BeautifulSoup
from urllib.request import urlopen

# Declare URL
url = 'https://en.wikipedia.org/wiki/Google'
title = url[30:]

# Get the HTML
raw_html = urlopen(url)
html = BeautifulSoup(raw_html, 'html5lib')

# Get the list of Headings
headline_list = html.findAll("span", {"class": "mw-headline"})
scraped_headings = [headline.text for headline in headline_list]

# Get the list of Paragraph Data
scraped_list = html.findAll("div", {"id": "mw-content-text"})[0].div.findAll("p")
scraped_data = [data.text for data in scraped_list]

# Write everything in file
with open('Saved_Data.txt', 'a') as file:
    file.write('\n\n' + title + '\n' + '='*50 + '\n')
    for i in scraped_headings:
        try:
            file.write(i+'\n')
        except Exception as e:
            print(e)

    file.write('\n\n\n')

    for i in scraped_data:
        try:
            file.write(i+'\n\n')
        except Exception as e:
            print(e)

    file.write('='*100 + '\n' + '='*100 + '\n')

print('Done!')
