# Project Gutenberg Scraper

A Python script to scrape Chinese books from [Project Gutenberg](https://www.gutenberg.org), an extensive online library of free eBooks. This project demonstrates basic web scraping techniques using the `requests` and `BeautifulSoup` libraries.

## Project Structure
```
.
├── gutenberg.py
├── project_gutenberg/
│   └── [scraped text files]
├── requirements.txt
```

## Installing
   ```bash
   pip install -r requirements.txt
   ```
- `requests==2.32.3` - For sending HTTP requests to the website.
- `BeautifulSoup==4.12.3` - For parsing and navigating HTML content.

## Coding style
Follow PEP8 unless explicitly specified otherwise

## Deployment
   ```bash
   python gutenberg.py
   ```
The script will start scraping Chinese books from Project Gutenberg and save the results as a `.txt` file in the `project_gutenberg` folder.

## Demo
[![Project Gutenberg - 網頁爬蟲練習](https://img.youtube.com/vi/_mD591UNjw8/0.jpg)](https://www.youtube.com/watch?v=_mD591UNjw8)


## Versioning
- Python 3.10

## Authors
[solano66](https://github.com/solano66)

## Acknowledgments
Thank you to all the people who release code on GitHub.
