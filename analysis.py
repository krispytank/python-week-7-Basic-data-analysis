import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

df = pd.read_csv ('street.csv')

# print check dataframe
print("\nsummary data:")
print(df.head())

# check for missing values
missing_values = df.isnull().sum()

# print missing values
print("\nMising values:")
print(missing_values)

# clean dataset by droping missing row values
df_dropped_rows = df.dropna()
print("DataFrame after dropping rows with any missing value:")
print(df_dropped_rows)

# clean dataset by droping missing cols values
df_dropped_cols = df.dropna(axis=1)
print("\nDataFrame after dropping columns with any missing value:")
print(df_dropped_cols)

# Compute the basic statistics
summary_stats = df.describe()

# Print the resulting DataFrame
print("\nSummary statistics")
print(summary_stats)

# group by ward and compute mean for each section
ward_grouop = df.groupby('WARD')

# mean of section in a ward
mean_section_ward = ward_grouop['SECTION'].mean()
print("\nMean section per ward")
print(mean_section_ward)


# line chart
plt.plot(df['WARD'], df['SECTION'])
plt.xlabel('WARD')
plt.ylabel('SECTION')
plt.title('WARD by SECTION')
plt.show()

# bar chart
df.groupby('WARD')['SECTION'].mean().plot(kind = 'bar')
plt.xlabel('WARD')
plt.ylabel('SECTION')
plt.title('Average section by ward')
plt.show()


#histogram
df['WARD'].plot(kind = 'hist', bins = 100)
plt.xlabel('WARD')
plt.ylabel('WARD')
plt.title('ward distribution')
plt.show()


#scatter
df.plot(kind = 'scatter', x='WARD', y='SECTION')
plt.title('ward vs section')
plt.show()