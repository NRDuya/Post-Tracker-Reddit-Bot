import os
import praw
import re
from os.path import join, dirname
from dotenv import load_dotenv
from config import*
from post import*

# RETRIEVE client_id and client_secret FROM .env
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
API_ID = os.environ.get("API_ID")
API_SECRET = os.environ.get("API_SECRET")

#CREATES REDDIT INSTANCE (READ ONLY)
reddit = praw.Reddit(client_id = API_ID,
            client_secret = API_SECRET,
            user_agent = 'post_tracker_bot by /u/mootetoo')

#CREATES SUBREDDIT WE WILL BE READING FROM
subreddit = reddit.subreddit('buildapcsales')

#MESSAGE FUNCTION THAT WILL SEND TEXT MESSAGE TO USER (GOOGLE VOICE?)
def message():
    print("send text message of links")

#FUNCTION TO CHECK THE PRICE OF THE PRODUCT IN THE POST TITLE
def isPrice(title):
    price = re.findall(r"(?:[\$]{1})([\d]+.?\d)", title)
    return float(price[0])

submissionsList = []

for submission in subreddit.rising(limit = numOfSearches):
    if (all(i in submission.title for i in keywords)):
        price = isPrice(submission.title)
        if (price <= maxPrice): 
            submissionsList.append(Post(submission.title, submission.url, price))

sortedSubmissions =  sorted(submissionsList, key=lambda x: x.price, reverse=False)

for i in sortedSubmissions:
    print(i.title)
    print(i.url)
    print(i.price)