import sys
import RPi.GPIO as GPIO ## Import GPIO library

gpio_num = int(sys.argv[1])
gpio_str = sys.argv[1]
# cmd_str = sys.argv[2]
GPIO.setmode(GPIO.BCM) ## Use board pin numbering

GPIO.setup(gpio_num, GPIO.OUT)
relay_state = GPIO.input(gpio_num)

path = 'scripts/'+gpio_str+'.txt'
state_file = open(path,'r')
last_state = state_file.read()

if last_state == "ON": #add conditional here when voltage is read
	GPIO.output(gpio_num, 1)
else:
	GPIO.output(gpio_num, 0)

print(last_state)
state_file.close()









