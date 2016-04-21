from bs4 import BeautifulSoup
import urllib2, sys


# Usage:
#   subreddit = the name of the subreddit you wish to scrape data from
#       e.g. "funny", "programming", etc..
def scrape_reddit(subreddit):
    hdrs = { 'User-Agent': 'Small project bot by /u/kodyk' }
    url = ("https://www.reddit.com/r/%s" % subreddit)
    request = urllib2.Request(url, headers=hdrs)
    html = BeautifulSoup(urllib2.urlopen(request).read(), "lxml")
    posts = [
        {
            "title": entry.find("a", "title").string.encode('ascii', 'ignore'),
            "user_posted": entry.find("a", "author").string.encode('ascii', 'ignore'),
            "number_of_upvotes":
                int(entry.parent.find("div", "score").string)
                if entry.parent.find("div", "score").string != u'\u2022'
                else 0,
            "url":
                entry.find("a", "title")['href']
                if entry.find("a", "title")['href'].startswith("/r/") == False
                else "https://reddit.com%s" % entry.find("a", "title")['href'],
            "base_url": entry.find("span", "domain").a["href"].replace("/domain/", "https://")
        } for entry in sorted(
            html.find_all("div", "entry"),
            key=lambda post: int(post.parent.find("div", "score").string)
                if post.parent.find("div", "score").string != u'\u2022'
                else 0,
            reverse=True)
        ]
    return posts

if __name__ == '__main__':
    if len(sys.argv) == 2:
        print scrape_reddit(sys.argv[1])




