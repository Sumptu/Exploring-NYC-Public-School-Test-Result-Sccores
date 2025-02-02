import pandas as pd
import numpy as np

schools = pd.read_csv("schools.csv")

schools["total_SAT"] = schools["average_math"] + schools["average_reading"] + schools["average_writing"]

grouped = schools.groupby('borough')['total_SAT'].agg(['std', 'mean', 'count']).reset_index()

largest_std_dev_row = grouped.loc[grouped['std'].idxmax()]  

largest_std_dev = pd.DataFrame({
    'borough': [largest_std_dev_row['borough']],
    'num_schools': [largest_std_dev_row['count']],
    'average_SAT': [largest_std_dev_row['mean']],
    'std_SAT': [largest_std_dev_row['std']]
}).round(2)


print(largest_std_dev)