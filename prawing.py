#!/usr/bin/env python

import praw

r = praw.Reddit('Trying out praw to help fittit by u/thambi69 ')

sub = r.get_subreddit('fitness')
for submission in sub.get_hot(limit=10):
    if 'Moronic Monday' in submission.title:
        print submission.selftext
