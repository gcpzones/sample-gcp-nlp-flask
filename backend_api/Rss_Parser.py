import feedparser as feedparser

#NewsFeed = feedparser.parse("https://www.bundesbank.de/service/rss/en/633312/feed.rss")
#NewsFeed = feedparser.parse("https://jpmorganchaseco.gcs-web.com/rss/news-releases.xml")
NewsFeed = feedparser.parse("https://www.hsbc.com/rss-feed")

print('Number of RSS posts :', len(NewsFeed.entries))

i = 1

while i < len(NewsFeed.entries):
    entry = NewsFeed.entries[i]
    print(entry.published)
    print(entry.title_detail)
    print(entry.summary_detail)
    print(entry.link)
    i += 1

