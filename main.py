from data_generator import getData
import pandas as pd

with open('collection.json', encoding='utf-8') as inputfile:
    df = pd.read_json(inputfile)

df.to_csv('csvfile.csv', encoding='utf-8', index=False)

print(getData())