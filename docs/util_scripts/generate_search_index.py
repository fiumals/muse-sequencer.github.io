#!/bin/python
from bs4 import BeautifulSoup # html parser
import os
import json
import sys

# this script generates the search index for the search functionality, it gets the text contents from all .articlelink elements in a contents.html file
# run this from the script from the same directory as the contents.html file or pass that directory as the first argument

directory = sys.argv[1] if len(sys.argv) > 1 else './'
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
        title = link.get_text() or "undefined title"
        url = filename
        content = "undefined content"

        mainDiv = soup.select_one('#main');

        if mainDiv is None:
            print("no main div, skipping " + filename)
            continue

        # default to the first h1 element to get the title of the page else fall back to first title element 

        content = mainDiv.get_text(separator=" ", strip=True)

        indexedFiles.append({
            'title': title,
            'url': url,
            'content': content
        })

jsonFile = open(directory + 'search_index.json', 'w')
json.dump(indexedFiles, jsonFile, indent = 2)
jsonFile.close()

