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
import math
import time


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
        labelHP1 = ttk.Label(HardpointInfo, text = "LWB forward")
        labelHP1.grid(column=0, row=2, sticky="W", padx=5, pady=3)
        
        self.AX = Entry(HardpointInfo, width=10)
        self.AX.grid(column=1, row=2, sticky="W", padx=5, pady=3)
        self.AX.insert(END,float(self.A[0][0]))

        self.AY = Entry(HardpointInfo, width=10)
        self.AY.grid(column=2, row=2, sticky="W", padx=5, pady=3)
        self.AY.insert(END,float(self.A[1][0]))

        self.AZ = Entry(HardpointInfo, width=10)
        self.AZ.grid(column=3, row=2, sticky="W", padx=5, pady=3)
        self.AZ.insert(END,float(self.A[2][0]))

        labelHP2 = ttk.Label(HardpointInfo, text = "LWB wheel")
        labelHP2.grid(column=0, row=3, sticky="W", padx=5, pady=3)
        
        self.BX = Entry(HardpointInfo, width=10)
        self.BX.grid(column=1, row=3, sticky="W", padx=5, pady=3)
        self.BX.insert(END,float(self.B[0][0]))

        self.BY = Entry(HardpointInfo, width=10)
        self.BY.grid(column=2, row=3, sticky="W", padx=5, pady=3)
        self.BY.insert(END,float(self.B[1][0]))

        self.BZ = Entry(HardpointInfo, width=10)
        self.BZ.grid(column=3, row=3, sticky="W", padx=5, pady=3)
        self.BZ.insert(END,float(self.B[2][0]))

        labelHP3 = ttk.Label(HardpointInfo, text = "LWB backward")
        labelHP3.grid(column=0, row=4, sticky="W", padx=5, pady=3)
        
        self.CX = Entry(HardpointInfo, width=10)
        self.CX.grid(column=1, row=4, sticky="W", padx=5, pady=3)
        self.CX.insert(END,float(self.C[0][0]))

        self.CY = Entry(HardpointInfo, width=10)
        self.CY.grid(column=2, row=4, sticky="W", padx=5, pady=3)
        self.CY.insert(END,float(self.C[1][0]))

        self.CZ = Entry(HardpointInfo, width=10)
        self.CZ.grid(column=3, row=4, sticky="W", padx=5, pady=3)
        self.CZ.insert(END,float(self.C[2][0]))

        labelHP4 = ttk.Label(HardpointInfo, text = "UWB forward")
        labelHP4.grid(column=0, row=5, sticky="W", padx=5, pady=3)
        
        self.DX = Entry(HardpointInfo, width=10)
        self.DX.grid(column=1, row=5, sticky="W", padx=5, pady=3)
        self.DX.insert(END,float(self.D[0][0]))

        self.DY = Entry(HardpointInfo, width=10)
        self.DY.grid(column=2, row=5, sticky="W", padx=5, pady=3)
        self.DY.insert(END,float(self.D[1][0]))

        self.DZ = Entry(HardpointInfo, width=10)
        self.DZ.grid(column=3, row=5, sticky="W", padx=5, pady=3)
        self.DZ.insert(END,float(self.D[2][0]))

        labelHP5 = ttk.Label(HardpointInfo, text = "UWB wheel")
        labelHP5.grid(column=0, row=6, sticky="W", padx=5, pady=3)
        
        self.EX = Entry(HardpointInfo, width=10)
        self.EX.grid(column=1, row=6, sticky="W", padx=5, pady=3)
        self.EX.insert(END,float(self.E[0][0]))

        self.EY = Entry(HardpointInfo, width=10)
        self.EY.grid(column=2, row=6, sticky="W", padx=5, pady=3)
        self.EY.insert(END,float(self.E[1][0]))

        self.EZ = Entry(HardpointInfo, width=10)
        self.EZ.grid(column=3, row=6, sticky="W", padx=5, pady=3)
        self.EZ.insert(END,float(self.D[2][0]))

        labelHP6 = ttk.Label(HardpointInfo, text = "UWB backward")
        labelHP6.grid(column=0, row=7, sticky="W", padx=5, pady=3)
        
        self.FX = Entry(HardpointInfo, width=10)
        self.FX.grid(column=1, row=7, sticky="W", padx=5, pady=3)
        self.FX.insert(END,float(self.F[0][0]))

        self.FY = Entry(HardpointInfo, width=10)
        self.FY.grid(column=2, row=7, sticky="W", padx=5, pady=3)
        self.FY.insert(END,float(self.F[1][0]))

        self.FZ = Entry(HardpointInfo, width=10)
        self.FZ.grid(column=3, row=7, sticky="W", padx=5, pady=3)
        self.FZ.insert(END,float(self.F[2][0]))

        labelHP7 = ttk.Label(HardpointInfo, text = "Steering bar in")
        labelHP7.grid(column=0, row=8, sticky="W", padx=5, pady=3)
        
        self.RX = Entry(HardpointInfo, width=10)
        self.RX.grid(column=1, row=8, sticky="W", padx=5, pady=3)
        self.RX.insert(END,float(self.R[0][0]))

        self.RY = Entry(HardpointInfo, width=10)
        self.RY.grid(column=2, row=8, sticky="W", padx=5, pady=3)
        self.RY.insert(END,float(self.R[1][0]))

        self.RZ = Entry(HardpointInfo, width=10)
        self.RZ.grid(column=3, row=8, sticky="W", padx=5, pady=3)
        self.RZ.insert(END,float(self.R[2][0]))

        labelHP8 = ttk.Label(HardpointInfo, text = "Steering bar Out")
        labelHP8.grid(column=0, row=9, sticky="W", padx=5, pady=3)
        
        self.QX = Entry(HardpointInfo, width=10)
        self.QX.grid(column=1, row=9, sticky="W", padx=5, pady=3)
        self.QX.insert(END,float(self.Q[0][0]))

        self.QY = Entry(HardpointInfo, width=10)
        self.QY.grid(column=2, row=9, sticky="W", padx=5, pady=3)
        self.QY.insert(END,float(self.Q[1][0]))

        self.QZ = Entry(HardpointInfo, width=10)
        self.QZ.grid(column=3, row=9, sticky="W", padx=5, pady=3)
        self.QZ.insert(END,float(self.Q[2][0]))

        labelHP9 = ttk.Label(HardpointInfo, text = "Wheel center")
        labelHP9.grid(column=0, row=10, sticky="W", padx=5, pady=3)
        
        self.WCX = Entry(HardpointInfo, width=10)
        self.WCX.grid(column=1, row=10, sticky="W", padx=5, pady=3)
        self.WCX.insert(END,float(self.WC[0][0]))

        self.WCY = Entry(HardpointInfo, width=10)
        self.WCY.grid(column=2, row=10, sticky="W", padx=5, pady=3)
        self.WCY.insert(END,float(self.WC[1][0]))

        self.WCZ = Entry(HardpointInfo, width=10)
        self.WCZ.grid(column=3, row=10, sticky="W", padx=5, pady=3)
        self.WCZ.insert(END,float(self.WC[2][0]))

    def setHardpoints(self):
        self.kinematics(0,0)

        self.A = np.matrix([float(self.AX.get()),float(self.AY.get()),float(self.AZ.get())]).T
        self.B = np.matrix([float(self.BX.get()),float(self.BY.get()),float(self.BZ.get())]).T
        self.C = np.matrix([float(self.CX.get()),float(self.CY.get()),float(self.CZ.get())]).T

        self.D = np.matrix([float(self.DX.get()),float(self.DY.get()),float(self.DZ.get())]).T
        self.E = np.matrix([float(self.EX.get()),float(self.EY.get()),float(self.EZ.get())]).T
        self.F = np.matrix([float(self.FX.get()),float(self.FY.get()),float(self.FZ.get())]).T

        self.R = np.matrix([float(self.RX.get()),float(self.RY.get()),float(self.RZ.get())]).T
        self.Q = np.matrix([float(self.QX.get()),float(self.QY.get()),float(self.QZ.get())]).T
        self.WC = np.matrix([float(self.WCX.get()),float(self.WCY.get()),float(self.WCZ.get())]).T

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
        
        self.ax.set_xlim(-100,300)
        self.ax.set_ylim(-100,400)
        self.ax.set_zlim(-100,300)
    
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

    def simulate(self, angMax, angMin, steerMin, steerMax):

        for angle in range(angMin, angMax+1):
            self.kinematics(math.radians(angMin + angle), 0)
            self.updateCoordinates()
            time.sleep(0.01)