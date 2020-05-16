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
        self.tab_control.pack(expand=1, fill='both')
        
window = Tk()
window.title("Suspension Kinematics Simulator v1.0")
window.geometry('800x600')
window.resizable(width=False, height=False)
app = application(window)
window.mainloop()


