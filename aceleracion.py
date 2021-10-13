# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 18:09:51 2021

@author: dguti
"""
from sense_hat import SenseHat

sense = SenseHat()

while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x=round(x, 0)
    y=round(y, 0)
    z=round(z, 0)

    print("x=%2f, y=%2f, z=%2f" % (x, y, z))

