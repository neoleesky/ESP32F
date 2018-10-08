# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import gc
import webrepl
import network
import time
import ntptime
import machine
import utime


#set wlan
ap = network.WLAN(network.AP_IF)
ap.active(True)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('XiaoPiDan', 'asdfzxcv123')
#time.sleep(3)
if wlan.isconnected() == True:
    print('alread connect')
else:
    wlan.connect('ZMI_E9C0', '63254450')
#    time.sleep(3)

#set time
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



#webrepl
webrepl.start()


#gc
gc.collect()
