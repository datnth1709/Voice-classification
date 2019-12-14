#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Wave dispaly
@author: Jiannan Hua
last edited: Oct.24  2018
"""


import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
import math

def fun(x,t):
    y = 2 * np.sin(0.5 * x - 10 * t) + 2 * np.sin(0.6 * x - 60 * t)
    return y

class WavaDisplay(object):
    def __init__(self, wave_fun):
        self.wave_fun = wave_fun

    def Spread(self, xmin, xmax, tmin, tmax, delta_x=0.02, delta_t=0.02):
        self.x = np.linspace(xmin, xmax, (xmax - xmin) / delta_x)
        self.t = np.linspace(tmin, tmax, (tmax - tmin) / delta_t)
        
        fig, ax = plt.subplots(nrows=1, ncols=1)
        
        plt.ion()  #interactive mode on
        
        try:
            for t in self.t:
                self.y = self.wave_fun(self.x, t)
                plt.grid(True) #添加网格
                ax.plot(wd.x, wd.y, color ='k', ls ='-')
                plt.pause(delta_t)
                plt.cla()
        except Exception as err:
            print(err)
        
wd = WavaDisplay(fun)
wd.Spread(xmin=0, xmax=100, tmin=0, tmax=1)

