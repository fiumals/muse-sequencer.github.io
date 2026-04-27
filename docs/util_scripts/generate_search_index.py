#!/bin/python
from bs4 import BeautifulSoup # html parser
import os
import json

directory = './'
indexedFiles = []

if not os.path.exists(directory + 'contents.html'):
    print("contents.html not found in current working directory")
    exit(1)

contentsFile = open(directory + 'contents.html', 'r')
contentsHtml = contentsFile.read()
contentsFile.close()

contentsSoup = BeautifulSoup(contentsHtml, 'html.parser')

for link in contentsSoup.select('.articlelink'):
    filename = str(link['href'])

    if filename.endswith(".html"):
        print("indexing: " + filename)

        f = open(directory + filename, 'r')
        html = f.read()
        f.close()

        soup = BeautifulSoup(html, 'html.parser')
        title = "undefined title"
        url = filename
        content = "undefined content"


        h1Element = soup.select_one('h1');
        mainDiv = soup.select_one('#main');

        if mainDiv is None:
            print("no main div, skipping " + filename)
            continue

        # default to the first h1 element to get the title of the page else fall back to first title element 

        if h1Element is not None:
            title = h1Element.get_text()
        else:
            titleElement = soup.select_one('title')
            title = titleElement.get_text() if titleElement is not None else "undefined title"


        content = mainDiv.get_text(separator=" ", strip=True)

        indexedFiles.append({
            'title': title,
            'url': url,
            'content': content
        })

jsonFile = open('search_index.json', 'w')
json.dump(indexedFiles, jsonFile, indent = 2)
jsonFile.close()

