# Nicholas Qvick
# INTKM26A2 
# FoCar test main file
#

# focar:in tarvitsemat kirjastot
from machine import Pin, PWM
from time import sleep


# Moottori A
e1 = PWM(Pin(28))
m1 = Pin(27, Pin.OUT)

# Moottori B
e2 = PWM(Pin(26))
m2 = Pin(22, Pin.OUT)

# Aseta PWM-taajuus 1000 Hz
e1.freq(1000)
e2.freq(1000)

# Funkito ledille
def led():
     # otetaan led olio käyttöön
     led = Pin("LED", Pin.OUT)
     # while true loopilla vilkutetaan lediä
     while True:
        #1 lyhyt
        led.on()
        sleep(1) 
        led.off()
        sleep(1)
        #2 lyhyt
        led.on()
        sleep(1) 
        led.off()
        sleep(1)
        #3 lyhyt
        led.on()
        sleep(1) 
        led.off()
        sleep(1)
        #1 pitkä
        led.on()
        sleep(3) 
        led.off()
        sleep(3)
        #2 pitkä
        led.on()
        sleep(3) 
        led.off()
        sleep(3)
        #3 pitkä
        led.on()
        sleep(3) 
        led.off()
        sleep(3)

# Moottoreiden pysäytys funktio
def pysaytys(aika):
    e1.duty_u16(0)
    e2.duty_u16(0)
    sleep(aika)

# Funktio eteenpäin menemiselle
def eteenpain(aika): 
    m1.value(1)
    m2.value(1)
    # 75% Nopeus 
    e1.duty_u16(49181)
    e2.duty_u16(49181)
    sleep(aika)

# Funktio paruuttamiselle
def taaksepain(aika):
    m1.value(0)
    m2.value(0)
    # 75% Nopeus
    e1.duty_u16(49181)
    e2.duty_u16(49181)
    sleep(aika)

# Kääntymisen funktio
# 5 sekuntia riittää 90 asteen käännökselle laminaatilla vasemmalle,
# mutta toinen moottori hieman huonompi kun toinen niin antaa sekuntti enemmän aikaa,
# että päästään 90 astetta oikealle
# HUOM! Ladattavilla akku paristoilla korkeampi V joten vaatii vähemmän aikaa
# kääntyä kuin piuhalla
def kaanny(suunta, aika):
    # Suunta vasemmalle
    if(suunta == "vasen"):
        m1.value(1)
        # Toinen moottori taaksepäin
        m2.value(0)
         # Nopeus 50%
        e1.duty_u16(32767)
        # Nopeus 50%
        e2.duty_u16(32767)  
        # Kääntymisen kesto
        sleep(aika)
    # Vaihtoehtoinen suunta (Todennäköisesti oikealle)
    else:
        # Toinen moottori taaksepäin
        m1.value(0)
        m2.value(1)
        # Nopeus 50%
        e1.duty_u16(32767)
        # Nopeus 50% 
        e2.duty_u16(32767) 
        # Kääntymisen kesto
        sleep(aika)

# U-käännökselle funktio
def U(aika):
        # Toinen moottori taaksepäin
        m1.value(0)
        m2.value(1)
        # Nopeus 50%
        e1.duty_u16(32767)
        # Nopeus 50% 
        e2.duty_u16(32767) 
        # Kääntymisen kesto
        sleep(aika)
