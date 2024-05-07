import time
import math

from wpilib import AddressableLED, LEDData

class Lightshow:

    # A class that creates a flowing rainbow pattern on the LEDs.

    # :param num_leds: The number of LEDs on the robot.
    # :param pwm_port: The PWM port that the LEDs are connected to.
    
    def __init__(self, num_leds, pwm_port):
        
        # Initializes the Lightshow object.

        #  :param num_leds: The number of LEDs on the robot.
        # :param pwm_port: The PWM port that the LEDs are connected to.
        
        self.num_leds = num_leds  # The number of LEDs on the robot
        self.pwm_port = pwm_port  # The PWM port that the LEDs are connected to
        self.leds = AddressableLED(pwm_port)  # The LED object
        self.leds.setLength(num_leds)  # Set the number of LEDs
        self.leds.start()  # Start the LED object
        self.hue_offset = 0  # The hue offset for the rainbow pattern

try: self.timer = wpilib.Timer()

except: self.timer = time.time

def set_hue_offset(self, hue_offset):

    # Sets the hue offset for the rainbow pattern.

    # :param hue_offset: The hue offset for the rainbow pattern.
    
    self.hue_offset = hue_offset

def periodic(self):
    """
    Updates the LEDs with the flowing rainbow pattern.

    This method calculates the hue value based on the elapsed time since the robot started and the hue_offset attribute.
    It then calculates the RGB values for each LED based on the hue value and the LED index.
    Finally, it sets the data for the LEDs using the calculated RGB values.
    """
    
    hue_increment = 0.005  # The increment for the hue value
    if isinstance(self.timer, time.time):
        hue = (self.timer() * hue_increment + self.hue_offset) % 1  # Calculate the hue value
    else:
        hue = (self.timer.get() * hue_increment + self.hue_offset) % 1  # Calculate the hue value

    led_data = []  # Initialize an empty list for the LED data
    for i in range(self.num_leds):  # Loop through each LED
        h = hue + i / self.num_leds  # Calculate the hue value for the current LED
        r, g, b = self.hsv_to_rgb(h, 1, 1)  # Convert the hue value to RGB values
        led_data.append(LEDData(r, g, b))  # Add the RGB values to the LED data list

    try:
        self.leds.setData(led_data)  # Set the data for the LEDs
    except:
        print("Error setting LED data")

@staticmethod
def hsv_to_rgb(h, s, v):
    """
    Converts HSV values to RGB values.

    :param h: The hue value (0-1).
    :param s: The saturation value (0-1).
    :param v: The value (brightness) value (0-1).
    :return: The RGB values as a tuple (red, green, blue).
    """
    h = h % 1  # Ensure h is in the range 0-1
    s = max(0, min(s, 1))  # Clamp s to the range 0-1
    v = max(0, min(v, 1))  # Clamp v to the range 0-1

    if s == 0:  # If s is 0, the color is a shade of gray
        return v, v, v

    h *= 6  # Calculate the index of the current hue value
    i = int(h)  # Get the integer part of the index
    f = h - i  # Calculate the fractional part of the index
    p = v * (1- s)  # Calculate the value of the primary color
    q = v * (1 - s * f)  # Calculate the value of the secondary color
    t = v * (1 - s * (1 - f))  #Calculate the value of the tertiary color

    if i == 0:  # If the index is 0, calculate the RGB values for red
        r, g, b = v, t, p
    elif i == 1:  # If the index is 1, calculate the RGB values for yellow
        r, g, b = q, v, p
    elif i == 2:  # If the index is 2, calculate the RGB values for green
        r, g, b = p, v, t
    elif i == 3:  # If the index is 3, calculate the RGB values for cyan
        r, g, b = p, q, v
    elif i == 4:  # If the index is 4, calculate the RGB values for blue
        r, g, b = t, p, v
    else:  # If the index is 5, calculate the RGB values for magenta
        r, g, b = v, p, q

    return r, g, b  # Return the RGB values as floats
