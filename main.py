# Nicholas Qvick
# INTKM26A2 
# Raspberry pico W main.py file
from machine import Pin
from focar import led
from focar import pysaytys
from focar import eteenpain
from focar import kaanny
from focar import taaksepain

led()

eteenpain(3)
kaanny("vasen", 5)
eteenpain(2)
kaanny("vasen", 5)
taaksepain(4)


