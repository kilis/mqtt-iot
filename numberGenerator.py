import random
import time
import math
import logging

def getTempature(x):
    tempeture = random.normalvariate(50, x)
    time.sleep(0.2)
    return round(tempeture, 2)
