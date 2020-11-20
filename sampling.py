from collections import deque # double-ended queue
import random
import simpy
from simpy.util import start_delayed
import matplotlib.pyplot as plt
from numpy import average
import numpy as np

NUMBER_CARS = 100
RANDOM_SEED = 42
INTERVAL_CARS = 8

green_time = 36
red_time = 24

arrival_rate = 8
t_interarrival_mean= 1.0 / arrival_rate

times = []
for i in range(NUMBER_CARS):
   times.append(random.expovariate(t_interarrival_mean))
print(average(times))

'''
In the balanced scenario, the signals are re-timed with 60-second cycle lengths.
The amount of green time at each minor intersection is apportioned in a 3:2 ratio (36 seconds for the major street, 24 for the minor). 
The increased turnover improves pedestrian compliance and decreases congestion on surrounding streets.
'''

plt.hist(times, bins=50) 
plt.show()
print(average(times))

seconds = 500
time = 0
light = True # true will mean green, false is red.
green_times = []
red_times = []
while time <= seconds:
    if light:
        now = time
        time += green_time
        light = False
        print("light turned red at:", time, "seconds")
        green_times.append(time - now)
    else:
        now = time
        time += red_time
        light = True
        print("light turned green at:", time, "seconds")
        red_times.append(time - now)

