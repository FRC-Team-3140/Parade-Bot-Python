import wpilib
import time
import commands2


class Lightshow(commands2.Subsystem):

    def __init__(self):
        super().__init__()

        self.kNumLeds = 60  # Replace with your total number of LEDs
        self.kPwmPort = 5  # Replace with your PWM port number

        self.leds = wpilib.AddressableLED(self.kPwmPort)
        self.leds.setLength(self.kNumLeds)
        #nself.leds = wpilib.Led(self.kNumLeds)
        self.startTime = time.time()
        self.frame_id = 0
        self.period = 0.5
        self.update_gait = 3
        self.color1 = wpilib.AddressableLED.LEDData(0,255,0) # Green
        self.color2 = wpilib.AddressableLED.LEDData(0,0,255) # Black
        self.leds.start()

    def setPeriod(period):
        '''
        Time to 
        '''

    def periodic(self):
        self.frame_id = self.frame_id + 1

        # Control how often updates are sent to save compute time.
        if self.frame_id % self.update_gait == 0:
            self.animate_chase()


    def animate_chase(self):
        '''
        Animate a chase pattern 5 LEDs wide and alternating between two colors
        
        '''
        speed = 0.1/self.period

        frame = (self.frame_id * speed)

        led_data = []
        for i in range(self.kNumLeds):
            primary_color = (i + frame) // 5 % 2 == 0
            if primary_color:
                led_data.append(self.color1)
            else:
                led_data.append(self.color2)

        self.leds.setData(led_data)

        







