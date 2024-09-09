import numpy as np
import matplotlib.pyplot as plt

# Function to compute the Lagrange interpolation polynomial
def lagrange_interpolation(x_values, y_values, x):
    """
    Compute the Lagrange interpolation polynomial at a given point x.
    
    Parameters:
    x_values: list of x data points (known x values)
    y_values: list of y data points (corresponding y values)
    x: the x value where the polynomial is evaluated
    
    Returns:
    The interpolated value at the given x
    """
    n = len(x_values)  # Number of data points
    result = 0         # Initialize the result to 0
    
    # Loop through each known data point
    for i in range(n):
        term = y_values[i]  # Start with the y value at i-th point
        
        # Calculate the product for the Lagrange basis polynomial L_i(x)
        for j in range(n):
            if i != j:  # Skip the current point i when j == i
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        
        result += term  # Add the term for the current i-th Lagrange polynomial
    
    return result

# Table of data points (x and y values)
x_values = [0, 1, 2, 3]  # Known x values (nodes)
y_values = [1, 2, 0, 4]  # Corresponding y values at the nodes

# Define a range of x values for plotting the interpolation curve
x_range = np.linspace(min(x_values), max(x_values), 500)

# Compute the interpolated y values for the defined x range
y_interp = [lagrange_interpolation(x_values, y_values, x) for x in x_range]

# Plotting the interpolation polynomial and the original data points
plt.plot(x_range, y_interp, label='Lagrange Interpolation Polynomial')
plt.scatter(x_values, y_values, color='red', label='Known Data Points')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lagrange Interpolation Polynomial')
plt.grid(True)
plt.show()
