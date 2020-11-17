import pandas as pd

centurion = pd.read_excel('Centurion Historical Prices.xlsx')

# print(centurion.head())
# print(centurion.columns)
#
# print(centurion['Market'].head())

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

# remove unwanted columns
centurion.drop(labels=cols_to_drop, axis=1, inplace=True)

# remove prices with none values (i.e. weekends)
centurion.dropna(how='any', axis=0, inplace=True)

# set index
centurion['Price Date'] = pd.to_datetime(centurion['Price Date'], dayfirst=False)
centurion.set_index(keys='Price Date', inplace=True)

centurion
