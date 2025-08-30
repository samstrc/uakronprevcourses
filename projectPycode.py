# Sam Strickler, Inro Data Science, Final Project


# Importing modules and opening data frame -------------------------------------------------------------------------------------------

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
# ***From week 5 and 10 slides
df = pd.read_csv('chicagoschools.csv')


# Cleaning/preprocessing data -------------------------------------------------------------------------------------------

# I had to use the internet to figure out how to do this.
# First, create a list of the quantitative variables we are studying.
quantitative_vars = ['Average_ACT_School', 'Graduation_Rate_School', 'Student_Count_Low_Income']
# The line of code below essentially makes sure that the columns in the quantitative_vars list of the data frame df are converted to numeric data types
df[quantitative_vars] = df[quantitative_vars].apply(pd.to_numeric, errors='coerce') # Uses pandas to_numeric function to convert between types


# Drop rows with missing values in the selected quantitative variables
# I also had to google what was causing errors in my code and this fixed the calculations below by removing rows with missing values.
df_cleaned = df.dropna(subset=quantitative_vars)


# Plot data & perform exploratory analysis -------------------------------------------------------------------------------------------

# For the following plots, I will use the cleaned dataframe to make visualizations and calculate correlation coefficients
# Scatter Plot of Average ACT vs Graduation Rate
# ***From week 10 slides
plt.scatter(df_cleaned.Average_ACT_School, df_cleaned.Graduation_Rate_School) # Makes scatter plot
plt.xlabel('Average ACT School') # Labels x-axis
plt.ylabel('Graduation Rate School') # Labels y-axis
plt.title('Scatter Plot: ACT and Graduation Rate') # Labels title of scatter plot
plt.show() # Displays plot to user

# Scatter Plot of Average ACT and Student Count Low Income
# ***From week 10 slides
plt.scatter(df_cleaned.Student_Count_Low_Income, df_cleaned.Average_ACT_School) # Makes scatter plot
plt.xlabel('Student Count Low Income') # Labels x-axis
plt.ylabel('Average ACT School') # Labels y-axis
plt.title('Scatter Plot: Low-Income Count and Average ACT School') # Labels title of scatter plot
plt.show() # Displays plot to user

# Scatter Plot: Graduation Rate vs Student Count Low Income
# ***From week 10 slides
plt.scatter(df_cleaned.Student_Count_Low_Income, df_cleaned.Graduation_Rate_School) # Makes scatter plot
plt.xlabel('Student Count Low Income') # Labels x-axis
plt.ylabel('Graduation Rate School') # Labels y-axis
plt.title('Scatter Plot: Graduation Rate vs Low-Income Count') # Labels title of scatter plot
plt.show() # Displays plot to user

# Calculating correlation coefficients between variables -------------------------------------------------------------------------------------------

# Correlation Coefficient: Average ACT vs Graduation Rate
# ***From week 10 slides
r1 = np.corrcoef(df_cleaned.Average_ACT_School, df_cleaned.Graduation_Rate_School)[0, 1] # Calculates correlation between 2 variables using numpy
print(f"Correlation between Average ACT and Graduation Rate: {r1:.2f}") # Prints correlation (2 decimal places)

# Correlation Coefficient: Average ACT vs Student Count Low Income
# ***From week 10 slides
r2 = np.corrcoef(df_cleaned.Student_Count_Low_Income, df_cleaned.Average_ACT_School)[0, 1] # Calculates correlation between 2 variables using numpy
print(f"Correlation between Average ACT and Student Count Low Income: {r2:.2f}") # Prints correlation (2 decimal places)

# Correlation Coefficient: Graduation Rate vs Student Count Low Income
# ***From week 10 slides
r3 = np.corrcoef(df_cleaned.Student_Count_Low_Income, df_cleaned.Graduation_Rate_School)[0, 1] # Calculates correlation between 2 variables using numpy
print(f"Correlation between Graduation Rate and Student Count Low Income: {r3:.2f}") # Prints correlation (2 decimal places)

