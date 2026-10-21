# Nicholas Qvick
# INTKM26A2 
# FoCar test main file
#

# Tehot
# 25% = 16383
# 30% = 19660 
# 40% = 26214
# 50% = 32767
# 60% = 39321
# 75% = 49181
# 100 = 65535

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

# Led olio
led = Pin("LED", Pin.OUT)

# Moottoreiden pysäytys funktio
def pysaytys(aika):
    e1.duty_u16(0)
    e2.duty_u16(0)
    sleep(aika)

# Funktio eteenpäin menemiselle
def eteenpain(aika): 
    # LED päälle kun liikutaan
    led.on()
    # Moottorit eteenpäin
    m1.value(1)
    m2.value(1)
    # 75% Nopeus 
    e1.duty_u16(49181)
    e2.duty_u16(49181)
    # Kesto
    sleep(aika)
    # LED kiinni kun funktio on valmis
    led.off()

# Funktio paruuttamiselle
def taaksepain(aika):
    # LED päälle kun liikutaan
    led.on()
    # Moottorit eteenpäin
    m1.value(0)
    m2.value(0)
    # 75% Nopeus
    e1.duty_u16(49181)
    e2.duty_u16(49181)
    # Kesto
    sleep(aika)
    # LED kiinni kun funktio on valmis
    led.off()

# Kääntymisen funktio
# 5 sekuntia riittää 90 asteen käännökselle laminaatilla vasemmalle,
# mutta toinen moottori hieman huonompi kun toinen niin antaa sekuntti enemmän aikaa,
# että päästään 90 astetta oikealle
# HUOM! Ladattavilla akku paristoilla korkeampi V joten vaatii vähemmän aikaa
# kääntyä kuin piuhalla
def kaanny(suunta, aika):
    # Suunta vasemmalle
    if(suunta == "vasen"):
        # LED päälle kun liikutaan
        led.on()
        m1.value(1)
        # Toinen moottori taaksepäin
        m2.value(0)
         # Nopeus 50%
        e1.duty_u16(32767)
        # Nopeus 50%
        e2.duty_u16(32767)  
        # Kääntymisen kesto
        sleep(aika)
        # LED kiinni kun funktio on valmis
        led.off()
    # Vaihtoehtoinen suunta (Todennäköisesti oikealle)
    else:
        # LED päälle kun liikutaan
        led.on()
        # Toinen moottori taaksepäin
        m1.value(0)
        m2.value(1)
        # Nopeus 50%
        e1.duty_u16(32767)
        # Nopeus 50% 
        e2.duty_u16(32767) 
        # Kääntymisen kesto
        sleep(aika)
        # LED kiinni kun funktio on valmis
        led.off()

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

# Loppu
