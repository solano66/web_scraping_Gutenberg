import os
import re
import requests
from bs4 import BeautifulSoup as bs

# 檢查儲存資料的資料夾是否存在
folder_path = 'project_gutenberg'
if not os.path.exists(folder_path):
    os.mkdir(folder_path)

# 設定目標網址
url = 'https://www.gutenberg.org/browse/languages/zh'
response = requests.get(url)
soup = bs(response.text, "lxml")

# 初始化變數
list_posts = []
count = 1

# 選取中文書籍的連結
chinese_books = soup.select('div.pgdbbylanguage > ul > li.pgdbetext > a')

regex_no = r'/ebooks/(\d+)'
regex_chinese = r'^[\u4E00-\u9FFF]'

for book in chinese_books:
    # 檢查是否為純中文書
    match_chinese = re.match(regex_chinese, book.get_text())

    if not match_chinese:
        continue
    
    # 去除無法命名的符號
    book_name = re.sub(r'[\s<>:"/\\|?*]', '', book.get_text())
    # 取得書本編號
    match_no = re.match(regex_no, book['href'])

    # 建立 list
    list_posts.append({
        'order': count,
        'ID': match_no.group(1),
        'title': book_name,
        'link': f'https://www.gutenberg.org/cache/epub/{match_no.group(1)}/pg{match_no.group(1)}-images.html'
    })
    count += 1

# 下載每本書的內容
for obj in list_posts:
    res_book = requests.get(obj['link'])
    soup_book = bs(res_book.text, "lxml")

    # 移除多餘的 HTML 元素
    for garbage in soup_book.select('head, section.pg-boilerplate.pgheader, p#id00000'):
        garbage.decompose()

    # 提取純文本
    txt = soup_book.get_text()

    # 儲存為 .txt 檔案
    file_name = f'{folder_path}/{obj["order"]}_{obj["title"]}_{obj["ID"]}.txt'
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(txt)

    print(f'已下載 {obj["order"]}_{obj["title"]}_{obj["ID"]}')