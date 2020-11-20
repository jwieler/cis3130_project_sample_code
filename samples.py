import random
import simpy

NUMBER_CARS = 100
RANDOM_SEED = 42
INTERVAL_CARS = 8

GREEN_TIME = 36
RED_TIME = 24

arrivals = []

def source(env, number, interval, intersection):
    """Source generates cars randomly"""
    for i in range(number):
        c = car(env, 'Car%02d' % i, intersection, time_in_intersection=12.0)
        env.process(c)
        t = random.expovariate(1.0 / interval)
        yield env.timeout(t)

def car(env, name, intersection, time_in_intersection):
    """Car arrives and then leaves."""
    arrive = env.now
    print('%7.4f %s: Here I am' % (arrive, name))

    with intersection.request() as req:
        wait = env.now - arrive
        # We got through the inersection
        print('%7.4f %s: Waited %6.3f' % (env.now, name, wait))

        tii = random.expovariate(1.0 / time_in_intersection)
        yield env.timeout(tii)
        print('%7.4f %s: Finished' % (env.now, name))

# Setup and start the simulation
print('Traffic')
random.seed(RANDOM_SEED)
env = simpy.Environment()

# Start processes and run
intersection = simpy.Resource(env, capacity=1)
env.process(source(env, NUMBER_CARS, INTERVAL_CARS, intersection))
env.run()

