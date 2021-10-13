# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 17:28:06 2021

@author: dguti
"""

from sense_hat import SenseHat
sense = SenseHat()
sense.clear()

o = sense.get_orientation()
pitch = o["pitch"]
roll = o["roll"]
yaw = o["yaw"]
print("pitch: %2f, roll: %2f, yaw: %2f" % (pitch, roll, yaw))
