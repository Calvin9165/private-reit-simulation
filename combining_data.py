import pandas as pd
import matplotlib.pyplot as plt


from loading_non_om_data import xre
from loading_om_data import centurion, rise, equiton
from cleaning_data_functions import start_date_finder, end_date_finder


df_list = [xre, centurion, rise, equiton]

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





# for df in df_list:
#
#     for column in df.columns:
#
#
#         reit_data[df['CUSIP']]





