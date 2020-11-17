import pandas as pd


xre = pd.read_csv('XRE.TO Historical Prices.csv')
xre['Date'] = pd.to_datetime(xre['Date'], dayfirst=False)
xre.set_index(keys='Date', inplace=True)