import commands2
import commands2.cmd
from wpilib.interfaces import GenericHID
from wpilib import XboxController
from subsystems.drivesubsystemA import DriveSubsystemA

class DriverControlCommand(commands2.CommandBase):
    def __init__(self, drive_subsystem: DriveSubsystemA, controller: XboxController):
        super().__init__()
        self.drive_subsystem = drive_subsystem
        self.controller = controller
        self.addRequirements(drive_subsystem)

    def execute(self):
        # Get the x speed and the z rotation from the controller
        x_speed = self.controller.getLeftY()
        z_rotation = self.controller.getRightX()

        # Use the x speed and z rotation to drive the robot
        self.drive_subsystem.arcadeDrive(x_speed, z_rotation)

    def end(self, interrupted: bool):
        # Stop the robot when the command ends
        self.drive_subsystem.stop()

    def isFinished(self):
        # This command should run until interrupted
        return False