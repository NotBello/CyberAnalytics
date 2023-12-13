# Created By Venujan Malaiyandi
# BSCP|CS|61|101
# For Task 3.1P
# Cyber Security Analytics

import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('ielts_scores.csv')

# Use for loop and find average, min, max for columns except Nationality
for column in df.columns:
    if column != 'Nationality':
        average = df[column].mean()
        minimum = df[column].min()
        maximum = df[column].max()

        print(f"{column} Average: {average}")
        print(f"{column} Minimum: {minimum}")
        print(f"{column} Maximum: {maximum}")
        print("")

# Use loc to index the entire max nationality row by omiting column value
max_overall_Nationality_score = df.loc[df['Overall'].idxmax()]

#Print the indexed row 
print(f"The country with the highest overall score is:\n{max_overall_Nationality_score}")


