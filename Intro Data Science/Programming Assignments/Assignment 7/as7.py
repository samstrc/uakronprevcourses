# Sam Strickler, Data Science, Assignment 7

# Modules
from matplotlib import pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import numpy as np
import statsmodels.api as sm

# Importing and displaying csv dataset
df = pd.read_csv('data.csv')
print(df)

#--------------------------------------------------------------------------------------------------------------
# PROBLEM 1

# a) Load the data and compute the linear regression line for X = mile number to
# predict Y = mile time in minutes. Include in your code after computing the
# regression a comment a)#y = the equation of the line.

# Let X represent the number of miles and let Y represent mile time (min)

# Creates a scatterplot for mile and minutes columns, calculates the correlation coefficient
plt.scatter(df.Mile, df.Minutes)
r = np.corrcoef(df.Mile,df.Minutes)[0,1]
print('\n\nThe value of r for X = Mile and Y = Minutes is {} \n\n'.format(r))

Y=df.Minutes
X=df.Mile

# Preparing the variables for regression, to keep track of predictor/outcome
X=sm.add_constant(X)

# Adds the constants, makes the summary include beta_0 and beta_1
lr_model = sm.OLS(Y,X).fit()

# OLS means “Ordinary Least Squares” regression
print(lr_model.summary())

# ans: The equation of the regression line is y = 0.0817x + 14.1087

# b) Interpret the regression coefficient in context of the problem. Have your answer as
# a comment #b) interpretation.

# ans: The regression coefficient in this calculation is 0.0817. In the context of the dataset, it means that
# on average, for each additional mile, the time (in minutes) is expected to increase by about 0.082 minutes. 


# c) Create a scatter plot, including the regression line. Underneath the piece of code
# which finishes the plot, include a comment #c) is done.

# Pick 100 points equally spaced
X_prime = np.linspace(X.Mile.min(), X.Mile.max(), 110)
X_prime = sm.add_constant(X_prime)

# Calculate the predicted values
y_hat = lr_model.predict(X_prime)

# Plots the regression line with the scatter plot
plt.scatter(df.Mile, df.Minutes)
plt.plot(X_prime[:,1], y_hat, 'red', alpha=0.9)
plt.xlabel('Miles')
plt.ylabel('Minutes')
print(plt.show())

# ans: The code above completes part c.



#--------------------------------------------------------------------------------------------------------------

# PROBLEM 2
# a & c) Load the data and compute the multilinear regression model for X = mile number and Y = net elevation 
# to predict Z = mile time in minutes. Create a scatter plot for X, Y and Z, including the multilinear regression plane.
# Underneath the piece of code which finishes the plot, include a comment #c) is
# done.

# Setting up the variables for the multilinear regression model
X_multi = df[['Mile', 'Elevation']]  # Predictor variables: Mile and Elevation
Z = df['Minutes']  # Target variable: Minutes

# Add a constant term to include the intercept in the model
X_multi = sm.add_constant(X_multi)

# Fit the multilinear regression model
multi_lr_model = sm.OLS(Z, X_multi).fit()

# Display the model summary
print(multi_lr_model.summary())

# Visualization Code
X1 = df['Mile']  # Mile
X2 = df['Elevation']  # Elevation

# Create the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter plot with labels
ax.scatter(X1, X2, Z)
ax.set_xlabel('Miles')
ax.set_ylabel('Elevation (ft)')
ax.set_zlabel('Minutes')

# Fit the plane using np.linalg.lstsq for visualization
A = np.vstack([X1, X2, np.ones_like(X1)]).T
plane_coef, _, _, _ = np.linalg.lstsq(A, Z, rcond=None)

# Create a mesh grid for the plane 
X1_plane, X2_plane = np.meshgrid(
    np.linspace(X1.min(), X1.max(), 10),
    np.linspace(X2.min(), X2.max(), 10)
)
Z_plane = plane_coef[0] * X1_plane + plane_coef[1] * X2_plane + plane_coef[2]

# Add regression plane to the plot
ax.plot_surface(X1_plane, X2_plane, Z_plane, alpha=0.5, color='orange')

plt.show()

# ans: The regression plane equation is: Z = 0.0813X1 + 0.0039X2 + 14.1303 (I think)

# b) Use your answer for part a) to predict the length of time for mile 51 if mile 51
# has a net elevation gain of 42 feet. Include in your code #b) prediction Z = your
# prediction.

# Extracting the coefficients from the fitted model
intercept = multi_lr_model.params['const']
beta_mile = multi_lr_model.params['Mile']
beta_elevation = multi_lr_model.params['Elevation']

# Predicting the time for mile 51 with an elevation gain of 42 feet
mile_51 = 51
elevation_51 = 42
Z_prediction = intercept + beta_mile * mile_51 + beta_elevation * elevation_51

# Displaying the prediction
print("\n\nMaking prediction for  mile = 51 and elevation = 42...\nPrediction Z = {} minutes for the provided input data.".format(Z_prediction))