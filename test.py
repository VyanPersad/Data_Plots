import cv2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import missingno as msno
import seaborn as sns
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn import datasets
from importData import *

filepath = 'dataSets\\sales1.xlsx'

df = read_from_file(filepath, sheet=1)
#df = df.head(10)
print(df)

