

import numpy as np

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

        return self.x,self.y,self.theta

init_x = 0.5
init_y = 1
init_theta = 0
print("Initial Pose :",init_x,init_y,init_theta)

Robot_1 = UnicycleRobot(init_x, init_y, init_theta)

v = 0 # m/s
omega = 1.52 # rad/sec
dt = 1 # sec
x,y,theta = Robot_1.update_pose(v, omega, dt)

print("Pose :",x,y,theta)