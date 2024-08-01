from importData import *
import html5lib

url ='https://en.wikipedia.org/wiki/2024_Summer_Olympics_medal_table'

df = simple_scraper(url=url, test=1, table_Num=3)

#write_to_csv(df, 'test')