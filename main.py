humidity = 0
temp_raum = 0
g_temp = 40
DHT11.set_pin(DigitalPin.P2)
neZha.set_motor_speed(neZha.MotorList.M4, 0)
led1 = PlanetX_Display.create(PlanetX_Display.DigitalRJPin.J3, 12, PlanetX_Display.NeoPixelMode.RGB)
led2 = PlanetX_Display.create(PlanetX_Display.DigitalRJPin.J4, 12, PlanetX_Display.NeoPixelMode.RGB)

def on_forever():
    global temp_raum
    global humidity
    humidity = DHT11.humidity()
    temp_raum = DHT11.temperature()
    PlanetX_Display.show_user_text(1, "Raumtemperatur:")
    PlanetX_Display.show_user_number(3, temp_raum)
    PlanetX_Display.show_user_text(5, "Luftfeuchtigkeit:")
    PlanetX_Display.show_user_number(8, humidity)
    pumpe()
    ledv()
basic.forever(on_forever)

def pumpe():
    drunter = g_temp - temp_raum
    if int(g_temp) == temp_raum:
        neZha.set_motor_speed(neZha.MotorList.M4, 0)
    elif drunter >= 3:
        neZha.set_motor_speed(neZha.MotorList.M4, 50)
    elif drunter >= 5:
        neZha.set_motor_speed(neZha.MotorList.M4, 100)
    elif drunter <= -1:
        neZha.set_motor_speed(neZha.MotorList.M4, -50)
    elif drunter <= -3:
        neZha.set_motor_speed(neZha.MotorList.M4, -100)

def ledv():
    drunter = g_temp - temp_raum
    if drunter == 0:
        led1.clear()
        led2.clear()
    if drunter >= 1:
        led2.clear()
        led1.rotate(1)
        led1.show_rainbow(1, 360)
    if drunter < 0:
        led1.clear()
        led2.rotate(1)
        led2.show_rainbow(1, 360)