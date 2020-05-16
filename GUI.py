from tkinter import *
from tkinter import ttk
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
import numpy as np

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
        
        # If double wishbone selected
        self.doubleWishboneInputs()
        
        # Simulation details
        self.SimDetails()    
        
        # Draws left frame
        self.HardpointInfo.pack(side=LEFT)
        
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
        
    def doubleWishboneInputs(self):
        labelHP1 = ttk.Label(self.HardpointInfo, text = "LWB Forward")
        labelHP1.grid(column=0, row=2, sticky="W", padx=5, pady=3)
        HP1 = Entry(self.HardpointInfo)
        HP1.grid(column=1, row=2, sticky="W", padx=5, pady=3)

        labelHP2 = ttk.Label(self.HardpointInfo, text = "LWB Backward")
        labelHP2.grid(column=0, row=3, sticky="W", padx=5, pady=3)
        HP2 = Entry(self.HardpointInfo)
        HP2.grid(column=1, row=3, sticky="W", padx=5, pady=3)

        labelHP3 = ttk.Label(self.HardpointInfo, text = "LWB Outboard")
        labelHP3.grid(column=0, row=4, sticky="W", padx=5, pady=3)
        HP3 = Entry(self.HardpointInfo)
        HP3.grid(column=1, row=4, sticky="W", padx=5, pady=3)
        
        labelHP4 = ttk.Label(self.HardpointInfo, text = "UWB Forward")
        labelHP4.grid(column=0, row=5, sticky="W", padx=5, pady=3)
        HP4 = Entry(self.HardpointInfo)
        HP4.grid(column=1, row=5, sticky="W", padx=5, pady=3)

        labelHP5 = ttk.Label(self.HardpointInfo, text = "UWB Backward")
        labelHP5.grid(column=0, row=6, sticky="W", padx=5, pady=3)
        HP5 = Entry(self.HardpointInfo)
        HP5.grid(column=1, row=6, sticky="W", padx=5, pady=3)

        labelHP6 = ttk.Label(self.HardpointInfo, text = "UWB Outboard")
        labelHP6.grid(column=0, row=7, sticky="W", padx=5, pady=3)
        HP6 = Entry(self.HardpointInfo)
        HP6.grid(column=1, row=7, sticky="W", padx=5, pady=3)

        labelHP7 = ttk.Label(self.HardpointInfo, text = "Steering bar in")
        labelHP7.grid(column=0, row=8, sticky="W", padx=5, pady=3)
        HP7 = Entry(self.HardpointInfo)
        HP7.grid(column=1, row=8, sticky="W", padx=5, pady=3)

        labelHP8 = ttk.Label(self.HardpointInfo, text = "Steering bar Out")
        labelHP8.grid(column=0, row=9, sticky="W", padx=5, pady=3)
        HP8 = Entry(self.HardpointInfo)
        HP8.grid(column=1, row=9, sticky="W", padx=5, pady=3)

        labelHP9 = ttk.Label(self.HardpointInfo, text = "Wheel center")
        labelHP9.grid(column=0, row=10, sticky="W", padx=5, pady=3)
        HP9 = Entry(self.HardpointInfo)
        HP9.grid(column=1, row=10, sticky="W", padx=5, pady=3)
    
    def SimDetails(self):

        labelSimDet = ttk.Label(self.HardpointInfo, text = "Input range (lower wishbone)", font=("Helvetica", 10, 'bold'))
        labelSimDet.grid(column=0, row=11, columnspan=2, sticky="W", padx=5, pady=10)
        
        labelSimDet1 = ttk.Label(self.HardpointInfo, text = "max. angle [deg]")
        labelSimDet1.grid(column=0, row=12, sticky="W", padx=5, pady=3)
        SimDet1 = Entry(self.HardpointInfo)
        SimDet1.grid(column=1, row=12, sticky="W", padx=5, pady=3)

        labelSimDet2 = ttk.Label(self.HardpointInfo, text = "min. angle [deg]")
        labelSimDet2.grid(column=0, row=13, sticky="W", padx=5, pady=3)
        SimDet2 = Entry(self.HardpointInfo)
        SimDet2.grid(column=1, row=13, sticky="W", padx=5, pady=3)

window = Tk()
window.title("Suspension Kinematics Simulator v1.0")
window.geometry('800x600')
window.resizable(width=False, height=False)
app = application(window)
window.mainloop()

