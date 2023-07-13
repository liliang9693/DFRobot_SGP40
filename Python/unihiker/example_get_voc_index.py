#coding:utf-8
'''
    @DFRobot SEN0394
    @Gravity: SGP40 Air Quality Sensor
    @https://www.dfrobot.com/product-2251.html
    @This code runs on unihiker
'''

import time
from DFRobot_SGP40 import DFRobot_SGP40
from pinpong.board import Board

Board().begin()
#set IICbus elativeHumidity(0-100%RH)  temperature(-10~50 centigrade)
sgp40=DFRobot_SGP40(relative_humidity = 50,temperature_c = 25)

#set Warm-up time
print ('Please wait 10 seconds...')
sgp40.begin(10)

#If you want to modify the environment parameters, you can do so
#elativeHumidity(0-100%RH)  temperature(-10~50 centigrade)
#sgp40.set_envparams(50,-2)

while True:
    print ('Voc index : %d'%(sgp40.get_voc_index()))
    time.sleep(1)