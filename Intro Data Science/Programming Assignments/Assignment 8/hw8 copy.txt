# Sam Strickler, Assignment 8, Intro Data Science

# Problem 1

# This is a list to store all of our values
list <- c(-3, 5, 12, -40, 9, 23, 3, -23, 15, 15, -9) 

i <- 1 # Used to index the list
count <- 0 # Updates for each positive int counted
total <- 0 # Total sum of positive vals 

while (i <= length(list)) { # Iterates over whole list
    if (list[i] > 0) { # If to include only pos vals
        total <- total + list[i] # Adds positve values to total
        count <- count + 1 # Increments counter for every pos val
    }
    i <- i + 1 # Increments iterator regardless of any condition
}

xbar <- total / count # Computes the mean for the dataset
cat("The average of all positive values in this list is: ", xbar, "\n")


# Problem 2

# a) Import the data to be used in R
data <- read.csv("bobcat.csv") 

# b) Summary statistics for 'Minutes'
summary(data$Minutes)

# Calculate mean/average
mean_minutes <- mean(data$Minutes)
cat("Mean:", mean_minutes, "\n")

# Calculate median
median_minutes <- median(data$Minutes)
cat("Median:", median_minutes, "\n")

# Calculate IQR
IQR_value <- IQR(data$Minutes)
cat("IQR:", IQR_value, "\n")

# Calculate the range (max - min) of Minutes
range_minutes <- range(data$Minutes)
cat("Range:", range_minutes, "\n")

# Sample standard deviation for Minutes
sd_minutes <- sd(data$Minutes)
cat("Standard Deviation:", sd_minutes, "\n")

# d) Plot histogram 
hist(data$Minutes, breaks = seq(min(data$Minutes), max(data$Minutes), by = 30), 
     col = "skyblue", main = "Histogram of Mile Times", 
     xlab = "Minutes per Mile", ylab = "Frequency")

# e) Find the correlation between the mile number and the length of the mile
correlation <- cor(data$Mile, data$Minutes)
cat("Correlation:", correlation, "\n")

# f) Scatter plot with regression line
plot(data$Mile, data$Minutes, main = "Scatter Plot of Mile vs Minutes", 
     xlab = "Mile", ylab = "Minutes per Mile", pch = 19)
abline(lm(Minutes ~ Mile, data = data), col = "red")

# g) Linear regression model and equation
model <- lm(Minutes ~ Mile, data = data)
summary(model)

# Get the regression equation
cat("Intercept:", coefficients(model)[1], "\n")
cat("Slope:", coefficients(model)[2], "\n")

# h) Define a function to predict minutes based on the mile number
predict_minutes <- function(mile) {
  intercept <- coefficients(model)[1]
  slope <- coefficients(model)[2]
  return(intercept + slope * mile)
}

# Predictions for miles 6, 15, and 42
cat("Prediction for 6 miles:", predict_minutes(6), "\n")
cat("Prediction for 15 miles:", predict_minutes(15), "\n")
cat("Prediction for 42 miles:", predict_minutes(42), "\n")