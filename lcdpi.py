from RPLCD import CharLCD
lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])
lcd.write_string(u'Hello world!')

from gpiozero import Buzzer

buzzer = Buzzer(15)

while True:
    buzzer.on()
    sleep(1)
    buzzer.off()
    sleep(1)