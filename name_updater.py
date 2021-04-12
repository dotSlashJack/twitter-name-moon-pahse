#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
update twitter name with emoji of current moon phase
@author: jack hester
"""
import tweepy
from datetime import datetime, timedelta, date
import moon_phase

consumer_key = ""
consumer_secret = ""
access_token = "c"
access_token_secret = ""
  
# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  
# set access to user's access key and access secret
auth.set_access_token(access_token, access_token_secret)
  
# calling the api
api = tweepy.API(auth)

def get_emoji():
    phase = moon_phase.get_phase()
    if phase == "New":
        return "🌑"
    elif phase == "Full":
        return "🌕"
    elif phase == "First Quarter":
        return "🌓"
    elif phase == "Last Quarter":
        return "🌗"
    elif phase == "Waxing Crescent":
        return "🌒"
    elif phase == "Waning Crescent":
        return "🌘"
    elif phase == "Waxing Gibbous":
        return "🌔"
    elif phase == "Waning Gibbous":
        return "🌖"
    else:
        return " "

base_twitter_name = "Jack" #TODO: might be useful to get this automatically, then add moon phase to it

name_with_phase = base_twitter_name + " " + get_emoji()

api.update_profile(name=name_with_phase)

print("Your twitter name was updated with the moon's phase")
