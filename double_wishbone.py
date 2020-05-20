# -*- coding: utf-8 -*-
"""
@author: Rafael Basilio Chaves
"""
import numpy as np
from aux_functions import skew_symmetric, trigon
from tkinter import *
from tkinter import ttk
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import pyplot as plt

class double_wishbone:
    def __init__(self):
        # Lower wishbone
        self.A = np.matrix([100,0,0]).T
        self.B = np.matrix([0,200,0]).T
        self.C = np.matrix([-100,0,0]).T
        
        # Upper wishbone    
        self.D = np.matrix([ 100,0,200]).T
        self.E = np.matrix([ 0,200,200]).T
        self.F = np.matrix([-100,0,200]).T
    
        # Steering bar
        self.R = np.matrix([50,0,100]).T
        self.Q = np.matrix([50,200,100]).T
        
        # Wheel center
        self.WC = np.matrix([0,300,100]).T
    
    def doubleWishboneInputs(self, HardpointInfo):
        labelHP1 = ttk.Label(HardpointInfo, text = "LWB Forward")
        labelHP1.grid(column=0, row=2, sticky="W", padx=5, pady=3)
        self.HP1 = Entry(HardpointInfo)
        self.HP1.grid(column=1, row=2, sticky="W", padx=5, pady=3)

        labelHP2 = ttk.Label(HardpointInfo, text = "LWB Backward")
        labelHP2.grid(column=0, row=3, sticky="W", padx=5, pady=3)
        self.HP2 = Entry(HardpointInfo)
        self.HP2.grid(column=1, row=3, sticky="W", padx=5, pady=3)

        labelHP3 = ttk.Label(HardpointInfo, text = "LWB Outboard")
        labelHP3.grid(column=0, row=4, sticky="W", padx=5, pady=3)
        self.HP3 = Entry(HardpointInfo)
        self.HP3.grid(column=1, row=4, sticky="W", padx=5, pady=3)

        labelHP4 = ttk.Label(HardpointInfo, text = "UWB Forward")
        labelHP4.grid(column=0, row=5, sticky="W", padx=5, pady=3)
        self.HP4 = Entry(HardpointInfo)
        self.HP4.grid(column=1, row=5, sticky="W", padx=5, pady=3)

        labelHP5 = ttk.Label(HardpointInfo, text = "UWB Backward")
        labelHP5.grid(column=0, row=6, sticky="W", padx=5, pady=3)
        self.HP5 = Entry(HardpointInfo)
        self.HP5.grid(column=1, row=6, sticky="W", padx=5, pady=3)

        labelHP6 = ttk.Label(HardpointInfo, text = "UWB Outboard")
        labelHP6.grid(column=0, row=7, sticky="W", padx=5, pady=3)
        self.HP6 = Entry(HardpointInfo)
        self.HP6.grid(column=1, row=7, sticky="W", padx=5, pady=3)

        labelHP7 = ttk.Label(HardpointInfo, text = "Steering bar in")
        labelHP7.grid(column=0, row=8, sticky="W", padx=5, pady=3)
        self.HP7 = Entry(HardpointInfo)
        self.HP7.grid(column=1, row=8, sticky="W", padx=5, pady=3)

        labelHP8 = ttk.Label(HardpointInfo, text = "Steering bar Out")
        labelHP8.grid(column=0, row=9, sticky="W", padx=5, pady=3)
        self.HP8 = Entry(HardpointInfo)
        self.HP8.grid(column=1, row=9, sticky="W", padx=5, pady=3)

        labelHP9 = ttk.Label(HardpointInfo, text = "Wheel center")
        labelHP9.grid(column=0, row=10, sticky="W", padx=5, pady=3)
        self.HP9 = Entry(HardpointInfo)
        self.HP9.grid(column=1, row=10, sticky="W", padx=5, pady=3)

    def setHardpoints(self):
        self.kinematics(0,0)
        self.updateCoordinates()
        
    def draw_system(self, PlotArea):
        
        self.PlotArea = PlotArea
        self.fig = Figure(figsize=(5, 4), dpi=100)

        self.canvas = FigureCanvasTkAgg(self.fig, master=PlotArea)
        self.canvas.draw()

        self.canvas.get_tk_widget().pack()
        self.toolbar = NavigationToolbar2Tk(self.canvas, PlotArea)
        self.toolbar.update()

        self.updateCoordinates()

    def updateCoordinates(self):    
        self.ax = self.fig.add_subplot(111, projection="3d")

        # Lower wishbone
        self.lwb_x = np.array([self.A[0,0], self.r_0b[0,0], self.C[0,0]])
        self.lwb_y = np.array([self.A[1,0], self.r_0b[1,0], self.C[1,0]])
        self.lwb_z = np.array([self.A[2,0], self.r_0b[2,0], self.C[2,0]])
    
        # Upper wishbone
        self.uwb_x = np.array([self.D[0,0], self.r_0e[0,0], self.F[0,0]])
        self.uwb_y = np.array([self.D[1,0], self.r_0e[1,0], self.F[1,0]])
        self.uwb_z = np.array([self.D[2,0], self.r_0e[2,0], self.F[2,0]])
        
        # Kingpin
        self.kp_x = np.array([self.r_0b[0,0],self.r_0e[0,0]])
        self.kp_y = np.array([self.r_0b[1,0],self.r_0e[1,0]])
        self.kp_z = np.array([self.r_0b[2,0],self.r_0e[2,0]])
        
        # Steering bar
        self.sb_x = np.array([self.r_0q[0,0], self.r_0r[0,0]])
        self.sb_y = np.array([self.r_0q[1,0], self.r_0r[1,0]])
        self.sb_z = np.array([self.r_0q[2,0], self.r_0r[2,0]])
        
        self.sb_wc_x = np.array([self.r_0q[0,0],self.r_0w[0,0]])
        self.sb_wc_y = np.array([self.r_0q[1,0],self.r_0w[1,0]])
        self.sb_wc_z = np.array([self.r_0q[2,0],self.r_0w[2,0]])    
        
        # Wheel Center
        self.wc_x = np.array([self.r_0w[0,0],(self.r_0e[0,0]+ self.r_0b[0,0])/2])
        self.wc_y = np.array([self.r_0w[1,0],(self.r_0e[1,0]+ self.r_0b[1,0])/2])
        self.wc_z = np.array([self.r_0w[2,0],(self.r_0e[2,0]+ self.r_0b[2,0])/2])
        
        #ax.set_xlim(-1,4)
        #ax.set_ylim(-1,4)
        #ax.set_zlim(-1,4)
    
        self.ax.view_init(23, 35)
        self.ax.plot3D(self.lwb_x,self.lwb_y,self.lwb_z,'red', linewidth=10)
        self.ax.plot3D(self.uwb_x,self.uwb_y,self.uwb_z,'blue', linewidth=10)
        self.ax.plot3D(self.kp_x,self.kp_y,self.kp_z,'green', linewidth=10)
        self.ax.plot3D(self.sb_x,self.sb_y,self.sb_z,'gray', linewidth=10)
        self.ax.plot3D(self.wc_x,self.wc_y,self.wc_z, 'green', linewidth=10)
        self.ax.plot3D(self.sb_wc_x,self.sb_wc_y,self.sb_wc_z, 'gray',linewidth=10)
        plt.show()
        self.canvas.draw()

    def kinematics(self,phi,u):
        ###################################
        # Calculations for lower wishbone #
        ###################################
        
        # Hardpoints fixed at the chassis
        r_ac = self.C - self.A
        
        # Normalized rotation vector for the lower wishbone
        e_ac = r_ac / np.linalg.norm(r_ac)
        
        # Rotation axis as skew-symmetric matrix for later calculations
        e_acS = skew_symmetric(e_ac)
        
        # Rotation axis squared for later calculations
        e_ac2 = e_ac*e_ac.T
        
        # Also part of A_phi calculation
        eye_ac = np.identity(3) - e_ac2
        
        # Finally, calculates the rotation matrix of the LWB
        A_phi = e_ac2 + eye_ac*np.cos(phi) + e_acS*np.sin(phi)
        
        ###################################
        # Calculations for upper wishbone #
        ###################################
        
        r_be = self.E - self.B
        r_de = self.E - self.D
        r_ab = np.matmul(A_phi,(self.B-self.A))
        r_bd = self.D - (self.A+r_ab)
        r_df = self.F - self.D
        e_df = r_df/np.linalg.norm(r_df)
        e_df2 = e_df*e_df.T
        e_dfS = skew_symmetric(e_df)
        
        a = np.dot(np.matmul(r_bd.T,(np.identity(3)-e_df2)),r_de)
        
        b_aux = np.cross(e_df.T,r_de.T)
        b_aux.shape = (3,1)
        b = np.dot(r_bd.T,b_aux)
        c = np.dot(-r_bd.T*e_df2,r_de) - 0.5*(np.dot(r_de.T,r_de)+np.dot(r_bd.T,r_bd)-np.dot(r_be.T,r_be))
        
        psi = trigon(a,b,c)
        
        A_psi = e_df2 + (np.identity(3)-e_df2)*np.cos(psi) + e_dfS*np.sin(psi)
        
        ###################################
        #    Calculations for Kingpin     #
        ###################################
        
        # Lower point
        self.r_0b = self.A + r_ab
        
        r_0de = np.matmul(A_psi,self.E-self.D)
        
        # Upper point
        self.r_0e = self.D + r_0de
        
        beta = trigon(r_be[0],r_be[2],self.r_0e[0])
        
        A_beta = np.array([[np.cos(beta), 0, np.sin(beta)],
                           [0,            1,            0],
                           [-np.sin(beta),0, np.cos(beta)]])
    
        r_0be = self.r_0e - self.B
    
        alpha = trigon(r_0be[1],r_0be[2],r_be[1])
        
        A_alpha = np.array([[1,             0,              0],
                            [0, np.cos(alpha), -np.sin(alpha)],
                            [0, np.sin(alpha),  np.cos(alpha)]])
        
        ###################################
        #    Rotation around Kingpin      #
        ###################################
  
        
        self.r_0r = self.R + np.matrix([0,u,0]).T
        r_rb = self.r_0b - self.r_0r
        rrcht = r_rb.T*np.matmul(A_alpha,A_beta)
        r_rq = self.Q - self.R
        r_bq = self.Q - self.B 
        r_be = self.E - self.B
        e_be = r_be / np.linalg.norm(r_be)
        e_be2 = e_be*e_be.T
        e_beS = skew_symmetric(e_be)
        
        a = np.dot(rrcht,np.matmul((np.identity(3)-e_be2),r_bq))
        
        b_aux = np.cross(e_be.T,r_bq.T)
        b_aux.shape = (3,1)
        b = np.dot(rrcht,b_aux)
        
        p1 = rrcht*e_be2*r_bq
        p2 = np.dot(r_rb.T,r_rb)+np.dot(r_bq.T,r_bq)-np.dot(r_rq.T,r_rq)

        c = -(p1 + 0.5*p2)
        
        delta=trigon(a,b,c)
        A_delta= e_be2 + (np.identity(3)-e_be2)*np.cos(delta) + e_beS*np.sin(delta)
        
        A_w = np.matmul(A_alpha,np.matmul(A_beta,A_delta))
        r0_bq = np.matmul(A_w,r_bq)
        self.r_0q = self.r_0b + r0_bq
        
        ###################################
        #      Wheel Center Movement      #
        ###################################
        r_bw = A_w*(self.WC-self.B)
        self.r_0w = self.r_0b + r_bw 