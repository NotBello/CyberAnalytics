# Created By Venujan Malaiyandi
# BSCP|CS|61|101
# For Task 3.2C
# Cyber Security Analytics

import pandas as pd
import numpy as np
from IPython.display import display

# Read the CSV file into a DataFrame
df = pd.read_csv('result.csv')

# Create new column with the given formulae for new Total column
df['New Total'] = (5/100) * (df['Ass1'] + df['Ass3']) + (15/100) * (df['Ass2'] + df['Ass4']) + (50/100) * df['Exam']

# Create Final column by rounding off the column New Total
df['Final'] = np.where(df['Exam'] < 48, np.minimum(df['New Total'].round(), 44), df['New Total'].round().astype(int))


# Create the new Grade column based on conditions
conditions = [
    (df['Final'] <= 49.45),
    (49.45 < df['Final']) & (df['Final'] <= 59.45),
    (59.45 < df['Final']) & (df['Final'] <= 69.45),
    (69.45 < df['Final']) & (df['Final'] <= 79.45),
    (79.45 < df['Final'])
]

choices = ['N', 'P', 'C', 'D', 'HD']

# Use numpy select to give the grades based on the above conditions
df['Grade'] = np.select(conditions, choices, default='')

# Save the updated columns to result_updated.csv
df.to_csv('result_updated.csv', index=False)

failed_hurdle_df = df[df['New Total'] < 50]  # Check for Total < 50 to filter students who failed to achieve 50
failed_hurdle_df = failed_hurdle_df[failed_hurdle_df['Exam'] <= 48]  # Check for Exam <= 48
failed_hurdle_file_path = 'failedhurdle.csv'
failed_hurdle_df.to_csv(failed_hurdle_file_path, index=False)

# Select the student records with exam score >100
high_score_df = df[df['Exam'] > 100]

# Display the required three types of output
print('The failed hurdle student records: ')
display(failed_hurdle_df)

print('')

print('The high score student records:')
display(high_score_df)
