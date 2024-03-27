# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17mBhfp9CHj-UlaSK4YVexj_z47dkW3Eu
"""

import pandas as pd
import numpy as np

# Let us generate sample data i.e,the  producers, their yield, and their quality score
np.random.seed(0)

producers_data = {
    'Producer_ID': ['Producer001', 'Producer002', 'Producer003', 'Producer004', 'Producer005'],
    'Yield': np.random.randint(1000, 5000, 5),
    'Quality_Score': np.random.uniform(0, 10, 5),
    'Reliability_Score': np.random.uniform(0, 10, 5)
}

producers_df = pd.DataFrame(producers_data)

#We will then  Calculate the average performance metrics keeping the yield, quality score and reliability score in mind
producers_df['Average_Performance'] = (producers_df['Yield'] + producers_df['Quality_Score'] + producers_df[
    'Reliability_Score']) / 3

# Ranking all the producers based on average performance
producers_df['Performance_Rank'] = producers_df['Average_Performance'].rank(ascending=False).astype(int)

# Identify top-performing producers
top_producers = producers_df.sort_values(by='Performance_Rank').head(3)


print("The Top  3 Performing Producers during this year are:")
print(top_producers[['Producer_ID', 'Average_Performance', 'Performance_Rank']])

