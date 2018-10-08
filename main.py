"""
Neo's EPS32F kit
Author:	Neo Lee
Date:	08/10/2017
# Used Pin 13,16,17,18,19,23,26 for display
# Used Pin 5 for dht
# USed Pin 4 for touch1
# Used Pin 27,32,33 for LED
# Used Pin  0, 22 for Uart2 hcho
# Used Pin ?? ?? for UART1 GPS
"""

import display
import time
import ubinascii
from machine import UART, Pin, random, TouchPad, DHT, GPS


#define tft
tft = display.TFT()

tft.init(tft.ST7735R, speed=10000000, spihost=tft.HSPI, mosi=23, miso=19, clk=18, cs=26, dc=17, rst_pin=16,
         backl_pin=13, hastouch=False, bgr=True, width=128, height=128, backl_on=1, rot=tft.PORTRAIT_FLIP, splash=False)
tft.font(tft.FONT_Ubuntu)
#define touchpad
touch1 = TouchPad(Pin(4))
touch1.config(300)

#define UART of hcho
uart = UART(2, baudrate=9600, bits=8, parity=None, stop=1,rx=0, tx=22, timeout=1000)
#define UART of GPS
#ugps = UART(1, rx=27, tx=21, baudrate=9600, bits=8, parity=None, stop=1, timeout=1500, buffer_size=1024,
#                    lineend='\r\n')


#DHT11
def get_dht():
    dht = DHT(Pin(5), DHT.DHT11)
    (success, temperature, humidity) = dht.read()
    return  temperature, humidity

#HCHO
def get_hcho():
    a = 'ff0178410000000046'
    b = 'ff0186000000000079'
    a_bytes = ubinascii.unhexlify(a)  # 传感器改问答式
    b_bytes = ubinascii.unhexlify(b)  # 询问数值
    print(a_bytes)
    print(b_bytes)
    uart.write(b'\xff\x01xA\x00\x00\x00\x00F')
    # utime.sleep_ms(1000)
    uart.write(b'\xff\x01\x86\x00\x00\x00\x00\x00y')
    if uart.any():
        q = uart.read(9)
        #q= uart.readall()
        print('q')
        print(q)#获取9个数值
        qq = ubinascii.hexlify(q)
        print('qq')#16转str
        print (qq)
    #数值切片
        g = qq[4:6]
        d = qq[6:8]
    #16转10
        gg = int(g,16)
        dd = int(d,16)
        print (g)
        print (d)
        print (gg)
        print (dd)
    #计算最终值
        r = gg*256 + dd

        print ('result =' + str(r))
        return r

#GPS
#def ggps():




#display result
def show():
    tft.clear()
    r1 = get_dht()
    #r2 = get_hcho()
    #r1 = 45,78
    r2 = 30
    temperature = 'TEMP:' + str(r1[0])+ ' °C'
    humidity = 'HUM:' + str(r1[1])+ ' %RH'
    hcho = 'HCHO:' + str(r2)
    tft.text(5, 50, temperature, tft.WHITE)
    tft.text(5, 70, humidity,tft.BLUE)
    tft.text(5, 90, hcho,tft.RED)


def main():
    while True:
        show()
        time.sleep(5)
    # while True:
    #     if touch1.read() < 50 :
    #         print(touch1.read())
    #         show()
    #     else:
    #         print(touch1.read())

if __name__ == '__main__':
    main()