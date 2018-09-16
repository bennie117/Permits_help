
# coding: utf-8

# In[3]:

# stuff to import
get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd
import numpy as np
import statsmodels.api as sm
import pylab as pl
from sklearn import datasets
from sklearn import metrics


# In[4]:

# read in the file, dtype tells us the type to use for the data
# I have used this file from NYC open data because i can work with it on my computer,
# the other file, that you emailed me, does not load on my computer (possibly because it contains microsoft characters?)
filename = 'DOB_Permit_Issuance.csv'
update = pd.read_csv(filename, header = 0, dtype=str)


# In[9]:

pd.read_csv('DOB_Permit_Issuance (11/11).csv',header = 0, dtype=str)


# In[209]:

# here is the data, the NaN's come from the fact that the csv file does not have a value in those fields
update


# In[210]:

# here are the headers for the data,
list(update.columns.values)


# In[211]:

# count the most common Permitee's First and Last name, the dropna drops an NaN's that it finds
#first_names = update["Permittee's First Name"].dropna()
#last_names = update["Permittee's Last Name"].dropna()
permittees = update.loc[:,"Permittee's First Name": "Permittee's License #"].dropna()


# In[212]:

# here's a print of the first names
permittees


# In[213]:

# here we count the most frequently used permittee. We consider the n most frequent permittees.
n = 20;
licence_num_counts = permittees["Permittee's License #"].value_counts()[0:n];

# note that it contains a field with no licence string, remove it with the isalnum property of string:
most_freq_licence_nums = [ licence_num for licence_num in licence_num_counts.index[:] if licence_num.isalnum()]

# now get the most frequent permittees
most_freq_permittees = permittees[permittees["Permittee's License #"].isin(most_freq_licence_nums)]



# In[214]:

# here we give a frequency plot of the most frequent permittees,
# this is plots licence number against frequency. Will try to change to name vs frequency.
# can include more permittee's by increasing n above
licence_num_counts.plot(kind='bar')


# In[ ]:



