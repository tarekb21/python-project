import csv
import pandas as pd # pandas will help us read and write on csv files

data = {
    "Name": ["Sally", "Ally", "Omar", "Jake", "Jack"], 
    "Age": [23, 21, 25, 23, 22]
        }
    

#DataFrame is a data structure that organizes data into a 2-dimensional table of rows and columns, much like a spreadsheet
data = pd.DataFrame(data)
data.to_csv("age_data.csv")
print(data.head())
