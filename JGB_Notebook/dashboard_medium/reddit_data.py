import pandas as pd
import dateutil.relativedelta
from datetime import date
import datetime
import yfinance as yf
import numpy as np
import praw
import sqlite3
from config import r_cid, r_csec, r_uag
#return a dataframe for the newest reddit posts
def get_reddit(cid= r_cid, csec= r_csec, uag= r_uag, subreddit='wallstreetbets'):
   
    #connect to reddit
    reddit = praw.Reddit(client_id= cid, client_secret= csec, user_agent= uag)
#get the new reddit posts
    posts = reddit.subreddit(subreddit).new(limit=None)
#load the posts into a pandas dataframe
    p = []
    for post in posts:
        p.append([post.title, post.score, post.selftext])
    posts_df = pd.DataFrame(p,columns=['title', 'score', 'post'])
    
    return posts_df