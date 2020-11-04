from mcp3008 import MCP3008
import time


adc = MCP3008()

while True:
	value = adc.read( channel = 1 ) #
	print("Normalised Value: %.4f" % (value / 1023.0) )
	time.sleep(0.1)
