"""
Neo's EPS32F kit use for GPS
Author:	Neo Lee
Date:	08/10/2017
# Used Pin 13,16,17,18,19,23,26 for display
# USed Pin 4 for touch1
# Used Pin  0, 22 for Uart2 GPS
# Used Pin ?? ?? for UART1 GPS
"""

import display
import time
from machine import UART, Pin, random, TouchPad, GPS


#define tft
tft = display.TFT()

tft.init(tft.ST7735R, speed=10000000, spihost=tft.HSPI, mosi=23, miso=19, clk=18, cs=26, dc=17, rst_pin=16,
         backl_pin=13, hastouch=False, bgr=True, width=128, height=128, backl_on=1, rot=tft.PORTRAIT_FLIP, splash=False)
tft.font(tft.FONT_Ubuntu)
#define touchpad
touch1 = TouchPad(Pin(4))
touch1.config(300)

#define UART of hcho
#uart = UART(2, baudrate=9600, bits=8, parity=None, stop=1,rx=0, tx=22, timeout=1000)
#define UART of GPS
uart = UART(2, rx=0, tx=22, baudrate=9600, bits=8, parity=None, stop=1, timeout=1500, buffer_size=1024,
                   lineend='\r\n')

gps = GPS(uart)


#display result
def show():
    tft.clear()
    gps.startservice()
    r = gps.getdata()
    latitude = 'La:' + str(r[1])+ ' N'
    longitude = 'Lo:' + str(r[2])+ ' E'
    altitude = 'Al:' + str(r[3])+ ' M'
    tft.text(5, 20, latitude, tft.WHITE)
    tft.text(5, 40, longitude,tft.BLUE)
    tft.text(5, 60, altitude,tft.RED)


def main():
    while True:
        show()
        time.sleep(5)


if __name__ == '__main__':
    main()