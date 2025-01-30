import csv
import numpy as np
import matplotlib.pyplot as plt

"""
Formula: 
b0 = (N * (sum_xy - sum_x * sum_y) / (N * sum_x_squared - sum_x ** 2)
b1 = (sum_y - b0 * sum_x) / N
"""

# Read data from CSV file

file_path = 'DAV/exp1Dataset.csv'
rows = []
with open(file_path, 'r') as file:
    csvreader = csv.reader(file)
    next(csvreader)
    for row in csvreader:
        rows.append([int(row[1]), int(row[2])])

# Extract Minutes and Units
minutes = np.array([row[0] for row in rows])
units = np.array([row[1] for row in rows])

# Calculate the necessary sums
N = len(units)
sum_x = np.sum(units)
sum_y = np.sum(minutes)
sum_xy = np.sum(minutes * units)
sum_x_squared = np.sum(units ** 2)

# Calculate b0 and b1 using the given formula
numerator = ((N * sum_xy) - (sum_x * sum_y))
denomerator = ((N * sum_x_squared) - (sum_x) ** 2)
b1 = numerator / denomerator
b0 = (sum_y - b1 * sum_x) / N

print(f'Numerator: {numerator}')
print(f'Denomerator: {denomerator}')
print(f'b0: {b0}')
print(f'b1: {b1}')

# Define the regression model
def predict(x):
    return b0 * x + b1

# Calculate predictions
predictions = predict(minutes)

# Plot the data and the regression line
plt.scatter(minutes, units, color='blue', label='Data points')
plt.plot(minutes, predictions, color='red', label='Regression line')
plt.xlabel('Minutes')
plt.ylabel('Units')
plt.legend()
plt.show()

# Calculate standard error
errors = units - predictions
squared_errors = errors ** 2
standard_error = np.sqrt(np.mean(squared_errors))
print(f'Standard Error: {standard_error}')

# Calculate accuracy (R-squared)
ss_total = np.sum((units - np.mean(units)) ** 2)
ss_residual = np.sum(squared_errors)
r_squared = 1 - (ss_residual / ss_total)
print(f'Accuracy (R-squared): {r_squared}')