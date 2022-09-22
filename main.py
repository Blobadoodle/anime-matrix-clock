from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from os import system
import signal
import sys

import time
from datetime import datetime

from pynput import keyboard

# CONFIG

fontname   = "Hack-Regular.ttf" # Font (must be in same directory)
fontsize   = 16  # Font size
width      = 64 # Image size
height     = 36
filename   = "time.gif" # Filename of image output
command    = "asusctl anime pixel-gif -p time.gif" # Command to be run every minute. Make sure the -p is the same as the filename. Put all your fine tweaking here.
textcolour = (255, 255, 255) # Text colour
timeformat = "%H:%M" # TODO: if you add %S it will still update every minute not second
mode       = "RGB"
keybind    = 269025089 # XF86Launch3

# END CONFIG

font = ImageFont.truetype(fontname, fontsize) # Register font
W,H = (width, height)

active = True

def main():
	now = datetime.now() # Get the current time
	strtime = now.strftime(timeformat) # Get time string

	img = Image.new(mode, (width, height)) # Create new image
	draw = ImageDraw.Draw(img)

	w,h = draw.textsize(strtime, font=font) # Get size of text so we can center it
	draw.text(((W-w)/2, (H-h)/1.1), strtime, textcolour,font=font) # Draw the text in the center

	img.save(filename)

	system(command) # Update matrix

def cleanup(signal, frame):
	system("asusctl anime -e false") # Turn off matrix on sigint
	sys.exit(0)

def on_press(key):
	try: # Get keycode
		vk = key.vk
	except AttributeError:
		vk = key.value.vk
	if vk == keybind:
		global active
		active = not active # Invert active state
		if active:
			system("asusctl anime -e true") # Enable display
			main() # Update display
		else:
			system("asusctl anime -e false") # Disable display

if __name__ == "__main__":
	system("asusctl anime -e true") # Enable display
	signal.signal(signal.SIGINT, cleanup) # Register SIGINT handler
	listener = keyboard.Listener( # Register keyboard listener
		on_press=on_press
	)
	listener.start()
	while True:
		if active :
			main()
		time.sleep(60 - time.time() % 60) # Run at the start of every second
