import os
import csv
from urllib.request import urlretrieve
from weibo_scraper import get_weibo_tweets_by_name
from utils import *

os.mkdir('./endorsements')
os.mkdir('./variety')
os.mkdir('./drama')

with open('vlinkage.csv', 'w', newline='') as csvfile:
	csvwriter = csv.writer(csvfile) 
	fields = ['date', 'data_type', 'post_url', 'pic_url']
	csvwriter.writerow(fields)

	for w in get_weibo_tweets_by_name('Vlinkage'):
		blog_body = w['mblog']['text']
		if '肖战' in blog_body and 'original_pic' in w['mblog']:
			data_type = ''
			if '寻艺品牌星指数' in blog_body:
				data_type = 'endorsements'
			elif '综艺嘉宾' in blog_body:
				data_type = 'variety'
			elif '电视剧演员' in blog_body:
				data_type = 'drama'
			post_url = w['scheme']
			pic_url = w['mblog']['original_pic']
			date = w['mblog']['created_at']
			dt = date_to_datetime(date)
			dt_str = datetime_to_string(dt)
			csv_row = [dt_str, data_type, post_url, pic_url]
			print('retrieving:', dt_str)
			pic_file_path = './' + data_type + '/' + dt_str.replace('/', '_') + '_' + data_type + '_' + 'vlinkage.jpg'
			urlretrieve(pic_url, pic_file_path)
			csvwriter.writerow(csv_row)
			if dt < stop_datetime:
				"breaking"
				break



