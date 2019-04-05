# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> parent of 96a54ad... Dev
=======
#hello tecent
>>>>>>> 96a54ad87c10098567ebab102d8b4b91bfc15614
import gc
import network
import time
#import ntptime
import machine
import utime
import gsm

#
# ap = network.WLAN(network.AP_IF) # create access-point interface
# ap.config(essid='ESP32F') # set the ESSID of the access point
# ap.active(True)         # activate the interface


#gsm.start(tx=27, rx=21, apn='ctnet', connect = True)
gsm.start(tx=27, rx=21, apn='ctnet')

# wlan = network.WLAN(network.STA_IF)
# wlan.active(True)
# #time.sleep(2)
# wlan.connect('XiaoPiDan', 'asdfzxcv123')
# time.sleep(3)
# if wlan.isconnected() == True:
#     print('alread connect')
# else:
#     wlan.connect('ZMI_E9C0', '63254450')
#     time.sleep(3)

#set time
rtc = machine.RTC()
rtc.ntp_sync(server="hr.pool.ntp.org", tz="CCT-8")
rtc.synced()
utime.gmtime()
print("Time set:", utime.strftime("%c"))
# try:
#     ntptime.settime()
# except:
#     pass
# rtc = machine.RTC()
# # for time convert to second
# tampon1 = utime.time()
# # for gmt. For me gmt+3.
# # 1 hour = 3600 seconds
# # 3 hours = 10800 seconds
# tampon2 = tampon1 + 28800
# # for second to convert time
# (year, month, mday, hour, minute, second, weekday, yearday) = utime.localtime(tampon2)
# # first 0 = week of year
# # second 0 = milisecond
# rtc.datetime((year, month, mday, 0, hour, minute, second, 0))



#webrepl
#webrepl.start()


#gc
gc.collect()
