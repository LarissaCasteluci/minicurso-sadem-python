# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 19:25:26 2018

@author: larissa-dell
"""

import matplotlib.pyplot as plt
import numpy as np

unidade = 'MPa'

s_x = 1000
s_y = 2000
t_xy = 60

s_med = .5 * (s_x + s_y)
R = np.sqrt((s_x - s_med) * (s_x - s_med) + t_xy * t_xy)

s_1 = s_med + R
s_2 = s_med - R

t_max = R

s = np.linspace(s_1, s_2, 200)

t = np.sqrt(R * R - (s - s_med) * (s - s_med))

print('Tensões Principais: ' + str(s_1) + unidade + ', ' + str(s_2) + unidade)
print('Tensão Máxima de Cisalhamento: ' + str(t_max) + unidade)

plt.plot(s,t)
plt.axis('equal')

if s_2 > 0:
    plt.xlim([-10, s_1 + 10])
elif s_1 < 0:
    plt.xlim([s_2 - 10, 10])
    
plt.grid(True)
plt.xlabel('Tensão Normal [' + unidade + ']')
plt.ylabel('Tensão Cisalhante [' + unidade + ']')
plt.show()