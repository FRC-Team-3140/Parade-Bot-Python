#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

#import commands2
#import commands2.button
#import commands2.cmd

import subsystems.lightshow as ls
import subsystems.differential_drive as dsa
from wpilib import XboxController
from commands.drivercontrol import DriverControlCommand

# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import commands2
import commands2.cmd
import commands2.button

import constants
import subsystems.differential_drive


class RobotContainer:

    def __init__(self):

        self.lightshow = ls.Lightshow()
        self.lightshow_command = commands2.cmd.run(self.lightshow.periodic, self.lightshow)

        self.robotDrive = subsystems.differential_drive.DifferentalDrive()
        

        # The driver's controller
        self.driverController = XboxController(0)

        # Configure the button bindings
        self.configureButtonBindings()

        # Configure default commands
        # Set the default drive command to split-stick arcade drive
        # self.robotDrive.setDefaultCommand(
        #     # A split-stick arcade command, with forward/backward controlled by the left
        #     # hand, and turning controlled by the right.
        #     commands2.cmd.run(
        #         lambda: self.robotDrive.arcadeDrive(
        #             -self.driverController.getLeftY(),
        #             -self.driverController.getRightX(),
        #         ),
        #         self.robotDrive,
        #     )
        # )

        self.robotDrive.setDefaultCommand( DriverControlCommand(self.robotDrive, self.driverController) )



    def configureButtonBindings(self):
        """
        Use this method to define your button->command mappings. Buttons can be created via the button
        factories on commands2.button.CommandGenericHID or one of its
        subclasses (commands2.button.CommandJoystick or command2.button.CommandXboxController).
        """

        # Configure your button bindings here

        # We can bind commands while retaining references to them in RobotContainer

        # Spin up the shooter when the 'A' button is pressed
        #self.driverController.A().onTrue(self.spinUpShooter)

        # Turn off the shooter when the 'B' button is pressed
        #self.driverController.B().onTrue(self.stopShooter)

        # We can also write them as temporary variables outside the bindings

        # Shoots if the shooter wheel has reached the target speed
        #shoot = commands2.cmd.either(
            # Run the feeder
        #    commands2.cmd.runOnce(self.shooter.runFeeder, [self.shooter]),
            # Do nothing
        #    commands2.cmd.nothing(),
            # Determine which of the above to do based on whether the shooter has reached the
            # desired speed
        #    lambda: self.shooter.getController().atSetpoint(),
        #)

        #stopFeeder = commands2.cmd.runOnce(self.shooter.stopFeeder, [self.shooter])

        # Shoot when the 'X' button is pressed
        #self.driverController.X().onTrue(shoot).onFalse(stopFeeder)

        # We can also define commands inline at the binding!

        # While holding the shoulder button, drive at half speed
        #self.driverController.rightBumper().onTrue(
        #    commands2.cmd.runOnce(
        #        lambda: self.robotDrive.setMaxOutput(0.5), [self.robotDrive]
        #    )
        #).onFalse(
        #    commands2.cmd.runOnce(
        #        lambda: self.robotDrive.setMaxOutput(1), [self.robotDrive]
        #    )
        #)

    def getAutonomousCommand(self) -> commands2.Command:
        """
        Use this to pass the autonomous command to the main :class:`.Robot` class.

        :returns: the command to run in autonomous
        """
        return None
