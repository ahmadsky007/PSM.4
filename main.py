import numpy as np
import matplotlib.pyplot as plt


g = 9.81
alpha = 30
alpha_rad = np.radians(alpha)
mass = 1.0
radius = 0.1
time_step = 0.01
total_time = 10


I_solid = 2 / 5 * mass * radius ** 2
I_hollow = 2 / 3 * mass * radius ** 2


a_solid = g * np.sin(alpha_rad) / (1 + I_solid / (mass * radius ** 2))
a_hollow = g * np.sin(alpha_rad) / (1 + I_hollow / (mass * radius ** 2))


time_array = np.arange(0, total_time, time_step)


position_solid, velocity_solid, rotation_solid = np.zeros_like(time_array), np.zeros_like(time_array), np.zeros_like(
    time_array)
position_hollow, velocity_hollow, rotation_hollow = np.zeros_like(time_array), np.zeros_like(time_array), np.zeros_like(
    time_array)


for i in range(1, len(time_array)):
    # Solid sphere
    velocity_solid[i] = velocity_solid[i - 1] + a_solid * time_step
    position_solid[i] = position_solid[i - 1] + velocity_solid[i] * time_step
    rotation_solid[i] = rotation_solid[i - 1] + (velocity_solid[i] / radius) * time_step


    velocity_hollow[i] = velocity_hollow[i - 1] + a_hollow * time_step
    position_hollow[i] = position_hollow[i - 1] + velocity_hollow[i] * time_step
    rotation_hollow[i] = rotation_hollow[i - 1] + (velocity_hollow[i] / radius) * time_step


plt.figure(figsize=(14, 7))


plt.subplot(1, 2, 1)
plt.plot(time_array, position_solid, label="Solid Sphere")
plt.plot(time_array, position_hollow, label="Hollow Sphere")
plt.xlabel("Time (s)")
plt.ylabel("Position of Center of Mass (m)")
plt.title("Position of Center of Mass Over Time")
plt.legend()


plt.subplot(1, 2, 2)
plt.plot(time_array, np.degrees(rotation_solid), label="Solid Sphere")
plt.plot(time_array, np.degrees(rotation_hollow), label="Hollow Sphere")
plt.xlabel("Time (s)")
plt.ylabel("Rotation Angle (degrees)")
plt.title("Rotation Angle Over Time")
plt.legend()

plt.tight_layout()
plt.show()
