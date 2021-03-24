# xz_weibo_data_scrape
Scraping data &amp; images associated with 肖战 from Weibo accounts Vlinkage and Datawin

# Vlinkage
* `variety` contains Vlinkage charts for 'Variety Show Guests'
* `drama` contains Vlinkage charts for 'TV Drama Actors'
* `endorsements` contains Vlinkage charts for endorsements
* `vlinkage.csv` contains the fields `[date, data_type, post_url, pic_url]`
* note that Vlinkage charts only go up to June 2020, not because there's no data beyond that, but due to Weibo API limitations.

# Datawin
* `datawin` contains Datawin charts for 'Drama Popularity'
* `datawin.csv` contains the fields `[date, post_url, pic_url]`
* should be complete for the time range March 24 2021 - January 2020
