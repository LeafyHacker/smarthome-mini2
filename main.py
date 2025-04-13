humidity = 0
temp_raum = 0
drunter2 = 0
g_temp = 26
drunter_alt = 0
DHT11.set_pin(DigitalPin.P2)
neZha.set_motor_speed(neZha.MotorList.M4, 0)
led1 = PlanetX_Display.create(PlanetX_Display.DigitalRJPin.J3, 12, PlanetX_Display.NeoPixelMode.RGB)
led2 = PlanetX_Display.create(PlanetX_Display.DigitalRJPin.J4, 12, PlanetX_Display.NeoPixelMode.RGB)
basic.show_number(1)
def pumpe():
    global drunter2
    drunter2 = g_temp - temp_raum
    if int(g_temp) == temp_raum:
        neZha.set_motor_speed(neZha.MotorList.M4, 0)
    elif drunter2 >= 1:
        neZha.set_motor_speed(neZha.MotorList.M4, 50)
    elif drunter2 >= 3:
        neZha.set_motor_speed(neZha.MotorList.M4, 100)
    elif drunter2 <= -1:
        neZha.set_motor_speed(neZha.MotorList.M4, -50)
    elif drunter2 <= -3:
        neZha.set_motor_speed(neZha.MotorList.M4, -100)
def leds():
    global drunter2
    global drunter_alt
    # drunter_alt = drunter
    # drunter = 3
    # drunter = g_temp - temp_raum
    if drunter2 != drunter_alt:
        if drunter2 == 0:
            led1.show_color(PlanetX_Display.colors(PlanetX_Display.NeoPixelColors.GREEN))
            led1.show()
            led2.show_color(PlanetX_Display.colors(PlanetX_Display.NeoPixelColors.GREEN))
            led2.show()
        if drunter2 > 0:
            led1.show_rainbow(330, 400)
            led2.clear()
            led2.show()
            
        if drunter2 < 0:
            led2.show_rainbow(200, 300)
            led1.clear()
            led1.show()
    if drunter2 >= 1:
        led1.rotate(1)
        led1.show()
        basic.show_arrow(ArrowNames.EAST, 0)
    if drunter2 < 0:
        led2.rotate(-1)
        led2.show()
        basic.show_arrow(ArrowNames.WEST, 0)
    drunter_alt = drunter2

def on_forever():
    global humidity, temp_raum
    humidity = DHT11.humidity()
    temp_raum = DHT11.temperature()
    PlanetX_Display.show_user_text(1, "Raumtemperatur:")
    PlanetX_Display.show_user_number(3, temp_raum)
    PlanetX_Display.show_user_text(5, "Luftfeuchtigkeit:")
    PlanetX_Display.show_user_number(8, humidity)
    pumpe()
basic.forever(on_forever)

def on_forever2():
    leds()
    basic.pause(100)
basic.forever(on_forever2)
