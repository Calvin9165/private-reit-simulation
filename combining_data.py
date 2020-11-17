import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from loading_non_om_data import xre
from loading_om_data import centurion, rise, equiton
from cleaning_data_functions import start_date_finder, end_date_finder


df_list = [xre, centurion, equiton]

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

# remove unwanted days
reit_data.dropna(how='any', axis=0, inplace=True)

reit_data.plot()
plt.show()

reit_data_pct = reit_data.pct_change()

cum_prod = np.cumprod(1 + reit_data_pct)

cum_prod.plot()
plt.show()

print(cum_prod)


