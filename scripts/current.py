# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)

# Create single-ended input on channel 0
a0 = AnalogIn(ads, ADS.P0)
a1 = AnalogIn(ads, ADS.P1)

maxnum = 20848
# Create differential input between channel 0 and 1
# chan = AnalogIn(ads, ADS.P0, ADS.P1)

# print("{:>5}\t{:>5}".format("raw", "v"))

        
# while True:
#     # print("{:>5}\t{:>5.3f}".format(chan.value, chan.voltage))
#     # print("a1 = ", a1.value, a1.voltage)

   
#     values = a0.value - 20848
    
#     if max(values)>0:
#         print("Device is True")
#         print(max(values))
#         state=True
#     else:
#         print("Device is False")
#         print(max(values))
#         state=False

#     # return state
 

#     # # Read all the ADC channel values in a list.
#     # values = a0.value - 20848
#     # if values<0:
#     # 	print("Device is On", values)
#     # else:
#     #     print("Device is OFF", values)

#     # print("a0 = ", a0.value, a0.voltage)
#     # print("a0 = ", a0.value, a0.voltage)
#     time.sleep(1)



values = [0]*100
while True:
    for i in range(100):
        #values[i] = adc.read_adc(0, gain=GAIN)   print(math.ceil(4.2))
        values[i] = a0.voltage - 2.6080795922727136

    print(max(values))

    if max(values)<0:
    	print("Divice is true")
    	print(max(values))
    else:
    	print("Divice is false")
    	print(max(values))

    # print("a1 = ", a1.value, a1.voltage)
                    
    # print("OFF")
    # #print(math.ceil(sum(values) / len(values)))
    # print(max(values))  
