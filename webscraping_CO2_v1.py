from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pd
import tweepy
import time

#twitter keys, from devoloper.twitter.com
CONSUMER_KEY = 'J8zaoLHtrRtl2Xb8dGodBby3O'
CONSUMER_SECRET = 'M7NRptFIQl1u0QPPMTsTGylT9IV5KNDHjI0qsBYdcCeSFiEETm'
ACCESS_KEY = '1118065183614734338-L6KOEFPOLji6iVG0vasRNhKF0G8Sb3'
ACCESS_SECRET = '4kAyQU60nzQRlJLcgLWK09R8PNTvvb1Rpdf6zIP1BH8rh'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#start of webscraping
myUrl = "https://www.esrl.noaa.gov/gmd/ccgg/trends/monthly.html"

uClient = uReq(myUrl)

page_html = uClient.read()

uClient.close()

page_soup = soup(page_html,"html.parser")

containers = page_soup.findAll('div',{"class":"colored_box seagreen text-right"})
table = containers[0]
#print(table.table.tr.td.text)
string=table.table.tr.get_text()
daily_CO2string = ("Den seneste måling fra Mauna Loa, Hawaii "+string)
print(daily_CO2string)
#daily_CO2string.replace('\xa0\xa0',', ')

#sending tweet
api.update_status(daily_CO2string)
