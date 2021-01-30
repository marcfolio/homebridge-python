import sys
import RPi.GPIO as GPIO ## Import GPIO library

gpio_num = int(sys.argv[1])
gpio_str = sys.argv[1]
cmd_str = sys.argv[2]
GPIO.setmode(GPIO.BCM) ## Use board pin numbering

GPIO.setup(gpio_num, GPIO.OUT)
relay_state = GPIO.input(gpio_num)
GPIO.output(gpio_num, not relay_state)
file_path = "scripts/" + gpio_str + ".txt"
new_file = open(file_path,'w')

if cmd_str == "true":
        new_file.write("ON")
        print("ON")
else:
        new_file.write("OFF")
        print("OFF")

new_file.close()




