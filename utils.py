import datetime

stop_datetime = datetime.date(2020, 1, 31)

month_abrvs = {'Jan': 1, 
			   'Feb': 2, 
			   'Mar': 3, 
			   'Apr': 4, 
			   'May': 5, 
			   'Jun': 6, 
			   'Jul': 7, 
			   'Aug': 8, 
			   'Sep': 9, 
			   'Oct': 10, 
			   'Nov': 11, 
			   'Dec': 12
			  }

def date_to_datetime(date):
	#['Wed', 'Mar', '24', '00:03:03', '+0800', '2021']
	split = date.split(' ')
	month, day, year = split[1], split[2], split[-1]
	month = month_abrvs[month]
	return datetime.date(int(year), month, int(day))

def datetime_to_string(datetime):
	return datetime.strftime('%Y/%m/%d')

	
