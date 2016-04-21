# subreddit-scraper
A simple bot for scraping the "hot" page from a subreddit.

This is a short tool I have written in Python for practice. This is also the first web-scraping bot I have ever written.

## Usage
```python
subreddit = "programming"
data = scrape_reddit(subreddit)
```

- subreddit = name of the subreddit you want to scrape.
  - e.g. subreddit = "programming"
  - will end up scraping https://reddit.com/r/programming
- scrape_reddit() will return an array of data objects, each containing:
  - title = title of post
  - user_posted = name of user the post belongs to
  - number_of_upvotes = number of upvotes
  - url = URL when clicking the title of the post
  - base_url = Domain of url

## Dependencies
Subreddit-scraper requires bs4 (BeautifulSoup) to be installed within your python environment.

To install BeautifulSoup, run this code in your terminal:
```
pip install bs4
```

## Standalone Runtime
Subreddit-scraper can be ran as a stand-alone program.

To run as a single program, specify the subreddit name as a parameter when running from the terminal:
```
python subreddit_scraper.py [name-of-subreddit]
```
