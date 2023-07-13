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


#If you want to modify the environment parameters, you can do so
#elativeHumidity(0-100%RH)  temperature(-10~50 centigrade)
#sgp40.set_envparams(relative_humidity = 50,temperature_c = 25)

while True:
    # get raw vlaue
    print ('Raw vlaue : %d'%(sgp40.measure_raw()))
    time.sleep(1)