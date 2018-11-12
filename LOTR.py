## Josh Blaz -- LOTR

import nltk
import re
import urllib.request
import lxml.html as lh
import io
import requests

# NOTE: Elvish text is translated awkwardly into .txt format
# IE: 
# ►M MPR -F+MTRX MP ft PPtK P&RMPht: P. t. The last Two runes are the initials of Thror and Thrain.

# Import The Fellowship of the Ring
url = "https://archive.org/stream/TheLordOfTheRing1TheFellowshipOfTheRing/The+Lord+Of+The+Ring+1-The+Fellowship+Of+The+Ring_djvu.txt"
r = requests.get(url)
root = lh.parse(io.BytesIO(r.content)).getroot()
pre = root.xpath('//pre') # Access Silm text within the tree
#print(len(xp))           # Make sure this is the correct element
book = pre[0]             # Silm HTML object
Fellowship_Full = book.text  # Full Silmarillion text
## Split into chapters

# Import The Two Towers
url = "https://archive.org/stream/TheLordOfTheRingsTheTwoTowerByJ.r.r.Tolkien/the%20lord%20of%20the%20rings%20the%20two%20tower%20by%20j.r.r.%20tolkien_djvu.txt"
r = requests.get(url)
root = lh.parse(io.BytesIO(r.content)).getroot()
pre = root.xpath('//pre') # Access Silm text within the tree
#print(len(xp))           # Make sure this is the correct element
book = pre[0]             # Silm HTML object
Towers_Full = book.text  # Full Silmarillion text
## Split into chapters

# Import The Return of the King
url = "https://archive.org/stream/TheLordOfTheRing1TheFellowshipOfTheRing/The%20Return%20Of%20The%20King_djvu.txt"
r = requests.get(url)
root = lh.parse(io.BytesIO(r.content)).getroot()
pre = root.xpath('//pre') # Access Silm text within the tree
#print(len(xp))           # Make sure this is the correct element
book = pre[0]             # Silm HTML object
King_Full = book.text  # Full Silmarillion text
## Split into chapters


# Import Silmarillion
url = "https://archive.org/stream/fegmcfeggerson_gmail_4731/473%20%281%29_djvu.txt"
r = requests.get(url)
root = lh.parse(io.BytesIO(r.content)).getroot()
pre = root.xpath('//pre') # Access Silm text within the tree
#print(len(xp))           # Make sure this is the correct element
book = pre[0]             # Silm HTML object
Silmarillion_Full = book.text  # Full Silmarillion text
## Split into chapters

# Import The Hobbit
url = "https://archive.org/stream/TheHobbitByJ.R.RTolkien/The%20Hobbit%20by%20J.R.R%20Tolkien_djvu.txt"
r = requests.get(url)
root = lh.parse(io.BytesIO(r.content)).getroot()
pre = root.xpath('//pre') # Access Silm text within the tree
#print(len(xp))           # Make sure this is the correct element
book = pre[0]             # Silm HTML object
Hobbit_Full = book.text  # Full Silmarillion text
## Split into chapters


### GOAL: split all books into chapters -> Run Sentiment Analysis and Topic Modeling
###      --> Use Sentiment140 API for sentiment analysis
### Overlay topic modeling over the sentiment analysis of each chapter