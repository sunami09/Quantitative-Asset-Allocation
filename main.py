from urllib.request import urlopen
import json
import sys
from apikey import api
import certifi
import tkinter as tk
from tkinter import *
import pandas as pd
import ssl
import math
from pandastable import Table, TableModel


# Create a SSL context
ssl_context = ssl.create_default_context()
ssl_context.load_verify_locations(cafile=certifi.where())


def get_data(url):
    response = urlopen(url, context=ssl_context)
    if response.getcode() == 200:
        print("API Response Successful")
    else:
        print("API Response Failed")
        sys.exit()
    return json.load(response)

url = f"https://financialmodelingprep.com/api/v3/sp500_constituent?apikey={api}"
data = get_data(url)

with open("data.json", 'w') as f:
    json.dump(data, f, indent=2)

symbol = []

for blob in data:
    symbol.append(blob['symbol'])

quote = ','.join(symbol)

url = f"https://financialmodelingprep.com/api/v3/quote/{quote}?apikey={api}"
quote = get_data(url)

with open("quote.json", 'w') as f:
    json.dump(quote, f, indent=2)

columns = ['Name', 'Symbol', 'Price', 'Market Capitalization', 'Weight', 'Number of Shares to Buy', 'Portfolio Allocation']
df = pd.DataFrame(columns=columns)

asset = 0
for ticker in quote:
    asset += ticker['marketCap']
    df = df._append(
        pd.Series([
            ticker['name'],
            ticker['symbol'],
            ticker['price'],
            ticker['marketCap'],
            'N/A',
            'N/A',
            'N/A'
        ], index = columns),
        ignore_index = True
    )
for i in range(0, len(df.index)):
    df.loc[i, 'Weight'] = (df.loc[i, 'Market Capitalization'] / asset) * 100


money = float(input("Enter The Size of your Portfolio: "))



for i in range(0, len(df.index)):
    df.loc[i, 'Number of Shares to Buy'] =math.floor(((df.loc[i, 'Weight'] / 100) * money) / df.loc[i, 'Price'])

    df.loc[i, 'Portfolio Allocation'] = round(df.loc[i, 'Number of Shares to Buy'] * df.loc[i, 'Price'], 2)





df.to_csv('datasource.csv', index=False)
df.to_excel('datasource.xlsx', index=False)
print(df)

class TestApp(Frame):
        """Basic test frame for the table"""
        def __init__(self, parent=None):
            self.parent = parent
            Frame.__init__(self)
            self.main = self.master
            self.main.geometry('1100x800+30+30')
            self.main.title('Table app')
            self.main.attributes('-topmost', 1)
            #self.main.after_idle(self.main.attributes, '-topmost', 0)
            
            f = Frame(self.main)
            f.pack(fill=BOTH,expand=1)
            df = pd.read_excel('datasource.xlsx')
            self.table = pt = Table(f, dataframe=df,
                                    showtoolbar=True, showstatusbar=True)
           

            pt.show()
          
            return


app = TestApp()


app.mainloop()
