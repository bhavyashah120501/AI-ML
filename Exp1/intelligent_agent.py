import requests
import random
import time

stream_temp = random.randint()

def setWaterConditions(required_temp):
    def WaterTubTemperature():
        # we can fetch the data from the sensor about the room temperature
        # due to unavailability of the sensors, a random number is chosen by default
        return random.randint(0, 27)
    def Change_stream_temp(p):
        global stream_temp
        stream_temp += p

    tub_temp = WaterTubTemperature()
    print('Current Tub Temperature is ' + str(round(tub_temp, 2)))
    if required_temp > tub_temp:
        # sending a command to the system to raise the temperature
        print("Increasing the stream_temp temperature by " + str(round(required_temp - tub_temp, 2)))
    elif required_temp < tub_temp:
        # sending a command to the system to drop the temperature
        print("Dropping the stream_temp temperature by " + str(round(tub_temp - required_temp, 2)))
    else:
        # all cool, relax!
        print("Conditions are alright! Sit back and relax!")
    change = round(required_temp - tub_temp, 2)
    Change_stream_temp(4)

while(True):
    setWaterConditions(random.randint())
    time.sleep(10)