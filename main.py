# MicroPython ST7735 TFT display driver example usage

from machine import Pin, SPI, reset
from tft import TFT_GREEN
from font import terminalfont

# DC       - RS/DC data/command flag
# CS       - Chip Select, enable communication
# RST/RES  - Reset
dc  = Pin(17, Pin.OUT, Pin.PULL_DOWN)
cs  = Pin(26, Pin.OUT, Pin.PULL_DOWN)
rst = Pin(16, Pin.OUT, Pin.PULL_DOWN)
bl  = Pin(13, Pin.OUT, Pin.PULL_DOWN)
# SPI Bus (CLK/MOSI/MISO)
# check your port docs to see which Pins you can use
spi = SPI(1, baudrate=8000000, polarity=1, phase=0, sck=Pin(18), mosi=Pin(23), miso=Pin(19))

# TFT object, this is ST7735R green tab version
tft = TFT_GREEN(128, 128, spi, dc, cs, rst, bl)

# init TFT
tft.init()

# start using the driver
tft.clear(tft.rgbcolor(255, 255, 255))


tft.hline(5,5,10,tft.rgbcolor(123,23,33))

import time
time.sleep(5)

show = "HCHO: 70%"
temp = 'TEMP: 26C'
tft.char(10,10,'A',terminalfont,tft.rgbcolor(255,0,0),2,2)
tft.text(10,30,show,terminalfont,tft.rgbcolor(0,255,0),2)
tft.text(1,50,temp,terminalfont,tft.rgbcolor(0,0,0),2)
#for i in range(128):
   #  tft.line(0, i, 127, 127-i, tft.rgbcolor(2*i, 124, 2*i))
    # tft.line(i, 0, 127-i, 127, tft.rgbcolor(0, 2*i, 0))