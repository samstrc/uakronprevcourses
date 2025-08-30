# Sam Strickler, Intro Data Science, Final Project

# Descriptive Analytics ----------------------------------------------------------
# Loading data file, storing correlated variables, printing summary stats
# ***From week 11 slides

# Allow user to select the file interactively
file_path <- file.choose()

# Load the selected file
df <- read.csv(file_path)

# Two most correlated quantitative variables
avg_act <- df$Average_ACT_School # Copies column from data frame
grad_rate <- df$Graduation_Rate_School # Copies column from data frame

# Summary statistics for avg_act
print("Summary for Average ACT School:")
print(summary(avg_act)) # Calls summary function
cat("Standard Deviation for Average ACT School:", sd(avg_act, na.rm = TRUE), "\n") # Prints std dev since summary doesn't calculate it

# Summary statistics for grad_rate
print("Summary for Graduation Rate School:")
print(summary(grad_rate)) # Calls summary function
cat("Standard Deviation for Graduation Rate School:", sd(grad_rate, na.rm = TRUE), "\n") # Prints std dev since summary doesn't calculate it

# Proportion of each category
school_type <- df$School_Type # Loads School_Type column into a variable 
proportions <- prop.table(table(school_type)) # Creates a frequency table

print("Proportions of School Types:")
print(proportions) # Prints proportions of Chicago school types

# Data Visualization ----------------------------------------------------------
# Creates visualizations of each variable's frequency distributions and a pie chart for the categorical variable
# ***From week 11 slides

library(ggplot2) # Loads ggplot2

# Histogram for Average ACT School using ggplot
ggplot(df, aes(x = Average_ACT_School)) +
  geom_histogram(binwidth = 1, fill = "lightblue", color = "black") +
  labs(title = "Histogram of Average ACT School", x = "Average ACT School", y = "Frequency") +
  theme_minimal() 

# Histogram for Graduation Rate School using ggplot
ggplot(df, aes(x = Graduation_Rate_School)) +
  geom_histogram(binwidth = 5, fill = "lightgreen", color = "black") +
  labs(title = "Histogram of Graduation Rate School", x = "Graduation Rate School", y = "Frequency") +
  theme_minimal()

# Pie Chart for School Type using basic R pie chart tool
pie(table(school_type), main = "Pie Chart of School Types", col = rainbow(length(unique(school_type))))
# Bar Graph for School Types using base R bar graph tool
barplot(proportions, 
        main = "Bar Graph of School Types", 
        xlab = "School Type", 
        ylab = "Proportion", 
        col = rainbow(length(proportions))) # Fun theme

# Mechanistic Analytics ---------------------------------------------------------
# Scatter plot with regression line
ggplot(df, aes(x = Average_ACT_School, y = Graduation_Rate_School)) +
  geom_point(color = "blue") +
  stat_smooth(method = "lm", color = "red", se = TRUE) +
  ylim(0, 100) +
  labs(title = "Scatterplot of ACT Scores vs Graduation Rates",
       x = "Average ACT Score",
       y = "Graduation Rate (%)")

# Fit the linear model using lm() function
reg_model <- lm(Graduation_Rate_School ~ Average_ACT_School, data = df)

# Extract coefficients using coef() function
coefficients <- coef(reg_model)
intercept <- coefficients[1]
slope <- coefficients[2]

# Print the equation with rounded output (to two decimal places)
cat("Regression Line: Y =", round(intercept, 2), "+", round(slope, 2), "X\n")

# Predict a value: X = 22 (avg ACT score of 22)
predicted_rate <- intercept + (slope * 22) # Calculate algebraically 
cat("Predicted graduation rate for a school with an average act score of 22: ", round(predicted_rate, 2), "%\n")