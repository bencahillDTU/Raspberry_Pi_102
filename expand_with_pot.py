
import time

import Adafruit_GPIO.I2C as I2C
import Adafruit_SSD1306
from mcp3008 import MCP3008
import time




from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

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

readings = 10
vals = []
for i in range(readings):
    vals.append(i)

# Load default font.
font = ImageFont.load_default()
adc = MCP3008()

while True:
    value = adc.read( channel = 1 ) #
    vals.append(value)
    del vals[0]
    av = sum(vals)/readings
    x=(av/1023.0)*(width-1)

    #print(x)
    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    draw.rectangle((0,20,x*2,height/8-1), outline=0, fill=1)

    # Display image.
    disp.image(image)
    disp.display()
    #time.sleep(.1)
    


