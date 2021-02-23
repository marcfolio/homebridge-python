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
while True:
	print("ext: ", a0.value - 20848)

# # print("int: ", a1.value)
# for i in range(50):
# 	a0values[i] = a0.value - 20848
# 	a1values[i] = a1.value -20848

# 	# INT OFF / EXT OFF
# 	if max(a0values) == -16:
# 		print("ext OFF", max(a0values), a0.voltage)
# 	elif max(a0values) == 0:
# 		print("ext OFF", max(a0values), a0.voltage)

# 	# INT OFF / EXT ON
# 	elif max(a0values) == -64:
# 		print("ext ON", max(a0values), a0.voltage)
# 	elif max(a0values) == -80:
# 		print("ext ON", max(a0values), a0.voltage)
# 	elif max(a0values) == -96:
# 		print("ext ON", max(a0values), a0.voltage)
# 	elif max(a0values) == -112:
# 		print("ext ON", max(a0values), a0.voltage)

# 	# INT ON / EXT OFF
# 	elif max(a0values) == 208: 
# 		print("ext OFF", max(a0values), a0.voltage)
# 	elif max(a0values) == 224:
# 		print("ext OFF", max(a0values), a0.voltage)
# 	elif max(a0values) == 240:
# 		print("ext OFF", max(a0values), a0.voltage)
# 	elif max(a0values) == 256:
# 		print("ext OFF", max(a0values), a0.voltage)

# 	# INT ON / EXT ON
# 	elif max(a0values) == 128:
# 		print("ext ON", max(a0values), a0.voltage)
# 	elif max(a0values) == 144:
# 		print("ext ON", max(a0values), a0.voltage)
# 	elif max(a0values) == 160:
# 		print("ext ON", max(a0values), a0.voltage)
# 	elif max(a0values) == 176:
# 		print("ext ON", max(a0values), a0.voltage)

	
# 	# INT ON / EXT ON
# 	if max(a1values) == 0:
# 		print("int ON", max(a1values), a1.voltage)
# 	# INT OFF / EXT ON && INT OFF / EXT OFF
# 	elif max(a1values) ==64:
# 		print("int OFF", max(a1values), a1.voltage)
# 	# INT ON / EXT OFF && # INT ON / EXT ON
# 	elif max(a1values) ==-16:
# 		print("int ON", max(a1values), a1.voltage)
# 	elif max(a1values) ==0:
# 		print("int ON", max(a1values), a1.voltage)
		


	