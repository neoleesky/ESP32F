"""
Neo's EPS32F kit use for GPS
Author:	Neo Lee
Date:	08/10/2017
# Used Pin 13,16,17,18,19,23,26 for display
# USed Pin 4 for touch1
# Used Pin  0, 22 for Uart2 GPS
# Used Pin 27,2 for UART1 GSM
"""

import display
import time
import gsm
from machine import UART, Pin, random, TouchPad
import ujson as json
import urequests
import time
#import ntptime
import machine
import utime


#onenet api配置
api_url='http://api.heclouds.com'
api_key='LAWZJ=Rs=NE2Ghj=lN==BgSQ7w0=' #请填入专属的api key
api_headers={'api-key':api_key,'content-type': 'application/json'}
device_id=46814719

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
# #uart = UART(2, rx=0, tx=22, baudrate=9600, bits=8, parity=None, stop=1, timeout=1500, buffer_size=1024,
#                    lineend='\r\n')
gsm.start(tx=27, rx=21, apn='ctnet', connect = True)

#gps = GPS(uart)


#display result
#def show():
    # tft.clear()
    # gps.startservice()
    # r = gps.getdata()
    # latitude = 'La:' + str(r[1])+ ' N'
    # longitude = 'Lo:' + str(r[2])+ ' E'
    # altitude = 'Al:' + str(r[3])+ ' M'
    # tft.text(5, 20, latitude, tft.WHITE)
    # tft.text(5, 40, longitude,tft.BLUE)
    # tft.text(5, 60, altitude,tft.RED)
#
# def upload_onenet():
#     url=r'%s/devices/%s/datapoints?type=4' % (api_url,device_id)
#     strftime= "%04u-%02u-%02uT%02u:%02u:%02u" % time.localtime()[0:6]
#     print ("time:",strftime)
#     l = gps.getdata()
#     lon = str(l[1])
#     lat = str(l[2])
#     data={"lon":{strftime:lon},"lat":{strftime:lat}}
#     print (json.dumps(data))
#     res = urequests.post(url,headers=api_headers,data=json.dumps(data))
#     print ("status_code:",res.status_code)


# def main():
#     while True:
#         show()
#         upload_onenet()
#         time.sleep(10)
#
#
# if __name__ == '__main__':
#     main()

try:
    ntptime.settime()
except:
    pass
rtc = machine.RTC()
# for time convert to second
tampon1 = utime.time()
# for gmt. For me gmt+3.
# 1 hour = 3600 seconds
# 3 hours = 10800 seconds
tampon2 = tampon1 + 28800
# for second to convert time
(year, month, mday, hour, minute, second, weekday, yearday) = utime.localtime(tampon2)
# first 0 = week of year
# second 0 = milisecond
rtc.datetime((year, month, mday, 0, hour, minute, second, 0))