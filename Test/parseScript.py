from bs4 import BeautifulSoup
import requests

page_link = 'http://www.youtube.com'

page_response = requests.get(page_link, timeout=5)

page_content = BeautifulSoup(page_response.content, "html.parser")

soup = BeautifulSoup(page_link)
soup.findAll()

#textContent = []
#for i in range(0, 20):
#    paragraphs = page_content.find_all("src")[i].text
#    textContent.append(paragraphs)
    
#print(len(textContent))