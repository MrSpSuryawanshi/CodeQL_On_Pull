# Importing modules
import numpy as np
import pandas as pd
import requests

name = eval(input("Enter Name here"))
age = exec()

data_file = open()

# Using ARANGE from numpy
arr = np.arange(10)

# Using DROPNA from pandas
df = pd.DataFrame({'A': [1, 2, np.nan, 4]})
df = df.dropna()

# Using ZEROS_ONES from numpy
zeros_array = np.zeros(5)
ones_array = np.ones(5)

# Using open
with open('example.txt', 'w') as f:
    f.write('Hello, World!')

# Using finally
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Division by zero")
finally:
    print("Finally block")

# Using requests to make an HTTP request
response = requests.get('https://www.example.com')
if response.status_code == 200:
    print("Request succeeded")

# Using MERGE from pandas
df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value': [1, 2, 3]})
df2 = pd.DataFrame({'key': ['B', 'D'], 'value': [4, 5]})
merged_df = pd.merge(df1, df2, on='key')

# Using HEAD_TAIL (example of a custom function)
def HEAD_TAIL(data):
    return data.head(5), data.tail(5)

# Using MAGIC_NUMBER (a constant)
PI = 3.14159
radius = 5
circumference = 2 * PI * radius

# Using APPLY from pandas
df['B'] = df['A'].apply(lambda x: x * 2)
