#!/usr/bin/env python3

# Test to read any serial value send from ESP32

device = '/dev/ttyUSB0'

import serial

esp32 = serial.Serial(device, 115200)
while 1:
    print(esp32.readline().decode())
