import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import missingno as msno
from sklearn.impute import SimpleImputer, KNNImputer
from importData import *

def cleanDataFill(dataFrame, condition = 0, fill = 0):
    #Fill is set to 0 if you want to set another numerical value then you can specifiy it in the parameters 
    #If the condition is set to 0 then it will replace N/A values with a 0
    #If the condition is set to 1 then it will drop the rows with ALL N/A values
    if (condition == 0):
        df_cleaned = dataFrame.fillna(fill)
    elif(condition == 1):
        df_cleaned = dataFrame.dropna(how='all')
    
    return df_cleaned

def cleanDataDrop(dataFrame, condition = 0):
    #If the condition is set to 0 then it will drop the rows with ALL N/A values
    #If the condition is set to 1 then it will drop the rows with ANY N/A values
    if (condition == 0):
        df_cleaned = dataFrame.dropna(how='all')
    elif(condition == 1):
        df_cleaned = dataFrame.dropna()
    
    return df_cleaned

def cleanDataImpute(dataframe):
    dataframe = dataframe.replace(0, np.nan)
    imputer = SimpleImputer(strategy='mean')
    transformed_vals = imputer.fit_transform(dataframe)
    
    return transformed_vals

def cleanKNNImputer(dataframe, k=2):
    dataframe = dataframe.replace(0, np.nan)
    imp = KNNImputer(n_neighbors = 2)
    imputed_df = imp.fit_transform(dataframe)

    return imputed_df