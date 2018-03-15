# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time

from neopixel import *

import argparse
import signal
import sys
def signal_handler(signal, frame):
        colorWipe(strip, Color(0,0,0))
        sys.exit(0)

def opt_parse():
        parser = argparse.ArgumentParser()
        parser.add_argument('-c', action='store_true', help='clear the display on exit')
        args = parser.parse_args()
        if args.c:
                signal.signal(signal.SIGINT, signal_handler)

# LED strip configuration:
LED_COUNT      = 150      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

#def setLEDstrip(LEDmode):
#    print('LEDmode = "' + LEDmode + '"')
#    LEDmode = {
#        "BLUE":  colorAll(strip, Color(0, 0, 255)),      # Blue
#        "RED":   colorAll(strip, Color(255, 0, 0)),      # Red
#        "GREEN": colorAll(strip, Color(0, 255, 0)),      # Green
#        "WHITE": colorAll(strip, Color(255, 255, 255)),  # White
#        "BLACK": colorAll(strip, Color(0, 0, 0)),        # Black
#    }
#    # default
#    colorAll(strip, Color(0, 0, 0))         # Black


# Define functions which animate LEDs in various ways.
def colorAll(strip, color, duration_in_seconds, wait_ms=50):
	"""Wipe color across display all at once, almost."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
#		strip.show()
#		time.sleep(wait_ms/1000.0)
	strip.show()
#	time.sleep(wait_ms/10.0)
	time.sleep(duration_in_seconds/5.0)

def colorFlash(strip, color, duration_in_seconds, wait_ms=50):
	iterations = duration_in_seconds
	for j in range(iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/100.0)
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, 0)
		strip.show()
		time.sleep(wait_ms/100.0)

def colorWipe(strip, color, wait_ms=50):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
	"""Movie theater light style chaser animation."""
	for j in range(iterations):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, color)
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)

def wheel(pos):
	"""Generate rainbow colors across 0-255 positions."""
	if pos < 85:
		return Color(pos * 3, 255 - pos * 3, 0)
	elif pos < 170:
		pos -= 85
		return Color(255 - pos * 3, 0, pos * 3)
	else:
		pos -= 170
		return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
	"""Draw rainbow that fades across all pixels at once."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((i+j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
	"""Draw rainbow that uniformly distributes itself across all pixels."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
	"""Rainbow movie theater light style chaser animation."""
	for j in range(256):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, wheel((i+j) % 255))
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)

# Main program logic follows:
if __name__ == '__main__':
        # Process arguments
        opt_parse()

	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	# Intialize the library (must be called once before other functions).
	strip.begin()

#	print ('Press Ctrl-C to quit.')
#	while True:
#		print ('Color wipe animations.')
#		colorWipe(strip, Color(255, 0, 0))  # Red wipe
#		colorWipe(strip, Color(0, 255, 0))  # Green wipe
#		colorWipe(strip, Color(0, 0, 255))  # Blue wipe
#		print ('Theater chase animations.')
#		theaterChase(strip, Color(127, 127, 127))  # White theater chase
#		theaterChase(strip, Color(127,   0,   0))  # Red theater chase
#		theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase
#		print ('Rainbow animations.')
#		rainbow(strip)
#		rainbowCycle(strip)
#		theaterChaseRainbow(strip)


#	file = open("LEDstrip.txt","w") 
##	file.writelines("Hello World") 
##	file.write("This is our new text file") 
##	file.writelines(" and this is another line.") 
##	file.writelines("Why? Because we can.") 
##	file.writelines("FLASHWHITE")
#	file.writelines("GREEN")
#	file.close()
	file = open("LEDstrip.txt","r")
	print file.read()
	file.close()
	while True:
#        int month = 8;
##        String LEDmode;
           with open("LEDstrip.txt") as file:
		LEDmode = file.read()
           print('LEDmode = "' + LEDmode + '" (Press Ctrl-C to quit.)')
	   file.close()
#         setLEDstrip(LEDmode)

	   if LEDmode == "BLUE":
              colorAll(strip, Color(0, 0, 255), 1)        # Blue
	   elif LEDmode == "RED":
              colorAll(strip, Color(255, 0, 0), 1)        # Red
	   elif LEDmode == "GREEN":
              colorAll(strip, Color(0, 255, 0), 1)        # Green
	   elif LEDmode == "WHITE": 
              colorAll(strip, Color(255, 255, 255), 1)    # White
	   elif LEDmode == "FLASHBLUE":
              colorFlash(strip, Color(0, 0, 255), 3)      # Blue flash
	   elif LEDmode == "FLASHRED":
              colorFlash(strip, Color(255, 0, 0), 3)      # Red flash
	   elif LEDmode == "FLASHGREEN":
              colorFlash(strip, Color(0, 255, 0), 3)      # Green flash
	   elif LEDmode == "FLASHWHITE": 
              colorFlash(strip, Color(255, 255, 255), 10) # White flash
	   else:
              colorAll(strip, Color(0, 0, 0), 1)          # Black

#        colorAll(strip, Color(0, 0, 0), 1)        # Black
#        time.sleep(4)
#        colorAll(strip, Color(255, 255, 255), 1)  # White
#        colorAll(strip, Color(0, 0, 0), 1)        # Black

#def setLEDstrip(LEDmode):
#    print('LEDmode = "' + LEDmode + '"')
#    LEDmode = {
#    }
#    # default
#    colorAll(strip, Color(0, 0, 0))         # Black


#	print ('White theater chase animation.')
#	theaterChase(strip, Color(127, 127, 127))  # White theater chase
#	print ('White flash animation.')
#	colorFlash(strip, Color(127, 127, 127), 5)  # White flash
#	print ('Green wipe animation.')
#	colorWipe(strip, Color(0, 255, 0))  # Green wipe
##        inkey = input("Press any key to quit.")
#	print ('Black wipe animation.')
#	colorWipe(strip, Color(0, 0, 0))    # Blackwipe
##	sys.exit()
#	print ('Green All.')
#	colorAll(strip, Color(0, 255, 0))  # Green wipe
#	print ('Black All.')
#	colorAll(strip, Color(0, 0, 0))    # Blackwipe

