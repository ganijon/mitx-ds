from bs4 import BeautifulSoup
import requests
import sys, os

# def main():
# '''
# Build a dictionary of MIT faculty member names with their abstracts
# '''

# Build a list of names of faculty from MIT EEC website
faculty_names = list()

r = requests.get("https://www.eecs.mit.edu/people/faculty-advisors")

soup = BeautifulSoup(r.text, 'html.parser')

div_people_list = soup.find_all("div", class_="people-list")[0]
div_title_list = div_people_list.find_all("div", class_="views-field views-field-title")
for div in div_title_list:
    if div.span.a:
        faculty_names.append(div.span.a.contents[0])

# Build a dictionary of author's abstract links from arXiv.org
arxiv_query_url = "https://arxiv.org/search/?query={0}&searchtype=author&abstracts=show&order=-announced_date_first&size=100"
file = sys.argv[0]
pathname = os.path.dirname(file)
abspathname = os.path.abspath(pathname)

for full_name in faculty_names:
    r = requests.get(arxiv_query_url.format(full_name.replace(" ", "+")))
    soup = BeautifulSoup(r.text, "html.parser")
    spans_abstract = soup.find_all("span", class_="abstract-full has-text-grey-dark mathjax")
    for span in spans_abstract:
        id = span['id'][:-16].replace("/", "")
        output_fileName =  abspathname + '\\abstracts\\' + id + '.txt'
        output_file = open(output_fileName, 'w+', encoding='utf-16')
        content = span.contents[0].strip(' \'\"\t\r\n')
        output_file.write(content)