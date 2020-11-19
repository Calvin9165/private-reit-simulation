import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from loading_non_om_data import xre
from loading_om_data import centurion, rise, equiton
from cleaning_data_functions import start_date_finder, end_date_finder, expected_index
import pandas_market_calendars as mcal

df_list = [xre, centurion, rise]

starting = []
ending = []

for df in df_list:

    df.sort_index(ascending=True, inplace=True)
    starting.append(df.index[0])
    ending.append(df.index[-1])

# defining the start and end dates
start_date = start_date_finder(dates=starting, how='newest')
end_date = end_date_finder(dates=ending, how='oldest')

# creating the Date Range
date_range = pd.date_range(start_date, end_date, freq='D')

# creating the combined DataFrame
reit_data = pd.DataFrame(index=date_range)


# combine the DataFrames
for df in df_list:

    for column in df.columns:

        reit_data[column] = df[column]


reit_data['RBS201'].dropna(how='any', inplace=True)

reit_data.fillna(0, axis=0, inplace=True)
reit_data['EQP105'] = equiton
reit_data['EQP105'].loc[equiton.index[0]:equiton.index[-1]].fillna(0, inplace=True)

reit_data['composite index'] = reit_data.mean(axis=1)

test = np.cumprod(1 + reit_data)
test.plot()
plt.show()

composite_reits = reit_data['composite index'].pct_change()
composite_reits.to_csv('composite reit returns.csv')
