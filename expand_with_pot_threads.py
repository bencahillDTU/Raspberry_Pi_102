
import time

import Adafruit_GPIO.I2C as I2C
import Adafruit_SSD1306
from mcp3008 import MCP3008
from threading import Thread
import time
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import sys

global sensval
sensval=0

class readSensors:  
    def __init__(self):
        self._running = True

    def terminate(self):  
        self._running = False  

    def run(self):
        global sensval
        while self._running:
            #time.sleep(5) #Five second delay
            value = adc.read( channel = 1 ) #
            vals.append(value)
            del vals[0]
            sensval = sum(vals)/readings
            #print("THREAD:", sensval)
            

# Raspberry Pi pin configuration:
RST = None     # on the PiOLED this pin isnt used

# 128x64 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

# Note you can change the I2C address by passing an i2c_address parameter like:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3C)


# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
x = 0

#Number of values to average over
readings = 50
vals = []
for i in range(readings):
    vals.append(i)

# Load default font.
font = ImageFont.load_default()

#initiate ADC
adc = MCP3008()

 #Create Class
Sensor = readSensors()
#Create Thread
SensorThread = Thread(target=Sensor.run) 
#Start Thread 
SensorThread.start()

while True:
    try:
        x=(sensval/1023.0)*(width-1)
        # Draw a black filled box to clear the image.
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        draw.rectangle((0,20,x*2,height/8-1), outline=0, fill=1)

        # Display image.
        disp.image(image)
        disp.display()
        #time.sleep(.1)
    except KeyboardInterrupt as e:
        sys.exit(e)
        SensorThread.terminate()


    


