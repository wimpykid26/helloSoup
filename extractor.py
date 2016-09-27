from bs4 import BeautifulSoup
import requests
import urllib
import os


def link_extractor(url):
	count = 1
	r = requests.get(url)
	soup = BeautifulSoup(r.content)
	link = soup.find_all('img')
	for link2 in link:
		fullLink = link2.get('src')
		count = count + 1
		downloader2("http://www.jiit.ac.in/" + fullLink, count)

def downloader2(imageUrl2,count2):
	savePath = "image" + str(count2)
	fullfilename = os.path.join('/home/dwaipayan/Downloads', savePath)
	urllib.urlretrieve(imageUrl2, fullfilename)

if  __name__=="__main__":
	link_extractor("http://www.jiit.ac.in/gallery")
