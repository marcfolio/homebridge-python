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
# Create differential input between channel 0 and 1
# chan = AnalogIn(ads, ADS.P0, ADS.P1)

print("{:>5}\t{:>5}".format("raw", "v"))



while True:
    # print("{:>5}\t{:>5.3f}".format(chan.value, chan.voltage))
    # print("a1 = ", a1.value, a1.voltage)
 

    # Read all the ADC channel values in a list.
    # values = a0.value-20848
    # if values>0:
    # 	print("Device is On", values)
    # else:
    #     print("Device is OFF", values)

    print("a0 = ", a0.value, a0.voltage)
    time.sleep(0.5)