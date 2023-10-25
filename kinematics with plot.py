import numpy as np
import matplotlib.pyplot as plt
import math

x_list = []
y_list = []
theta_list = []
time_list = []

class UnicycleRobot:
    def __init__(self, x, y, theta):
        self.x = x  # Initial X position
        self.y = y  # Initial Y position
        self.theta = theta  # Initial orientation (angle)

    def update_pose(self, v, omega, dt):
        # Update the robot's pose based on linear velocity (v) and angular velocity (omega)
        self.x += v * np.cos(self.theta) * dt
        self.y += v * np.sin(self.theta) * dt
        self.theta += omega * dt

        if(self.theta>math.radians(360)):
            self.theta = 0

        return self.x,self.y,self.theta

init_x = 0.5
init_y = 1
init_theta = 0
print("Initial Pose :",init_x,init_y,init_theta)

Robot_1 = UnicycleRobot(init_x, init_y, init_theta)

v = 0.1 # m/s
omega = 0.152 # rad/sec
dt = 0.1 # sec
time = 0
for x in range(500):
    x,y,theta = Robot_1.update_pose(v, omega, dt)
    time +=dt
    
    x_list.append(x)
    y_list.append(y)
    theta_list.append(theta)
    time_list.append(time)

plt.figure()
plt.plot(x_list, y_list, label="Robot Trajectory")
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.title("XY plot of robot")
plt.grid(True)
plt.legend()

plt.figure()
plt.plot(time_list, theta_list, label="Robot theta")
plt.xlabel("Time [sec]")
plt.ylabel("Theta [radians]")
plt.title("Robot Orientation Over Time")
plt.grid(True)

plt.show()