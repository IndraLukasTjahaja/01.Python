# Resource: https://www.kaggle.com/rtatman/careercon-intro-to-apis

import numpy as np
import pandas as pd
import requests
from flashtext.keyword import KeywordProcessor
from nltk.corpus import stopwords

# let's read in a couple of forum posts
forum_posts = pd.read_csv("../input/ForumMessages.csv")

# get a smaller sub-set for playing around with
sample_posts = forum_posts.Message[0:3]

# get data from list of top 5000 pypi packages (last 30 days)
url = 'https://hugovk.github.io/top-pypi-packages/top-pypi-packages-30-days.json'
data = requests.get(url).json()

# get just the list of package names
list_of_packages = [data_item['project'] for data_item in data['rows']]

# create a KeywordProcess
keyword_processor = KeywordProcessor()
keyword_processor.add_keywords_from_list(list_of_packages)

# remove english stopwords
keyword_processor.remove_keywords_from_list(stopwords.words('english'))

# remove custom stopwords
keyword_processor.remove_keywords_from_list(['http','kaggle'])

# test our keyword processor
for post in sample_posts:
    keywords_found = keyword_processor.extract_keywords(post, span_info=True)
    print(keywords_found)