from importData import *
from dataExploration import *

filepath = 'dataSets\\BuyerSalesHistory.csv'

df = read_from_file(filepath, col_Names=['Sku', 'Description','Cash Price','Year'])
print(df.head(10))
df = df[df['Year'] == 'This Year']   
#dfSelect = df[['Sku', 'Description','Cash Price','Year']]
print(df.head(10))
