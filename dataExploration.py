import cv2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import missingno as msno
import seaborn as sns
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn import datasets
from importData import *

def plotHistwBins(dataFrame, colName, binSize=None, title='None', xlabel='X-Axis', ylabel='Y-Axis', color='blue', label='Label'):
    if (binSize == None):
        plotData = dataFrame[f'{colName}']
        plotData = plotData.dropna()
        plt.hist(plotData, color=color, label=label)

    elif (binSize != None):        
        plotData = dataFrame[f'{colName}']
        bins = np.arange(plotData.min(), plotData.max(), binSize)
        plotData = plotData.dropna()
        plt.hist(plotData, bins=bins, color=color, label=label)
        
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.tight_layout()
    plt.show()

def boxPlotSimple(dataFrame,columns=None , by=None, title='None', xlabel='X-Axis', ylabel='Y-Axis', color='steelblue', label='Label'):
    dataFrame.boxplot(column=columns, by=by)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.tight_layout()
    plt.show()

def boxPlot(dataFrame, x=None , y=None, hue=None, title='None', xlabel='X-Axis', ylabel='Y-Axis', label='Label'):
    sns.boxplot(x=x, y=y, hue=hue, data=dataFrame)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.tight_layout()
    plt.show()

def scatterPlotSimple(dataFrame, X=None, Y=None, title='None', xlabel='X-Axis', ylabel='Y-Axis', color='steelblue', label='Label'):
    df = dataFrame.dropna()
    plt.scatter(x=df[X], y=df[Y])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.tight_layout()
    plt.show()

def scatterPlot(dataFrame, X=None, Y=None, hue=None, title='None', xlabel='X-Axis', ylabel='Y-Axis', color='steelblue', label='Label'):
    df = dataFrame.dropna()
    if (hue == None):
        plt.scatter(x=df[X], y=df[Y])
    elif (hue!= None):
        sns.scatterplot(x=X, y=Y, data=df, hue = hue)
    
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.tight_layout()
    plt.show()

def scatterPlotMatrix(dataFrame, colNames, label='Label'):
    df = pd.DataFrame(dataFrame.dropna(), columns=colNames)
    pd.plotting.scatter_matrix(df, marker='.')
    plt.legend()
    plt.tight_layout()
    plt.show()
    df = pd.DataFrame(dataFrame.dropna(), columns=colNames)
    pd.plotting.scatter_matrix(df, marker='.')
    plt.legend()
    plt.tight_layout()
    plt.show()

def barPlot(dataFrame, index = None, colNames = None, stacked=False, title='None', xlabel='X-Axis', ylabel='Y-Axis', width=10, height=5):
    #colnames is an array of the column names you wish to plot.
    df = dataFrame.dropna()
    df = df[colNames]
    df.set_index(index).plot.bar(rot=0, fontsize = 11, stacked=stacked, figsize=(width,height))
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(loc = (1.04,0.8))
    plt.tight_layout()
    plt.show()

def barPlotSimple(dataFrame, X=None, Y=None, hue=None, title='None', xlabel='X-Axis', ylabel='Y-Axis',width=10, height=5):
    df = dataFrame.dropna()
    sns.barplot(x=X, y=Y, data=df, hue = hue)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.tight_layout()
    plt.show()