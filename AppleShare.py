#Time Series data Analysis
#import the library pandas for data analysis
import pandas as pd

#import the library matplotlib for plotting on a graph
import matplotlib.pyplot as plt

#import the CSV file to read data from and save into dataframe df
df = pd.read_csv('apple.csv', index_col='Date', parse_dates=True)

#Create a new Column in dataframe called Change to compute the change in price per day
df['Change']= (df['Open'] - df['Close'])/df['Close']*100

#Edit the dataframe to remove unwanted columns
df = df[['Close','Adj Close', 'Change']]

#To sort the dataframe by index (Date)
df = df.sort_index()

#Prints the info about dataframe, like starting index, ending index and etc
#print(df.info())

#To print the first 5 elements of the dataframe
#print(df.head())

#Prints the mean of 'Adj Close' from Feb 2013 
#print(df.loc['2013-Feb', 'Adj Close'].mean())

#Prints the mean of 'Adj Close' between Feb 2013 and Feb 2014 
print(df.loc['2013-Feb':'2014-Feb', 'Adj Close'].mean())

#Prints the mean of the monthly closing value for the dataframe
print(df.resample('M')['Close'].mean())

#Prints the mean of 'Change' per week for the dataframe
print(df.resample('W')['Change'].mean())

#We define an element sample to store Adj CLose data from Feb 2012 to Feb 2014
sample = df.loc['2012-Feb':'2014-Feb', ['Adj Close']]

#We plot sample values
sample.plot()

#Prints the plotted graph
plt.show()
