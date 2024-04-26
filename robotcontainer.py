#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

#import commands2
#import commands2.button
#import commands2.cmd

import subsystems.lightshow as ls
import subsystems.drivesubsystemA as dsa


class RobotContainer:
    """
    This class is where the bulk of the robot should be declared. Since Command-based is a
    "declarative" paradigm, very little robot logic should actually be handled in the :class:`.Robot`
    periodic methods (other than the scheduler calls). Instead, the structure of the robot (including
    subsystems, commands, and button mappings) should be declared here.

    """

    def __init__(self):

        # create lightshow
        self.lightshow = ls.Lightshow()
        self.drive = dsa.DriveSubsystemA()

    def configureButtonBindings(self):
        """
        Use this method to define your button->command mappings. Buttons can be created via the button
        factories on commands.button.CommandGenericHID or one of its
        subclasses (commands.button.CommandJoystick or command2.button.CommandXboxController).
        """
        pass

    def getAutonomousCommand(self): # -> commands2.Command:
        """
        Use this to pass the autonomous command to the main :class:`.Robot` class.

        :returns: the command to run in autonomous
        """
        pass