import pandas as pd
import matplotlib.pyplot as plt

from cleaning_data_functions import clean_om_funds_from_dataphile

centurion = pd.read_excel('Centurion Historical Prices.xlsx')
rise = pd.read_excel('Rise Historical Prices.xlsx')
equiton = pd.read_excel('Equiton Historical Prices.xlsx')

# columns to remove
cols_to_drop = {

    'Short Name',
    'Day',
    'Market Code',
    'Price Source',
    'Bid Price',
    'Ask Price',
    'Statement Price',
    'Update Date',
    'Trade Volume',
    'Price Status',
    'Statement Price Status'
}

# adjusted DataFrames
centurion = clean_om_funds_from_dataphile(centurion, cols_to_drop)
rise = clean_om_funds_from_dataphile(rise, cols_to_drop)
equiton = clean_om_funds_from_dataphile(equiton, cols_to_drop)