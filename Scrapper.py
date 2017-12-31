# this file scraps the scores of every alliane in the matches in the 2017 FRC NECMP
# in the terminal

# install requests
# install bs4
# python

# in the python terminal
from bs4 import BeautifulSoup
import requests

# specify the url
url = "https://www.thebluealliance.com/event/2017necmp"
r = requests.get(url)

# get the html code of the site
soup = BeautifulSoup(r.content)
print(soup.prettify)

# find all the links
links = soup.find_all("a")

# returns all the links--neater
for link in links:
	print(link)

# returns all the href--neater
for link in links:
	print(link.get("href"))

# return the link text and the link itself
for link in links:
	print(link.text, link.get("href"))

# string substitution
for link in links:
    "<a href='%s'>%s</a>" %(link.get("href"),link.text)

# find all the red scores
r_data = soup.find_all("td",{"class" : "redScore"})
print(r_data)

#p rettify the list--easier to read
for item in r_data:
	print(item.text)

# find all the blue scores
b_data = soup.find_all("td",{"class" : "blueScore"})
print(b_data)

# prettify the list--easier to read
for item in b_data:
	print(item.text)

