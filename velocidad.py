# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 18:27:18 2021

@author: dguti
"""

from sense_hat import SenseHat

sense = SenseHat()

while True:
    acceleration = sense.get_gyroscope_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x=round(x, 0)
    y=round(y, 0)
    z=round(z, 0)

    print("x=%2f, y=%2f, z=%2f" % (x, y, z))
    
