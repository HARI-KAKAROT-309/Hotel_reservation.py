from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()

lable_frame = LabelFrame(root)

lable_frame.pack()

img = ImageTk.PhotoImage(Image.open("gy.jpg"))
panel = Label(lable_frame, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()