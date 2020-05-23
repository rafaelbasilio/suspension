from tkinter import *
from tkinter import ttk
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from double_wishbone import double_wishbone

class application:  
        
    def __init__(self, window):
        ###################################################################
        ##################   Designs the tabs for GUI #####################
        ###################################################################
        self.master = window
        self.tab_control = ttk.Notebook(window)
        
        # Creates the desirable tabs for GUI 
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab3 = ttk.Frame(self.tab_control)
        self.tab4 = ttk.Frame(self.tab_control)
        
        # Tab for entering inputs and calculating the whole things
        self.tab_control.add(self.tab1, text='Main Screen')
        
        # Creates left frame for entering suspension type and hardpoints
        self.HardpointInfo = ttk.Frame(self.tab1)
        self.HardpointInfo.grid(column=0, row = 0)

        # Label for combobox suspension type
        labelTop = ttk.Label(self.HardpointInfo, text = "Suspension Type", font=("Helvetica", 10, 'bold'))
        labelTop.grid(column=0, row=0, columnspan=2, sticky="W", padx=5)
        
        # Combobox suspension type
        comboBox1= ttk.Combobox(self.HardpointInfo, values=["Double Wishbone", "McPherson", "Multilink"])        
        # Sets double wishbone as default
        comboBox1.current(0)
        comboBox1.grid(column=0, row=1,columnspan=2, sticky="W", padx=5, pady=10)

        # Labels for hardpoints coordinates
        labelUnits = ttk.Label(self.HardpointInfo, text = "Hardpoints", font=("Helvetica", 10, 'bold'))
        labelUnits.grid(column=0, row=2, sticky="W", padx=5, pady=3)

        labelUnits = ttk.Label(self.HardpointInfo, text = "X [m]", font=("Helvetica", 10, 'bold'))
        labelUnits.grid(column=1, row=2, sticky="W", padx=5, pady=3)

        labelUnits = ttk.Label(self.HardpointInfo, text = "Y [m]", font=("Helvetica", 10, 'bold'))
        labelUnits.grid(column=2, row=2, sticky="W", padx=5, pady=3)

        labelUnits = ttk.Label(self.HardpointInfo, text = "Z [m]", font=("Helvetica", 10, 'bold'))
        labelUnits.grid(column=3, row=2, sticky="W", padx=5, pady=3)

        # If double wishbone selected
        suspension = double_wishbone()
        suspension.doubleWishboneInputs(self.HardpointInfo)

        # Plots
        self.PlotArea = ttk.Frame(self.tab1)
        suspension.kinematics(0,0)
        suspension.draw_system(self.PlotArea)    
        
        # Draws left frame
        self.HardpointInfo.pack(side=LEFT)

        # Draws the figure frame
        self.PlotArea.pack(side=LEFT)

        # Plots the torque and power curves
        self.tab_control.add(self.tab2, text='Angle Plots')
        
        # Plots resistance curves for every gear at the torque curve
        # and the last gear x power output (under/overrevs or optimum project)
        self.tab_control.add(self.tab3, text='Offsets / Others')
        
        # About
        self.tab_control.add(self.tab4, text='About')
        
        # You're free to change the entire code, but please do not delete this part. 
        # It is very important to me to receive feedbacks.
        Title = "Suspension Kinematics Simulator v1.0"
        appInfos ="""
        This software was originally designed by Rafael Basilio Chaves.
        Thanks to Abel Arrieta Castro for the help with bug correcting.
        The suspension models in this application were 100% based on the Book
        Vehicle Dynamics: Fundamentals and Modeling, written by Prof. Georg Rill
        The original version can be found at: https://github.com/rafaelbasilio/suspension
        Feel free to distribute and modify it as you want.\n
        This sofrware is 100% free and OpenSource and it must stay like this. 
        The commercial use of it is allowed, but it is extrictly vorbiden to sell this software for any price.
        Feedbacks, improvements and suggestions are always welcome!
        Please get in touch with me: doutorautomovel@gmail.com
        Have Fun! 
        """
        self.title = Label(self.tab4, text=Title, font=("Helvetica", 14, 'bold'))
        self.title.pack(pady=30)
        self.information = Label(self.tab4, text=appInfos)
        self.information.pack()
        
        # Packs the entire tabs
        self.tab_control.pack(expand=0, fill='both')

window = Tk()
window.title("Suspension Kinematics Simulator v1.0")
window.geometry('800x600')
window.resizable(width=False, height=False)
app = application(window)
window.mainloop()

