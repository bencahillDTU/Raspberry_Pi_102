
import os, time
def robot(text):
    os.system("pico2wave -w hello.wav \"" + text + "\"")
    os.system("aplay /home/pi/python_programming/hello.wav")
 
robot("Getting Even Better With Raspberry Pi")