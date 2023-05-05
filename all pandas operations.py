# -*- coding: utf-8 -*-
""" Here We will get a brief insight on all these basic operations which can be performed on Pandas Series :
    1)Creating a Series
    2)Accessing element of Series
    3)Indexing and Selecting Data in Series
    4)Binary operation on Series
    5)Conversion Operation on Series

Original file is located at
    https://colab.research.google.com/drive/1xY4yPVsNLDiIXu6lz9bOGFFuWLiEQH5w
"""

# import pandas as pd
import pandas as pd
 
# list of strings
lst = ['Hi', 'This', 'is', 'Khadeer', 'from', 'kadapa']
 
# Calling DataFrame constructor on list
df = pd.DataFrame(lst)
print(df)

import pandas as pd
 
# Define a dictionary containing employee data
data = {'Name':['khadeer', 'Princi', 'bunty', 'Andrea'],'Qualification':['B.tech', 'M.tech', 'MCA', 'MBA']}
 
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)
 
# select two columns
print(df[['Name', 'Qualification']])

# Import pandas package
import pandas as pd

# Define a dictionary containing employee data
data = {'Name':['khadeer', 'Princy', 'Bunty', 'Andrea'],
		'Age':[27, 24, 22, 32],
		'Address':['AndhraPradesh', 'Baghdad', 'Dhaka', 'Canberra'],
		'Qualification':['Msc', 'MA', 'MCA', 'Phd']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)

# select all rows
# and second to fourth column
df[df.columns[0:4]]

import numpy as np

# create a dictionary of numpy arrays
my_dict = {'A': np.array([1, 2, 3]), 'B': np.array([4, 5, 6]), 'C': np.array([7, 8, 9])}

# select column 'B' from the dictionary
selected_col = my_dict['B']

# print the selected column
print(selected_col)

import numpy as np

# create a dictionary of numpy arrays
my_dict = {'A': np.array([1, 2, 3]), 'B': np.array([4, 5, 6]), 'C': np.array([7, 8, 9])}

# select row 1 from the dictionary
selected_row = {key: arr[1] for key, arr in my_dict.items()}

# print the selected row
print(selected_row)

import pandas as pd

# create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

# select row 1, column 2 using .iloc
selected_value = df.iloc[1, 2]

# print the selected value
print(selected_value)

import pandas as pd

# create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}, index=['row1', 'row2', 'row3'])

# select row with index label 'row2', column with label 'B' using .loc
selected_value = df.loc['row2', 'B']

# print the selected value
print(selected_value)

import pandas as pd
import numpy as np

# create a DataFrame with some missing values
df = pd.DataFrame({'A': [1, 2, np.nan], 'B': [4, np.nan, 6], 'C': [np.nan, 8, 9]})

# check for missing values using .isnull()
print(df.isnull())

# check for non-missing values using .notnull()
print(df.notnull())

import pandas as pd
import numpy as np

# create a DataFrame with some missing values
df = pd.DataFrame({'A': [1, 2, np.nan, 4], 'B': [5, np.nan, np.nan, 8], 'C': [9, 10, 11, np.nan]})

# fill missing values with a specified value using .fillna()
df_filled = df.fillna(0)
print(df_filled)

# fill missing values with the mean of the column using .fillna()
df_mean = df.fillna(df.mean())
print(df_mean)

# replace specific values with another value using .replace()
df_replace = df.replace(np.nan, -1)
print(df_replace)

# fill missing values with interpolated values using .interpolate()
df_interpolated = df.interpolate()
print(df_interpolated)

import pandas as pd
import numpy as np

# create a DataFrame with some missing values
df = pd.DataFrame({'A': [1, 2, np.nan, 4], 'B': [5, np.nan, np.nan, 8], 'C': [9, 10, 11, np.nan]})

# drop rows with missing values using .dropna()
df_dropped = df.dropna()
print(df_dropped)
