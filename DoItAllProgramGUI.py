
from tkinter import ttk
from tkinter import *
import University.GUIMaster as gm
from University import user_profile as user_profile
from University import globals as globals
from University import GUIMaster as gui

#####################################
# Create and Initialize main Window
# Window is as small as can go to obscure
# This window will be running until the
# Program is ended
####################################


if __name__=="__main__":

    root = Tk()
    root.geometry('40x10')
    # root.withdraw()
    gui.start_program(root)
   
    root.mainloop()
