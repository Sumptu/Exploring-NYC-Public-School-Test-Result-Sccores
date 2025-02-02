import pandas as pd
import numpy as np

schools = pd.read_csv("schools.csv")

schools["total_SAT"] = schools["average_math"] + schools["average_reading"] + schools["average_writing"]

schools_sorted = schools.sort_values("total_SAT", ascending=False)

top_10_schools = schools_sorted[["school_name", "total_SAT"]]

print(top_10_schools.head(10))

