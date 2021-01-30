import sys

gpio_str = sys.argv[1]

path = 'scripts/'+gpio_str+'.txt'
state_file = open(path,'r')
last_state = state_file.read()
print(last_state)
state_file.close()




