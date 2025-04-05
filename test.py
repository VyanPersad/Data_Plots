from importData import *
from dataExploration import *

filepath = 'dataSets\\testDate.csv'

df = read_from_file(filepath, sheet=1)
df = df.head(10)
print(countVals(df,'SKU','20302D'))

