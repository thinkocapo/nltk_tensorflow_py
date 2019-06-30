
http://www.nltk.org/book/ch01.html

##### not inside virtualenv
#### inside virtualenv
```

```

## Setup
sudo apt-get install python-matplotlib (no virtualenv)
or
pip install python-matplotlib (virtualenv)
or it was:
pip install matplotlib (virtualenv)


#### tensortflow python3 env to support tensorflow:
```
virtualenv -p nltk_tensorflow_py_3
pip install -r requirements.txt
```
which installs tensorflow, nltk, matplotlib

#### Optional
- default location for datasets is ~/nltk_data
- sudo python -m nltk.downloader -d /usr/local/share/nltk_data all.
- nltk.org/data.html
- `python -m nltk.downloader all`

### Run (Tests) python v2?
```
# tests nltk and datasets are there
python3 app_nltk_test.py
['The', 'Fulton', 'Coutenty', 'Grand', 'Jury', 'said', ...]

# test analyzing them, opens a matplotlib for words over time in historical corpi:
source ~/virtualenvs/nltk_python which is v2....
python nltk.book.py

```

### Run -  For lots of different tests, kickstart with:
```
python
>>> from nltk.book import *
>>> from matplotlib import *
```

## TensorFlow
README.TensorFlow.md

## NewsApi
export NEWS_API_KEY=<key>
python app_newsapi.py
https://newsapi.org/docs/endpoints/top-headlines
client library newsapi-python returned empty results so use ^^
"We crawl and index news articles from over 30,000 news sources and blogs. We also monitor the top and breaking news headlines from the following 135 of the most notable of these sources." https://newsapi.org/sources


### Cool
Note

Important: You need to have Python's NumPy and Matplotlib packages installed in order to produce the graphical plots used in this book. Please see http://nltk.org/ for installation instructions.

Note

You can also plot the frequency of word usage through time using https://books.google.com/ngrams


https://eventregistry.org/

https://primer.ai/careers/

https://towardsdatascience.com/natural-language-processing-event-extraction-f20d634661d3




newsapi is only in the python v2 `nltk_python` virtualenv


https://realpython.com/python-requests/#the-get-request
https://github.com/mattlisiv/newsapi-python