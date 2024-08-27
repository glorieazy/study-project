import numpy as np
import matplotlib.pyplot as plt

# Parameters
l1 = 1.0  # Length of the first link
l2 = 1.0  # Length of the second link
t = np.linspace(0, 10, 500)  # Time from 0 to 10 seconds

# Define joint angles as simple functions of time
q1 = 0.1 * t
q2 = 0.05 * t

# Compute end-effector position using the analytical solution
def end_effector_pos(q1, q2, l1, l2):
    x = l1 * np.cos(q1) + l2 * np.cos(q1 + q2)
    y = l1 * np.sin(q1) + l2 * np.sin(q1 + q2)
    return x, y

# Calculate the end-effector positions
x_analytic, y_analytic = end_effector_pos(q1, q2, l1, l2)

# Plotting the trajectory using the analytical method
plt.figure(figsize=(8, 6))
plt.plot(x_analytic, y_analytic, label='Analytical Trajectory', color='b')
plt.title('Wrist Keypoint Trajectory (Analytical)')
plt.xlabel('X position (m)')
plt.ylabel('Y position (m)')
plt.legend()
plt.show()