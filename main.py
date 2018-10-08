"""
Demo program demonstrating the capabities of the MicroPython display module
Author:	LoBo (https://github/loboris)
Date:	08/10/2017

"""

import machine
import display
import time
import ubinascii
from machine import UART, Pin, random, TouchPad


#define tft
tft = display.TFT()
tft.init(tft.ST7735R, speed=10000000, spihost=tft.HSPI, mosi=23, miso=19, clk=18, cs=26, dc=17, rst_pin=16,
         backl_pin=13, hastouch=False, bgr=True, width=128, height=128, backl_on=1, rot=tft.PORTRAIT_FLIP, splash=False)
#define touchpad
touch1 = TouchPad(Pin(4))
touch1.config(300)

#DHT11
def get_room_temp():
    dht = machine.DHT(machine.Pin(5), machine.DHT.DHT11)
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

#display result
def show():
    tft.clear()

    r1 = get_room_temp()
    #r2 = get_hcho()
    #r1 = 45,78
    r2 = 30
    temperature = 'TEMP:' + str(r1[0])+ '°C'
    humidity = 'HUM:' + str(r1[1])+ '%RH'
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