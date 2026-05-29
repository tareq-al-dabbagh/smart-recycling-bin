from machine import ADC, Pin, PWM, I2C, time_pulse_us
import time
import json
import os
from i2c_lcd import I2cLcd   # Make sure lcd_api.py and i2c_lcd.py are on ESP32

# --- Metal sensor setup ---
metal_sensor = ADC(Pin(15))
metal_sensor.atten(ADC.ATTN_11DB)
servo = PWM(Pin(23), freq=50)
blue_led = Pin(18, Pin.OUT)
buzzer = Pin(16, Pin.OUT)

# --- Path setup --- #
filename = "cans.json"

if filename in os.listdir():
    with open (filename , "r") as f :
        try:
            can_numbers = json.load(f)
        except json.JSONDecodeError:
            can_numbers = 0
else:
    can_numbers = 0 

# --- Ultrasonic sensor setup ---
TRIG = Pin(5, Pin.OUT)
ECHO = Pin(13, Pin.IN)
BIN_HEIGHT = 80  # cm

# --- LCD setup ---
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
lcd = I2cLcd(i2c, 0x27, 2, 16)  # adjust 0x27 if needed

# --- Functions ---
def read_metal():
    s = 0
    for _ in range(10):
        s += metal_sensor.read()
        time.sleep_ms(5)
    return s // 10

def get_distance():
    TRIG.value(0)
    time.sleep_us(2)
    TRIG.value(1)
    time.sleep_us(10)
    TRIG.value(0)
    duration = time_pulse_us(ECHO, 1, 30000)
    return (duration * 0.0343) / 2  # distance in cm

def set_servo_angle(angle):
    duty = int(22 + (angle / 180 ) * 120)
    servo.duty(duty)
    
def get_fill_percentage():
    d = get_distance()
    filled = BIN_HEIGHT - d
    return (filled / BIN_HEIGHT) * 100

def saving(data):
    with open("cans.json","w") as f :
        f.write(json.dumps(data))

def can_counting():
    global can_numbers
    can_numbers += 1
    saving(can_numbers)

set_servo_angle(0)
time.sleep(0.5)

# --- Timers for 10-second update ---
last_ultrasonic_time = time.time()

while True:
    # --- Metal sensor check ---
    value = read_metal()
    if value < 1000:
        blue_led.value(1)
        set_servo_angle(145)
        buzzer.value(1)
        time.sleep(0.2)
        buzzer.value(0)
        time.sleep(0.2)
        buzzer.value(1)
        time.sleep(0.2)
        buzzer.value(0)
        time.sleep(1)
        set_servo_angle(0)
        time.sleep(0.5)
        blue_led.value(0)
        
        can_counting()

    # --- Ultrasonic sensor check every 10 seconds ---
    if time.time() - last_ultrasonic_time >= 10:
        percent = get_fill_percentage()
        lcd.clear()
        lcd.putstr("Bin Filled:"+"{:.0f}%".format(percent))
        lcd.move_to(0, 1)
        lcd.putstr("Total cans:"+ str(can_numbers))
        
        last_ultrasonic_time = time.time()

    time.sleep(0.2)
