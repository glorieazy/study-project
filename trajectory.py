import numpy as np
import matplotlib.pyplot as plt

# Parameters
alpha = 1.0  # Length of the first link
beta = 1.0  # Length of the second link
t = np.linspace(0, 10, 500)  # Time range from 0 to 10 seconds

# Define joint angles as simple functions of time
theta1 = 0.1 * t
theta2 = 0.05 * t

# Compute wrist keypoint position using the analytical solution
def end_effector_pos(theta1, theta2, alpha, beta):
    x = alpha * np.cos(theta1) + beta * np.cos(theta1 + theta2)
    y = alpha * np.sin(theta1) + beta * np.sin(theta1 + theta2)
    return x, y

# Calculate the end-effector positions
x_analytic, y_analytic = end_effector_pos(theta1, theta2, alpha, beta)

# Plotting the trajectory using the analytical method
plt.figure(figsize=(8, 6))
plt.plot(x_analytic, y_analytic, label='Analytical Trajectory', color='b')
plt.title('Wrist Keypoint Trajectory (Analytical)')
plt.xlabel('X position (m)')
plt.ylabel('Y position (m)')
plt.legend()
plt.show()
