# -*- coding: utf-8 -*-
"""
@author: Rafael Basilio Chaves
"""      
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from double_wishbone import double_wishbone
        
def draw_system(self,system):
    # In case of Double Wishbone
    if(system == 1):
        # Lower wishbone
        lwb_x = np.array([self.A[0,0], self.r_0b[0,0], self.C[0,0]])
        lwb_y = np.array([self.A[1,0], self.r_0b[1,0], self.C[1,0]])
        lwb_z = np.array([self.A[2,0], self.r_0b[2,0], self.C[2,0]])
    
        # Upper wishbone
        uwb_x = np.array([self.D[0,0], self.r_0e[0,0], self.F[0,0]])
        uwb_y = np.array([self.D[1,0], self.r_0e[1,0], self.F[1,0]])
        uwb_z = np.array([self.D[2,0], self.r_0e[2,0], self.F[2,0]])
        
        # Kingpin
        kp_x = np.array([self.r_0b[0,0],self.r_0e[0,0]])
        kp_y = np.array([self.r_0b[1,0],self.r_0e[1,0]])
        kp_z = np.array([self.r_0b[2,0],self.r_0e[2,0]])
        
        # Steering bar
        sb_x = np.array([self.r_0q[0,0],self.r_0r[0,0]])
        sb_y = np.array([self.r_0q[1,0],self.r_0r[1,0]])
        sb_z = np.array([self.r_0q[2,0],self.r_0r[2,0]])
        
        sb_wc_x = np.array([self.r_0q[0,0],self.r_0w[0,0]])
        sb_wc_y = np.array([self.r_0q[1,0],self.r_0w[1,0]])
        sb_wc_z = np.array([self.r_0q[2,0],self.r_0w[2,0]])    
        
        # Wheel Center
        wc_x = np.array([self.r_0w[0,0],(self.r_0e[0,0]+self.r_0b[0,0])/2])
        wc_y = np.array([self.r_0w[1,0],(self.r_0e[1,0]+self.r_0b[1,0])/2])
        wc_z = np.array([self.r_0w[2,0],(self.r_0e[2,0]+self.r_0b[2,0])/2])
        
        ax = plt.axes(projection="3d")
        #ax.set_xlim(-1,4)
        #ax.set_ylim(-1,4)
        #ax.set_zlim(-1,4)
        #ax.view_init(51, 61)
        ax.plot3D(lwb_x,lwb_y,lwb_z,'red', linewidth=20)
        ax.plot3D(uwb_x,uwb_y,uwb_z,'blue', linewidth=20)
        ax.plot3D(kp_x,kp_y,kp_z,'green', linewidth=20)
        ax.plot3D(sb_x,sb_y,sb_z,'gray', linewidth=20)
        ax.plot3D(wc_x,wc_y,wc_z, 'green', linewidth=20)
        ax.plot3D(sb_wc_x,sb_wc_y,sb_wc_z, 'gray',linewidth=20)
        plt.show()
        
    # In case of McPherson    
    elif(system == 2):
        pass
    
    # In case of Multilink
    else:
        pass

#suspensao = double_wishbone()
#suspensao.kinematics(0,0)