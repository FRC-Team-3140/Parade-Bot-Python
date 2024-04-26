# Import the necessary libraries
import navx

import commands2

# Import the pose2d class from wpimath
from wpimath.geometry import Pose2d

class Gyro(commands2.Subsystem):
    _instance = None

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = cls()
        return cls._instance

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        # Initialize the navx here
        self.ahrs = navx.AHRS.create_spi()




        pass

    def get_angle(self):
        # Get the current angle from the navx
        return self.ahrs.getAngle()
    
    def get_relative_pose2d(self):
        # Get the location of the robot relative to the starting point
        return None # TODO: Pose2d(self.ahrs., 0, self.get_angle())

    def reset_angle(self):
        # Reset the angle to zero
        self.ahrs.reset()
