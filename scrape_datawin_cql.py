import os
import csv
from urllib.request import urlretrieve
from weibo_scraper import get_weibo_tweets_by_name
from utils import *

#os.mkdir('./cql_datawin')

with open('cql_datawin.csv', 'w', newline='') as csvfile:
	csvwriter = csv.writer(csvfile) 
	fields = ['date', 'post_url', 'pic_url']
	csvwriter.writerow(fields)

	for w in get_weibo_tweets_by_name('德塔文影视观察'):
		blog_body = w['mblog']['text']
		if '陈情令' in blog_body and '电视剧景气指数' in blog_body and 'original_pic' in w['mblog']:
			post_url = w['scheme']
			pic_url = w['mblog']['original_pic']
			date = w['mblog']['created_at']
			dt = date_to_datetime(date)
			dt_str = datetime_to_string(dt)
			csv_row = [dt_str, post_url, pic_url]
			print('retrieving:', dt_str)
			pic_file_path = './cql_datawin/' + dt_str.replace('/', '_') + '_' + 'datawin.jpg'
			urlretrieve(pic_url, pic_file_path)
			csvwriter.writerow(csv_row)
			