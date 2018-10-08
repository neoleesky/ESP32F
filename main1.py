"""
# MicroPython ST7735 TFT display driver example usage
# Used Pin 13,16,17,18,19,23,26 for display
# Used Pin 5 for dht
# USed Pin 4 for touch1
# Used Pin 27,32,33 for LED
# Used Pin  0, 22 for Uart
"""
from machine import Pin, SPI, TouchPad
from tft import TFT_GREEN
from font import terminalfont
import dht
import time
import ubinascii
import urequests as requests
from machine import UART


#define UART
uart = UART(2, baudrate=9600, bits=8, parity=None, stop=1,rx=0, tx=22, timeout=1000)

#define TFT
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

#define touchpad
touch1 = TouchPad(Pin(4))
touch1.config(300)

#define RGB
R = Pin(27, Pin.OUT, None)
G = Pin(32, Pin.OUT, None)
B = Pin(33, Pin.OUT, None)


def get_room_temp():
    d = dht.DHT11(Pin(5))
    d.measure()
    return  d.temperature(),d.humidity()

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


def display():
    # init TFT
    tft.init()
    # start using the driver
    tft.clear(tft.rgbcolor(255, 255, 255))
    r1 = get_room_temp()
    r2 = get_hcho()
    temperature = 'TEMP:' + str(r1[0])
    humidity = 'Hum:' + str(r1[1])
    hcho = 'HCHO:' + str(r2)
    tft.text(5, 50, temperature, terminalfont, tft.rgbcolor(0, 255, 0), 2)
    tft.text(5, 70, humidity, terminalfont, tft.rgbcolor(255, 255, 0), 2)
    tft.text(5, 90, hcho, terminalfont, tft.rgbcolor(255, 255, 0), 2)

def main():
    while True:
        display()
        time.sleep(5)
    # R.value(1)
    # G.value(1)
    # B.value(1)
    # while True:
    #     if touch1.read() < 50 :
    #         print(touch1.read())
    #         display()
    #     else:
    #         print(touch1.read())


        #upload_wx()
        #show_temp()
        #休眠60秒


if __name__ == '__main__':
    main()

# tft.hline(5,5,10,tft.rgbcolor(123,23,33))
#
#
# time.sleep(5)
#
# show = "HCHO: 70%"
# temp = 'TEMP: 26C'
# tft.char(10,10,'A',terminalfont,tft.rgbcolor(255,0,0),2,2)
# tft.text(10,30,show,terminalfont,tft.rgbcolor(0,255,0),2)
# tft.text(1,50,temp,terminalfont,tft.rgbcolor(0,0,0),2)
#for i in range(128):
   #  tft.line(0, i, 127, 127-i, tft.rgbcolor(2*i, 124, 2*i))
    # tft.line(i, 0, 127-i, 127, tft.rgbcolor(0, 2*i, 0))