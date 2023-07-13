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


from unihiker import GUI


u_gui=GUI()

title = u_gui.draw_text(origin="bottom",text="VOC:",x=120,y=120,font_size=16, color="#0000FF")
txt_voc = u_gui.draw_text(origin="top",text="",x=120,y=120,font_size=30, color="#0000FF")

sgp40=DFRobot_SGP40(relative_humidity = 50,temperature_c = 25)

title.config(text="Please wait 10 seconds...")
sgp40.begin(10)
title.config(text="VOC:")

while True:
    txt_voc.config(text=str(sgp40.get_voc_index()))
    time.sleep(1)

