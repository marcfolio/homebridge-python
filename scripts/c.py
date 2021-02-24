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


a0values = [0]*100 #exterior
a1values = [0]*100 #interior

a0_state = False
a1_state = False
# while True:
# 	print("ext: ", a0.value - 20848)

# # print("int: ", a1.value)
for i in range(100):
	a0values[i] = a0.value - 20672
	a1values[i] = a1.value - 20672

print("a0: ", max(a0values))
print("a1: ", max(a1values))

# EXT OFF / INT OFF
if max(a0values) >=176 and max(a0values) <= 192:
	a0_state = False
# EXT ON / INT OFF	
elif max(a0values) == 112:
	a0_state = True
# EXT ON / INT ON	
elif max(a0values) == 352:
	a0_state = True
# EXT OFF / INT ON	
elif max(a0values) >= 416 and  max(a0values) <= 432:
	a0_state = False

print("ext: ", a0_state)

# EXT OFF / INT OFF 
if max(a1values) ==256:
	a1_state = False
# EXT ON / INT OFF
elif max(a1values) == 240:
	a1_state = False
# EXT ON / INT ON && EXT OFF / INT ON
elif max(a1values) == 176:
	a1_state = True

print("int: ", a0_state)