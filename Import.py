import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel('./Top 300.xlsx', sheet_name='Sheet1')

print("Column headings:")
print(df.columns)