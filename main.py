# Nicholas Qvick
# INTKM26A2 
# Raspberry pico W main.py file
from focar import pysaytys
from focar import eteenpain
from focar import kaanny
from focar import taaksepain

# Eteenpäin 3sekuntia
eteenpain(aika=3)
# Pysäytys
pysaytys(aika=1)
# 45 asteen kääntö ja eteenpäin sekuntti
kaanny(suunta="vasen", aika=2)
eteenpain(aika=1)
# pysäytys
pysaytys(aika=1)
# kääntö 45 astetta ja taaksepäin
kaanny(suunta="vasen", aika=2)
taaksepain(aika=1.5)
# Pysäytys
pysaytys(aika=1)
# kääntö 90 astetta ja eteenpäin 3 sekunttia
kaanny(suunta="vasen", aika=4)
eteenpain(aika=3)
# Lopetus
pysaytys(aika=1)



