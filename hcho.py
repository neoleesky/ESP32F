#!/usr/bin/env python
# -*- coding: utf-8 -*-



import ubinascii
import urequests as requests
from machine import UART

uart = UART(2, baudrate=9600, bits=8, parity=None, stop=1,rx=16, tx=17, timeout=1000)
count = 1
while True:
    print('\n\n===============CNT {}==============='.format(count))
    a = 'ff0178410000000046'
    b = 'ff0186000000000079'
    a_bytes = ubinascii.unhexlify(a)  #传感器改问答式
    b_bytes = ubinascii.unhexlify(b)  #询问数值
    print (a_bytes)
    print( b_bytes)

    uart.write(b'\xff\x01xA\x00\x00\x00\x00F')

    #utime.sleep_ms(1000)
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
        g = qq[8:10]
        d = qq[10:12]
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
    # 计数器+1
    utime.sleep_ms(1000)
    count += 1
    print('---------------------------------------')