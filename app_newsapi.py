import os
from newsapi import NewsApiClient
print(os.environ.get('API_NEWS_KEY'))
import requests


# Init
newsapi = NewsApiClient(api_key=os.environ.get('API_NEWS_KEY'))

# country/category + sources are mutually exlusive
"""
(q='bitcoin',
sources='bbc-news,the-verge',
category='business',
language='en',
country='us')
"""


# EMPTY RESULT
# /v2/top-headlines
# top_headlines = newsapi.get_top_headlines(q='bitcoin',
#                                           sources='bbc-news,the-verge',
#                                           language='en')
# print(top_headlines)



# SUCCESS
# Requests library...
# https://newsapi.org/v2/top-headlines?country=us&apiKey=<value>
url='https://newsapi.org/v2/top-headlines?country=us&apiKey=' + os.environ.get('NEWS_API_KEY')
response = requests.get(url)
print(response.content)


# FAILS
# /v2/everything
# all_articles = newsapi.get_everything(q='bitcoin',
#                                       sources='bbc-news,the-verge',
#                                       domains='bbc.co.uk,techcrunch.com',
#                                       from_param='2018-12-01',
#                                       to='2017-12-12',
#                                       language='en',
#                                       sort_by='relevancy',
#                                       page=2)
# print(all_articles)

# /v2/sources
# sources = newsapi.get_sources()
# print(sources)