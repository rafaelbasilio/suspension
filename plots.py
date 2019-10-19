# -*- coding: utf-8 -*-
"""
Autor: Rafael Basilio Chaves
"""
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
from double_wishbone import double_wishbone


ax = plt.axes(projection="3d")

data = double_wishbone()

# Lower wishbone
lwb_x = np.array([data.A[0], data.B[0], data.C[0]])
lwb_y = np.array([data.A[1], data.B[1], data.C[1]])
lwb_z = np.array([data.A[2], data.B[2], data.C[2]])

# Upper wishbone
uwb_x = np.array([data.D[0], data.E[0], data.F[0]])
uwb_y = np.array([data.D[1], data.E[1], data.F[1]])
uwb_z = np.array([data.D[2], data.E[2], data.F[2]])

# Kingpin
kp_x = np.array([data.B[0], data.E[0]])
kp_y = np.array([data.B[1], data.E[1]])
kp_z = np.array([data.B[2], data.E[2]])

# Steering bar
sb_x = np.array([data.R[0], data.Q[0]])
sb_y = np.array([data.R[1], data.Q[1]])
sb_z = np.array([data.R[2], data.Q[2]])

ax.plot3D(lwb_x,lwb_y,lwb_z,'gray')
ax.plot3D(uwb_x,uwb_y,uwb_z,'gray')
ax.plot3D(kp_x,kp_y,kp_z,'gray')
ax.plot3D(sb_x,sb_y,sb_z,'gray')

plt.show()
