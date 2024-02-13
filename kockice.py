import tkinter as tk
from tkinter import ttk
from tkinter import *
import random

window=Tk()
window.geometry("400x400")

l1=Label(window,font=("helvetica",50))

def roll():
    dice_values={'\u2680':1,'\u2681':2,'\u2682':3,'\u2683':4,'\u2684':5,'\u2685':6}

    dice_symbols=f"{random.choice(list(dice_values.keys()))}{random.choice(list(dice_values.keys()))}\n{random.choice(list(dice_values.keys()))}{random.choice(list(dice_values.keys()))}\n{random.choice(list(dice_values.keys()))}{random.choice(list(dice_values.keys()))}\n{random.choice(list(dice_values.keys()))}{random.choice(list(dice_values.keys()))}"
    l1.config(text=dice_symbols,foreground="brown4")
    l1.pack()
    

    

b1=Button(window,text="Roll",font=("helvetica",20),background="orange",command=roll)
b1.place(x=300,y=200)
b1.pack()



window.mainloop()