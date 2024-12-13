import requests
from bs4 import BeautifulSoup as bs
import re
import os

folderPath = 'project_gutenberg'
if not os.path.exists(folderPath):
    os.mkdir(folderPath)

url = 'https://www.gutenberg.org/browse/languages/zh'
res = requests.get(url)
soup = bs(res.text, "lxml")

list_posts = []
list_posts.clear()
count = 1

chinese_books = soup.select('div.pgdbbylanguage > ul > li.pgdbetext > a')

regex_no = r'/ebooks/(\d+)'
regex_chinese = r'^[\u4E00-\u9FFF]'

for book in chinese_books:
    match_chinese = re.match(regex_chinese, book.get_text())

    if not match_chinese:
        continue

    book_name = re.sub(r'[\s<>:"/\\|?*]', '',book.get_text())
    match_no = re.match(regex_no, book['href'])
    list_posts.append({
        'order': count,
        'ID': match_no.group(1),
        'title': book_name,
        'link': f'https://www.gutenberg.org/cache/epub/{match_no.group(1)}/pg{match_no.group(1)}-images.html'
    })
    count += 1

for index, obj in enumerate(list_posts):
    res_book = requests.get(obj['link'])
    soup_book = bs(res_book.text, "lxml")

    for garbage in soup_book.select('head'):
        garbage.decompose()
    for garbage in soup_book.select('section.pg-boilerplate.pgheader'):
        garbage.decompose()
    for garbage in soup_book.select('p#id00000'):
        garbage.decompose()

    txt = soup_book.get_text()

    with open(f'{folderPath}/{obj["order"]}_{obj["title"]}_{obj["ID"]}.txt', 'w', encoding='utf-8') as file:
        file.write(txt)
    
    print(f'已下載 {obj["order"]}_{obj["title"]}_{obj["ID"]}')

    
    
