# Smart Recycling Bin using ESP32

An intelligent recycling bin built using ESP32 that detects metal cans, automatically opens using a servo motor, tracks bin fill percentage using an ultrasonic sensor, and displays information on an LCD screen.

---

## Features

* Metal detection system
* Automatic servo-controlled lid
* Ultrasonic fill-level monitoring
* LCD status display
* Persistent can counting using JSON storage
* LED and buzzer feedback system

---

## Hardware Used

* ESP32
* SG90 Servo Motor
* Metal Sensor
* HC-SR04 Ultrasonic Sensor
* I2C LCD Display
* Buzzer
* LEDs
* External power supply

---

## How It Works

1. The metal sensor detects a metal can.
2. The servo motor opens the bin lid automatically.
3. The buzzer and LED provide feedback.
4. The can counter increases and is saved locally.
5. The ultrasonic sensor measures the bin fill percentage.
6. The LCD displays:

   * Bin fill percentage
   * Total cans collected

---

## Project Structure

```text
smart-bin-esp32/
│
├── main.py
├── lcd_api.py
├── i2c_lcd.py
├── README.md
├── LICENSE
│
├── images/
│
└── docs/
```

---

## Future Improvements

* WiFi monitoring dashboard
* Mobile application
* AI waste classification
* Solar-powered system
* Cloud data tracking

---

## Custom 3D Printed Parts

This project also includes custom-designed 3D printed components to improve the mechanical system and overall design.

### 3D Printed Components

* A cylindrical intake tunnel that guides cans into the bin
* A servo-attached lid mechanism for automatic opening and closing

These parts were designed and printed specifically for this project to create a cleaner and more reliable recycling system.

---
## Project Background

This project was developed between the end of 2024 and the beginning of 2025 as an embedded systems and hardware engineering project.

The project was later presented at the Third Governance Conference at Northern Technical University in Mosul on February 10, 2026.

This project was originally built as an earlier hardware and embedded systems project and was later cleaned, documented, and uploaded to GitHub as part of my engineering portfolio.


## Author

Tareq Al-Dabbagh
