# Nicholas Qvick
# INTKM26A2 
# Raspberry pico W main.py file
from focar import pysaytys
from focar import eteenpain
from focar import kaanny
from focar import taaksepain
"""
# Eteenpäin 3sekuntia
eteenpain(aika=1.5)
# Pysäytys
pysaytys(aika=1)

kaanny(suunta="oikea", aika=0.7)
eteenpain(aika=1.9) # 2 liian pitkä, 1,5 liian vähän
# pysäytys
pysaytys(aika=1)

kaanny(suunta="vasen", aika=0.5) # 0.75
# pysäytys
pysaytys(aika=1)
eteenpain(aika=1.9) #2 liian pitkä,  1,5 liian vähän
# Pysäytys
pysaytys(aika=1)
# kääntö 90 astetta ja eteenpäin 3 sekunttia
kaanny(suunta="vasen", aika=1)
eteenpain(aika=2) # 1,5
# Lopetus
pysaytys(aika=1)

kaanny(suunta="vasen", aika=1)

pysaytys(aika=1)
eteenpain(aika=6)
pysaytys(aika=1)
kaanny(suunta="oikea", aika=1)

pysaytys(aika=1)
eteenpain(aika=2)
pysaytys(aika=1)
"""
# 1
eteenpain(aika=3.65)

kaanny(suunta="oikea", aika=0.9)
# 2
eteenpain(aika=2.65)

kaanny(suunta="oikea", aika=0.9)
# 3
eteenpain(aika=3.65)

kaanny(suunta="oikea", aika=1.2)
# 4
eteenpain(aika=2.65)

kaanny(suunta="oikea", aika=0.9)
pysaytys(aika=1)

eteenpain(aika=3)

