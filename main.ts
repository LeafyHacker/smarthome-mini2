let humidity = 0
let temp_raum = 0
let drunter2 = 0
let g_temp = 26
let drunter_alt = 0
DHT11.setPin(DigitalPin.P2)
neZha.setMotorSpeed(neZha.MotorList.M4, 0)
let led1 = PlanetX_Display.create(PlanetX_Display.DigitalRJPin.J3, 12, PlanetX_Display.NeoPixelMode.RGB)
let led2 = PlanetX_Display.create(PlanetX_Display.DigitalRJPin.J4, 12, PlanetX_Display.NeoPixelMode.RGB)
basic.showNumber(1)
function pumpe() {
    
    drunter2 = g_temp - temp_raum
    if (Math.trunc(g_temp) == temp_raum) {
        neZha.setMotorSpeed(neZha.MotorList.M4, 0)
    } else if (drunter2 >= 1) {
        neZha.setMotorSpeed(neZha.MotorList.M4, 50)
    } else if (drunter2 >= 3) {
        neZha.setMotorSpeed(neZha.MotorList.M4, 100)
    } else if (drunter2 <= -1) {
        neZha.setMotorSpeed(neZha.MotorList.M4, -50)
    } else if (drunter2 <= -3) {
        neZha.setMotorSpeed(neZha.MotorList.M4, -100)
    }
    
}

function leds() {
    
    
    //  drunter_alt = drunter
    //  drunter = 3
    //  drunter = g_temp - temp_raum
    if (drunter2 != drunter_alt) {
        if (drunter2 == 0) {
            led1.showColor(PlanetX_Display.colors(PlanetX_Display.NeoPixelColors.Green))
            led1.show()
            led2.showColor(PlanetX_Display.colors(PlanetX_Display.NeoPixelColors.Green))
            led2.show()
        }
        
        if (drunter2 > 0) {
            led1.showRainbow(330, 400)
            led2.clear()
            led2.show()
        }
        
        if (drunter2 < 0) {
            led2.showRainbow(200, 300)
            led1.clear()
            led1.show()
        }
        
    }
    
    if (drunter2 >= 1) {
        led1.rotate(1)
        led1.show()
        basic.showArrow(ArrowNames.East, 0)
    }
    
    if (drunter2 < 0) {
        led2.rotate(-1)
        led2.show()
        basic.showArrow(ArrowNames.West, 0)
    }
    
    drunter_alt = drunter2
}

basic.forever(function on_forever() {
    
    humidity = DHT11.humidity()
    temp_raum = DHT11.temperature()
    PlanetX_Display.showUserText(1, "Raumtemperatur:")
    PlanetX_Display.showUserNumber(3, temp_raum)
    PlanetX_Display.showUserText(5, "Luftfeuchtigkeit:")
    PlanetX_Display.showUserNumber(8, humidity)
    pumpe()
})
basic.forever(function on_forever2() {
    leds()
    basic.pause(100)
})
