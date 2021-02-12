# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
import time
import board
import busio
i2c = busio.I2C(board.SCL, board.SDA)
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
ads = ADS.ADS1115(i2c)

# Create single-ended input on channel 0
a0 = AnalogIn(ads, ADS.P0)
a1 = AnalogIn(ads, ADS.P1)



a0values = [0]*100
a1values = [0]*100
while True:
    for i in range(100):
        a0values[i] = a0.value - 20848
        a1values[i] = a1.value -20848

    # a0 exterior light off && interior light off
    if max(a0values) >= 16 and max(a0values) <= 0:
    	print("ext OFF", max(a0values), a0.voltage)
    elif max(a0values) >= 240 and max(a0values) <= 272:
    	print("ext OFF", max(a0values), a0.voltage)
    elif max(a0values) == -64:
    	print("ext ON", max(a0values), a0.voltage)
    elif max(a0values) <= 192 and max(a0values) >= 176:
    	print("ext ON", max(a0values), a0.voltage)

	# if max(a1values) >= 16 and max(a1values) <= 0:
 #    	print("ext OFF", max(a1values), a1.voltage)
 #    elif max(a1values) >= 240 and max(a1values) <= 272:
 #    	print("ext OFF", max(a1values), a1.voltage)
 #    elif max(a1values) == -64:
 #    	print("ext ON", max(a1values), a1.voltage)
 #    elif max(a0vlues) <= 192 and max(a1values) >= 176:
 #    	print("ext ON", max(a1values), a1.voltage)    