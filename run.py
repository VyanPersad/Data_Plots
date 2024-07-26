from importData import *
import html5lib

url ='https://en.wikipedia.org/wiki/List_of_Formula_One_World_Constructors%27_Champions'

df = simple_scraper(url=url, table_Num=2)


write_to_csv(df, 'test')