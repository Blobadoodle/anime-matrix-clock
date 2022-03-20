from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from os import system
import signal
import sys

import time
from datetime import datetime

from pynput import keyboard

fontname   = "Hack-Regular.ttf"
fontsize   = 16
width      = 64
height     = 36
filename   = "time.gif"
command    = "asusctl anime pixel-gif -p time.gif"
textcolour = (255, 255, 255)
timeformat = "%H:%M"
mode       = "RGB"
keybind    = 269025089


font = ImageFont.truetype(fontname, fontsize)
W,H = (width, height)

active = True

def main():
    now = datetime.now()
    strtime = now.strftime(timeformat)

    img = Image.new(mode, (width, height))
    draw = ImageDraw.Draw(img)

    w,h = draw.textsize(strtime, font=font)
    draw.text(((W-w)/2, (H-h)/1.1), strtime, textcolour,font=font)

    img.save(filename)

    system(command)

def cleanup(signal, frame):
    system("asusctl anime -e false")
    sys.exit(0)

def on_press(key):
    try:
        vk = key.vk
    except AttributeError:
        vk = key.value.vk
    if vk == keybind:
        global active
        active = not active
        if active:
            system("asusctl anime -e true")
            main()
        else:
            system("asusctl anime -e false")

if __name__ == "__main__":
    system("asusctl anime -e true")
    signal.signal(signal.SIGINT, cleanup)
    listener = keyboard.Listener(
        on_press=on_press
    )
    listener.start()
    while True:
        if active :
            main()
        time.sleep(60 - time.time() % 60)
