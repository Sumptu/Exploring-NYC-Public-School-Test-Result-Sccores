import pandas as pd
import numpy as np

schools = pd.read_csv("schools.csv")

filtered_schools = schools[schools["average_math"] >= 0.8 * 800]

sorted_schools = filtered_schools.sort_values("average_math", ascending=False)

best_math_schools = sorted_schools[["school_name", "average_math"]]

print(best_math_schools)   

