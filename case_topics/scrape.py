from bs4 import BeautifulSoup
import re

input_file = "arxiv.html"
with open(input_file) as fp:
    soup = BeautifulSoup(fp)

tags = soup.find_all("span", attrs={"class": ["abstract-full"]})
for tag in tags:
    id = tag['id'][:-16]
    output_fileName = 'abstracts\\' + id + '.txt'
    output_file = open(output_fileName, 'w')
    output_file.write(tag.contents[0].strip(' \'\"\t\r\n'))
