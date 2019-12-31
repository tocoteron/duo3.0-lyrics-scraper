# coding: utf-8
import requests
from bs4 import BeautifulSoup

base_url = 'http://www.hosono.com/duo3.0/'

for section_num in range(1, 46):
    section_url = base_url + 'section{:02d}.html'.format(section_num)
    response = requests.get(section_url)
    response.encoding = 'shift_jis'
    soup = BeautifulSoup(response.text, "html.parser")

    print("Section {}".format(section_num))
    print()

    for p in soup.select("#text1 p")[1:-1]:
        english_expression = p.contents[0]
        japanese_expression = p.contents[2]
        print(english_expression)
        print(japanese_expression)
        print()