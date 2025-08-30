# Define the transition matrix
P <- matrix(c(
  0.7, 0.3, 0,   0,   0,   0,
  0.5, 0.5, 0,   0,   0,   0,
  0.1, 0.1, 0.2, 0.3, 0.1, 0.2,
  0.2, 0,   0.4, 0.1, 0.3, 0,
  0,   0,   0,   0,   0.8, 0.2,
  0,   0,   0,   0,   0.6, 0.4
), nrow = 6, byrow = TRUE)

# Define the states
states <- c("A", "B", "C", "D", "E", "F")

# Part d: Function to compute the n-step transition matrix
n_step_transition <- function(P, n) {
  # Start with the original matrix
  result <- P
  # Multiply the matrix n-1 times to get P^n
  for (i in 2:n) {
    result <- result %*% P
  }
  return(result)
}

# Part e: Compute the 3-step transition matrix and extract specific probabilities
P_3 <- n_step_transition(P, 3)
cat("3-step Transition Matrix:\n")
print(P_3)

cat("P[X4 = B | X1 = A]:", P_3[1, 2], "\n")
cat("P[X4 = B | X1 = D]:", P_3[4, 2], "\n")
cat("P[X4 = C | X1 = F]:", P_3[6, 3], "\n")

# Part f: Compute and print 5-step, 8-step, and 12-step transition matrices
P_5 <- n_step_transition(P, 5)
P_8 <- n_step_transition(P, 8)
P_12 <- n_step_transition(P, 12)

cat("\n5-step Transition Matrix:\n")
print(round(P_5, 6))

cat("\n8-step Transition Matrix:\n")
print(round(P_8, 6))

cat("\n12-step Transition Matrix:\n")
print(round(P_12, 6))

# Part g: Estimate probability of the 1000th bite starting from Criss (C)
P_1000 <- n_step_transition(P, 1000)
cat("\nEstimated probabilities for the 1000th bite starting from Criss:\n")
print(P_1000[3, ])

# Part h: Estimate probability of the 1000th bite starting from Ben (B)
cat("\nEstimated probabilities for the 1000th bite starting from Ben:\n")
print(P_1000[2, ])