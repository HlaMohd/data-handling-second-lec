import pandas as pd
df_CSV = pd.read_csv('session2_data/student_coffee_crisis.csv')
df_XLSX = pd.read_excel('session2_data/student_coffee_crisis.xlsx')
df_JSON = pd.read_json('session2_data/student_coffee_crisis.json')
print(df_CSV.sample(10))
print(df_XLSX.sample(10))
print(df_JSON.sample(10))
#import os
#print(os.listdir())
#print(os.listdir())
#print(os.getcwd())

