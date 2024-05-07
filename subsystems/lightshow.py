import time
import math

from wpilib import AddressableLED, LEDData, Timer

class Lightshow:
    """
    A class that creates a flowing pattern on the LEDs.

    :param num_leds: The number of LEDs on the robot.
    :param pwm_port: The PWM port that the LEDs are connected to.
    """

    def __init__(self, num_leds, pwm_port):
        """
        Initializes the Lightshow object.

        :param num_leds: The number of LEDs on the robot.
        :param pwm_port: The PWM port that the LEDs are connected to.
        """
        self.num_leds = num_leds  # The number of LEDs on the robot
        self.pwm_port = pwm_port  # The PWM port that the LEDs are connected to
        self.leds = AddressableLED(pwm_port)  # The LED object
        self.leds.setLength(num_leds)  # Set the number of LEDs
        self.leds.start()  # Start the LED object
        self.hue_offset = 0  # The hue offset for the rainbow pattern

        try: 
            self.timer = Timer()
        except ImportError: 
            raise ImportError("wpilib.Timer module not found. Cannot create Timer object.")
   
    def set_hue_offset(self, hue_offset):
        """
        Sets the hue offset for the rainbow pattern.

        :param hue_offset: The hue offset for the rainbow pattern.
        """
        self.hue_offset = hue_offset

    def periodic(self):
        """
        Updates the LEDs with the specified colors.

        This method calculates the RGB values for each LED based on the LED index.
        Finally, it sets the data for the LEDs using the calculated RGB values.
        """
        led_data = []  # Initialize an empty list for the LED data
        for i in range(self.num_leds):  # Loop through each LED
            r, g, b = self.get_color(i)  # Get the RGB values for the current LED index
            led_data.append(LEDData(r, g, b))  # Add the RGB values to the LED data list

        try:
            self.leds.setData(led_data)  # Set the data for the LEDs
        except Exception as e:
            raise Exception(f"Error setting LED data: {str(e)}")

    @staticmethod
    def get_color(i):
        """
        Returns the RGB values for the specified LED index.

        :param i: The LED index (0-based).
        :return: The RGB values as a tuple (red, green, blue).
        """
        colors = [(214,46,2), (253,152,85), (255,255,255), (209,97,162), (162,1,96)]
        return colors[i % len(colors)]
