#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import wpilib
import wpilib.drive
import commands2
from rev import CANSparkMax
import phoenix5 
import time

import constants

# create a motor controller translator to talonsrx
class TalonMotorController(wpilib.interfaces.MotorController):

    def __init__(self, talon: phoenix5.TalonSRX, *args):
        super().__init__(*args)
        self.is_enabled = True
        self.talon = talon

    def set(self, speed: float):
        if self.is_enabled:
            self.talon.set(phoenix5.ControlMode.PercentOutput, speed)
        else:
            self.talon.set(phoenix5.ControlMode.PercentOutput, 0)

    def get(self) -> float:
        return self.talon.get()
    
    def setInverted(self, isInverted: bool):
        self.talon.setInverted(isInverted)
    
    def getInverted(self) -> bool:
        return self.talon.getInverted()
    
    def disable(self):
        self.is_enabled = False
        self.set(0)

    def enable(self):
        self.is_enabled = True

    def stopMotor(self):
        self.set(0)



class DriveSubsystemA(commands2.Subsystem):
    def __init__(self) -> None:
        """Creates a new DriveSubsystem"""
        super().__init__()

        self.frame_id = 0

        kLeftSparkCANId = 9
        kLeftTalon1CANId = 4
        kLeftTalon2CANId = 6

        kRightSparkCANId = 8
        kRightTalon1CANId = 5
        kRightTalon2CANId = 7

        kCurrentLimit = 40

        self.left_motor1 = CANSparkMax(kLeftSparkCANId, CANSparkMax.MotorType.kBrushless)
        self.left_talon2 = phoenix5.TalonSRX(kLeftTalon1CANId)
        self.left_talon3 = phoenix5.TalonSRX(kLeftTalon2CANId)


        self.right_motor1 = CANSparkMax(kRightSparkCANId, CANSparkMax.MotorType.kBrushless)
        self.right_talon2 = phoenix5.TalonSRX(kRightTalon1CANId)
        self.right_talon3 = phoenix5.TalonSRX(kRightTalon2CANId)

        self.left_motor2 = TalonMotorController(self.left_talon2)
        self.left_motor3 = TalonMotorController(self.left_talon3)

        self.right_motor2 = TalonMotorController(self.right_talon2)
        self.right_motor3 = TalonMotorController(self.right_talon3)


        # Set the motors to brake when they are not getting signal
        self.left_motor1.setIdleMode(CANSparkMax.IdleMode.kBrake)
        #self.left_motor2.setNeutralMode(TalonSRX.NeutralMode.Brake)
        #self.left_motor3.setNeutralMode(TalonSRX.NeutralMode.Brake)

        self.right_motor1.setIdleMode(CANSparkMax.IdleMode.kBrake)
        #self.right_motor2.setNeutralMode(TalonSRX.NeutralMode.Brake)
        #self.right_motor3.setNeutralMode(TalonSRX.NeutralMode.Brake)

        # Set a current limit on the motors
        self.left_motor1.setSmartCurrentLimit(kCurrentLimit)
        self.right_motor1.setSmartCurrentLimit(kCurrentLimit)

        # Set the motors to reverse so that positive voltages move the robot forward
        self.left_motor1.setInverted(True)
        self.left_motor2.setInverted(False)
        self.left_motor3.setInverted(False)

        self.right_motor1.setInverted(False)
        self.right_motor2.setInverted(True)
        self.right_motor3.setInverted(True)

        # get the spark max encoders
        self.leftEncoder = self.left_motor1.getEncoder()
        self.rightEncoder = self.right_motor1.getEncoder()

        # The motors on the left side of the drive.
        self.leftMotors = wpilib.MotorControllerGroup(
            self.left_motor1,
            self.left_motor2,
            self.left_motor3
        )

        # The motors on the right side of the drive.
        self.rightMotors = wpilib.MotorControllerGroup(
            self.right_motor1,
            self.right_motor2,
            self.right_motor3
        )

        # The robot's drive
        self.drive = wpilib.drive.DifferentialDrive(self.leftMotors, self.rightMotors)

    def periodic(self):
        '''
        every 50 calls print out the encoder values
        '''
        self.frame_id += 1
        #if self.frame_id % 50 == 0:
            #print("System Time:",time.time())
            #print("Left Encoder: ", self.leftEncoder.getPosition())
            #print("Right Encoder: ", self.rightEncoder.getPosition())
            #print("done")

    def arcadeDrive(self, fwd: float, rot: float):
        """
        Drives the robot using arcade controls.

        :param fwd: the commanded forward movement
        :param rot: the commanded rotation
        """
        self.drive.arcadeDrive(fwd, rot)

    def stop(self):
        """
        Stops the drive from moving.
        """
        self.arcadeDrive(0,0)

    def resetEncoders(self):
        """Resets the drive encoders to currently read a position of 0."""
        self.leftEncoder.reset()
        self.rightEncoder.reset()

    def getAverageEncoderDistance(self):
        """
        Gets the average distance of the two encoders.

        :returns: the average of the two encoder readings
        """
        return (self.leftEncoder.getDistance() + self.rightEncoder.getDistance()) / 2.0

    def getLeftEncoder(self) -> wpilib.Encoder:
        """
        Gets the left drive encoder.

        :returns: the left drive encoder
        """
        return self.leftEncoder

    def getRightEncoder(self) -> wpilib.Encoder:
        """
        Gets the right drive encoder.

        :returns: the right drive encoder
        """
        return self.rightEncoder

    def setMaxOutput(self, maxOutput: float):
        """
        Sets the max output of the drive. Useful for scaling the drive to drive more slowly.

        :param maxOutput: the maximum output to which the drive will be constrained
        """
        self.drive.setMaxOutput(maxOutput)
