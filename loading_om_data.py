import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from cleaning_data_functions import clean_str_to_float

centurion = pd.read_csv('Centurion Monthly Returns.csv')
centurion['Date'] = pd.to_datetime(centurion['Date'], dayfirst=True)
centurion.set_index('Date', inplace=True)
centurion.rename({'Total Return': centurion['CUSIP'][0]}, axis=1, inplace=True)
centurion.drop({'CUSIP', 'NAV Growth', 'Div Growth'}, axis=1, inplace=True)

rise = pd.read_csv('Rise Monthly Returns.csv')
rise['Date'] = pd.to_datetime(rise['Date'], dayfirst=False)
rise.set_index('Date', inplace=True)
rise.rename({'Total Return': rise['CUSIP'][0]}, axis=1, inplace=True)
rise.drop({'CUSIP', 'NAV Growth', 'Dividend Growth'}, axis=1, inplace=True)


equiton = pd.read_csv('Equiton Monthly Returns.csv')
equiton['Date'] = pd.to_datetime(equiton['Date'], dayfirst=False)
equiton.set_index('Date', inplace=True)
equiton.rename({'Total Return': equiton['CUSIP'][0]}, axis=1, inplace=True)
equiton.drop({'CUSIP', 'NAV Growth', 'Distribution Growth'}, axis=1, inplace=True)
equiton = clean_str_to_float(df_to_clean=equiton, chars_to_remove=['%'])
equiton /= 100

print(equiton.head())

test = np.cumprod(1 + equiton['EQP105'])
