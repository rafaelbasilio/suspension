# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 08:54:13 2019

@author: Raquel
"""
import numpy as np
from aux_functions import skew_symmetric, trigon
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

class double_wishbone:
    def __init__(self):
        # Lower wishbone
        self.A = np.array([ 1,0,0])
        self.B = np.array([ 0,2,0])
        self.C = np.array([-1,0,0])
    
        # Upper wishbone    
        self.D = np.array([ 1,0,2])
        self.E = np.array([ 0,2,2])
        self.F = np.array([-1,0,2])
    
        # Steering bar
        self.R = np.array([0.5,0,1])
        self.Q = np.array([0.5,2,1])
        
        # Wheel center
        self.WC = np.array([0,3,1])
        
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
        e_ac2 = e_ac*np.transpose(e_ac)
        
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
        e_df2 = e_df*np.transpose(e_df)
        e_dfS = skew_symmetric(e_df)
        
        a = np.dot(np.matmul(np.transpose(r_bd),(np.identity(3)-e_df2)),r_de)
        b = np.dot(np.transpose(r_bd),np.cross(e_df,r_de))
        c = np.dot(-np.transpose(r_bd)*e_df2,r_de) - 0.5*(np.dot(r_de,r_de)+np.dot(r_bd,r_bd)-np.dot(r_be,r_be))
        
        psi = trigon(a,b,c);
        
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
  
        
        self.r_0r = self.R + np.array([0,u,0])
        r_rb = self.r_0b - self.r_0r
        rrcht = np.matmul(r_rb,A_alpha*A_beta)
        r_rq = self.Q - self.R
        r_bq = self.Q - self.B 
        r_be = self.E - self.B
        e_be = r_be / np.linalg.norm(r_be)
        e_be2 = e_be*e_be
        e_beS = skew_symmetric(e_be)
        
        a = np.dot(np.matmul(rrcht,(np.identity(3)-e_be2)),r_bq)
        b = np.dot(rrcht,np.cross(e_be,r_bq))
        c = -np.dot(rrcht,e_be2*r_bq) - 0.5*(np.dot(r_rb,r_rb)+np.dot(r_bq,r_bq)-np.dot(r_rq,r_rq))
        
        
        delta=trigon(a,b,c)
        A_delta= e_be2 + (np.identity(3)-e_be2)*np.cos(delta) + e_beS*np.sin(delta)
        
        A_w = np.matmul(A_alpha,np.matmul(A_beta,A_delta))
        r0_bq = np.matmul(A_w,r_bq)
        self.r_0q = self.r_0b + r0_bq
        
        
        self.draw_system()
        
        
    def draw_system(self):
        # Lower wishbone
        lwb_x = np.array([self.A[0], self.r_0b[0], self.C[0]])
        lwb_y = np.array([self.A[1], self.r_0b[1], self.C[1]])
        lwb_z = np.array([self.A[2], self.r_0b[2], self.C[2]])

        # Upper wishbone
        uwb_x = np.array([self.D[0], self.r_0e[0], self.F[0]])
        uwb_y = np.array([self.D[1], self.r_0e[1], self.F[1]])
        uwb_z = np.array([self.D[2], self.r_0e[2], self.F[2]])
        
        # Kingpin
        kp_x = np.array([self.r_0b[0],self.r_0e[0]])
        kp_y = np.array([self.r_0b[1],self.r_0e[1]])
        kp_z = np.array([self.r_0b[2],self.r_0e[2]])
        
        # Steering bar
        sb_x = np.array([self.r_0q[0],self.r_0r[0]])
        sb_y = np.array([self.r_0q[1],self.r_0r[1]])
        sb_z = np.array([self.r_0q[2],self.r_0r[2]])
        
#        # Wheel Center
#        wc_x = np.array([self.r_0w[0],(self.r_0e[0]+self.r_0b[0])/2])
#        wc_y = np.array([self.r_0w[1],(self.r_0e[1]+self.r_0b[1])/2])
#        wc_z = np.array([self.r_0w[2],(self.r_0e[2]+self.r_0b[2])/2])
        
        ax = plt.axes(projection="3d")
        ax.set_xlim(-1,4)
        ax.set_ylim(-1,4)
        ax.set_zlim(-1,4)
        ax.view_init(30, 10)
        ax.plot3D(lwb_x,lwb_y,lwb_z,'gray')
        ax.plot3D(uwb_x,uwb_y,uwb_z,'gray')
        ax.plot3D(kp_x,kp_y,kp_z,'gray')
        ax.plot3D(sb_x,sb_y,sb_z,'gray')
        plt.show()

suspensao = double_wishbone()
#suspensao.kinematics(0,0)
for i in range(-10,10):
   suspensao.kinematics(-i/100.0,0)
   plt.pause(0.1)
for i in range(-10,10):
   suspensao.kinematics(i/100.0,0)
   plt.pause(0.1)
for i in range(-10,10):
   suspensao.kinematics(-i/100.0,0)
   plt.pause(0.1)
for i in range(-10,10):
   suspensao.kinematics(i/100.0,0)
   plt.pause(0.1)