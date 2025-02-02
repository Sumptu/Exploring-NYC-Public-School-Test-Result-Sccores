# Exploring-NYC-Public-School-Test-Result-Sccores

Overview
This project explores the test result scores of New York City public schools, focusing on math performance, combined SAT scores, and the variability of SAT scores across different boroughs. The analysis is performed using Python and the pandas library.
Objectives
1.	Identify Schools with the Best Math Results:
    o	Determine schools where the average math score is at least 80% of the maximum possible score of 800.
    o	Save the results in a DataFrame called best_math_schools, including "school_name" and "average_math" columns, sorted by "average_math" in descending order.
2.	Find the Top 10 Performing Schools Based on Combined SAT Scores:
    o	Calculate the total SAT score for each school by summing the math, reading, and writing scores.
    o	Save the results in a DataFrame called top_10_schools, containing "school_name" and "total_SAT" columns, ordered by "total_SAT" in descending order.
3.	Determine the Borough with the Largest Standard Deviation in Combined SAT Scores:
    o	Identify the borough with the highest variability in SAT scores.
    o	Save the results in a DataFrame called largest_std_dev, containing:
      	"borough" - the name of the NYC borough.
      	"num_schools" - the number of schools in the borough.
      	"average_SAT" - the mean of "total_SAT".
      	"std_SAT" - the standard deviation of "total_SAT".
    o	Round all numeric values to two decimal places.
Data
The dataset used in this project contains information about NYC public schools, including:
  •	school_name: Name of the school.
  •	borough: NYC borough where the school is located.
  •	average_math: Average math score.
  •	average_reading: Average reading score.
  •	average_writing: Average writing score.
