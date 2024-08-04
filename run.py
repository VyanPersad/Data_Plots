from importData import *
import html5lib

url ='https://en.wikipedia.org/wiki/2024_Summer_Olympics_medal_table'

df = simple_scraper(url=url, test=1, table_Num=3)

write_to_csv(df, destpath='dataSets', file_name='test')

df2 = read_from_file('dataSets\sales1.xlsx')
print(df2)
#write_to_csv(df2, destpath='dataSets', file_name='test')
df2.to_csv('dataSets\test.csv')