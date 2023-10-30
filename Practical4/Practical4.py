# Define the function y = (x + 3)^2
def objective_function(x):
    return (x + 3) ** 2


# Define the gradient of the function
def gradient(x):
    return 2 * (x + 3)


# Gradient Descent parameters
learning_rate = 0.1  # Adjust the learning rate as needed
num_iterations = 100  # You can adjust the number of iterations

# Initial starting point
x = 2

# Gradient Descent optimization
for i in range(num_iterations):
    # Compute the gradient at the current point
    grad = gradient(x)

    # Update x using the gradient and learning rate
    x = x - learning_rate * grad

    # Print the current iteration and x value
    print(f"Iteration {i + 1}: x = {x}, y = {objective_function(x)}")

# Print the final result
print("\nLocal minimum:")
print(f"x = {x}, y = {objective_function(x)}")
