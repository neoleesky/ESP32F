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
import ujson as json
import urequests
<<<<<<< Updated upstream
import time
#import ntptime
import machine
import utime
from simple import MQTTClient

# #onenet api配置
# api_url='http://api.heclouds.com'
# api_key='LAWZJ=Rs=NE2Ghj=lN==BgSQ7w0=' #请填入专属的api key
# api_headers={'api-key':api_key,'content-type': 'application/json'}
# device_id=46814719

#mqtt 配置
SERVER = "183.230.40.39"
CLIENT_ID = "521190191"
TOPIC = b"ttt"
username='173816'
password='esp32f'
state = 0
=======
>>>>>>> Stashed changes


#define tft
# tft = display.TFT()
# tft.init(tft.ST7735R, speed=10000000, spihost=tft.HSPI, mosi=23, miso=19, clk=18, cs=26, dc=17, rst_pin=16,
#          backl_pin=13, hastouch=False, bgr=True, width=128, height=128, backl_on=1, rot=tft.PORTRAIT_FLIP, splash=False)
# tft.font(tft.FONT_Ubuntu)
# #define touchpad
# touch1 = TouchPad(Pin(4))
# touch1.config(300)

#define UART of hcho
#uart = UART(2, baudrate=9600, bits=8, parity=None, stop=1,rx=0, tx=22, timeout=1000)
#define UART of GPS
<<<<<<< Updated upstream
# #uart = UART(2, rx=0, tx=22, baudrate=9600, bits=8, parity=None, stop=1, timeout=1500, buffer_size=1024,
#                    lineend='\r\n')
# gsm.start(tx=27, rx=21, apn='ctnet', connect = True)
=======
uart = UART(2, rx=0, tx=22, baudrate=9600, bits=8, parity=None, stop=1, timeout=1500, buffer_size=1024,
                   lineend='\r\n')
>>>>>>> Stashed changes

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

def upload_onenet():
    url=r'%s/devices/%s/datapoints?type=4' % (api_url,device_id)
    strftime= "%04u-%02u-%02uT%02u:%02u:%02u" % time.localtime()[0:6]
    print ("time:",strftime)
    l = gps.getdata()
    lon = str(l[1])
    lat = str(l[2])
    data={"lon":{strftime:lon},"lat":{strftime:lat}}
    print (json.dumps(data))
    res = urequests.post(url,headers=api_headers,data=json.dumps(data))
    print ("status_code:",res.status_code)


def main():
    while True:
        show()
        upload_onenet()
        time.sleep(10)


<<<<<<< Updated upstream
#mqtt上传到onenet
def mqtt_onenet(server=SERVER):
    c = MQTTClient(CLIENT_ID, server, 6002, username, password)
    strftime = "%04u-%02u-%02uT%02u:%02u:%02u" % time.localtime()[0:6]
    msg1 = b'Hello #%s' % (strftime)
    c.connect()
    c.publish(b"ttt",msg1)
    c.disconnect()

def main():
    while True:
        mqtt_onenet()
        time.sleep(3)


if __name__ == '__main__':
    main()

=======
if __name__ == '__main__':
    main()
>>>>>>> Stashed changes
