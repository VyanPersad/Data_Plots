import pandas as pd
import numpy as np
import html5lib

#You may need to install 
#   openpyxl
#   lxml
#   beautifulsoup4 via pip 

filepath = 'IR Study Data V5.xlsx'
url = 'https://en.wikipedia.org/wiki/2020_Summer_Olympics'
match_term = ''

def read_from_file(filepath, test=0, n=5, col_Names = [], sheetName = None):
    filetype = filepath.split('.')[1]
    #This will read the csv and display the first 5 rows of the data.
    if (filetype == 'csv'):
        if (col_Names == []):
            dataFrame = pd.read_csv(filepath)
            #dataFrame = pd.read_csv(filepath, sep=';')
            #In the abobve line we tell pytohn to use the ; as the spearator.
            if (test == 0):
                print('Set test to 1 to view sample datraframes, Default is the first 5 rows, set n to vary the number of rows.')
            elif (test == 1):
                print(dataFrame.head(n))
        elif (col_Names != []):
            dataFrame = pd.read_csv(filepath, names=col_Names)
            #dataFrame = pd.read_csv(filepath, sep=';')
            #In the abobve line we tell pytohn to use the ; as the spearator.
            if (test == 0):
                print('Set test to 1 to view sample datraframes, Default is the first 5 rows, set n to vary the number of rows.')
            elif (test == 1):
                print(dataFrame.head(n))

        return dataFrame

    elif (filetype == 'xlsx'):
        if (sheetName == None):
            xlFile = pd.ExcelFile(filepath)  
            sheetName = xlFile.sheet_names[0]
            dataFrame = xlFile.parse(f'{sheetName}')
            if (test == 0):
                print('Set test to 1 to view sample datraframes, Default is the first 5 rows, set n to vary the numbe rof rows.')
            elif (test == 1):
                print(dataFrame.head(n))
            
            return dataFrame
 
def simple_scraper(url, n=5, test = 0, table_Num = 0, match_term = None):
    #If the url has multiple tables then set the table_Num to get that table
    #The dafault is set to 0 which will display the first one.
    if (match_term == None):
        dataFrame_list = pd.read_html(url)
        dataFrame = dataFrame_list[table_Num]
        if (test == 0):
            print('Set test to 1 to view sample datraframes, Default is the first 5 rows, set n to vary the number of rows.')
        elif (test == 1):
            print(dataFrame.head(n))
    else:
        dataFrame_list = pd.read_html(url, match=f'{match_term}')
        dataFrame = dataFrame_list[table_Num]
        if (test == 0):
            print('Set test to 1 to view sample datraframes, Default is the first 5 rows, set n to vary the number of rows.')
        elif (test == 1):
            print(dataFrame.head(n))
    
    return dataFrame

def write_to_csv(dataFrame, file_name):
    return dataFrame.to_csv(f'{file_name}.csv')
