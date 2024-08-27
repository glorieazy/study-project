import numpy as np
import matplotlib.pyplot as plt

# Parameters
l1 = 1.0  # Length of the first link
l2 = 1.0  # Length of the second link
t = np.linspace(0, 10, 500)  # Time from 0 to 10 seconds
dt = t[1] - t[0]  # Time step

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

# Compute velocities using analytical derivatives
vx_analytic = np.gradient(x_analytic, dt)
vy_analytic = np.gradient(y_analytic, dt)

# Compute velocities using forward difference method
vx_fd = (x_analytic[1:] - x_analytic[:-1]) / dt
vy_fd = (y_analytic[1:] - y_analytic[:-1]) / dt

# Compute velocities using central difference method
vx_cd = (x_analytic[2:] - x_analytic[:-2]) / (2 * dt)
vy_cd = (y_analytic[2:] - y_analytic[:-2]) / (2 * dt)

# Prepare time arrays for each method's results
t_fd = t[1:]  # One step reduced for forward difference
t_cd = t[1:-1]  # Two steps reduced for central difference

# Create a figure with 3 horizontal subplots
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# Plot for Analytical Velocities
axs[0].plot(t, vx_analytic, label='vx (Analytical)', color='b')
axs[0].plot(t, vy_analytic, label='vy (Analytical)', color='g')
axs[0].set_title('Analytical Velocities')
axs[0].set_xlabel('Time (s)')
axs[0].set_ylabel('Velocity (m/s)')
axs[0].legend()
axs[0].grid(True)

# Plot for Forward Difference Velocities
axs[1].plot(t_fd, vx_fd, label='vx (Forward Diff)', linestyle='--', color='b')
axs[1].plot(t_fd, vy_fd, label='vy (Forward Diff)', linestyle='--', color='g')
axs[1].set_title('Forward Difference Velocities')
axs[1].set_xlabel('Time (s)')
axs[1].set_ylabel('Velocity (m/s)')
axs[1].legend()
axs[1].grid(True)

# Plot for Central Difference Velocities
axs[2].plot(t_cd, vx_cd, label='vx (Central Diff)', linestyle='-.', color='b')
axs[2].plot(t_cd, vy_cd, label='vy (Central Diff)', linestyle='-.', color='g')
axs[2].set_title('Central Difference Velocities')
axs[2].set_xlabel('Time (s)')
axs[2].set_ylabel('Velocity (m/s)')
axs[2].legend()
axs[2].grid(True)

# Adjust layout and display the plot
plt.tight_layout()
plt.show()