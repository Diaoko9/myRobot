from gpiozero import OutputDevice, InputDevice

import time

###Ultrasonic sensor initialize
trig = OutputDevice(pin=17, active_high=True, initial_value=False)
trig.on()
time.sleep(20)
trig.off()		

###Reading echo Pulse


echo = InputDevice(pin=27, pull_up=False)
echo_state = False

###Rising
if echo_state==False & echo.value==True :
	echo_state = True
	start_time = time.perf_counter_ns()

elif echo_state==True & echo.value==False :
	echo_state = False
	end_time = time.perf_counter_ns()




start_time = time.perf_counter_ns()
if echo.value==True:
	time.sleep(0.001)
end_time = time.perf_counter_ns()
elapsed_time = end_time - start_time
print(elapsed_time)
