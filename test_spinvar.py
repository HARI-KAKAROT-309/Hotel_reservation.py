from tkinter import *
from tkinter.messagebox import showerror

class GUI:
    def __init__(self, parent):
        self.iv = IntVar()
        self.sb = Spinbox(parent, from_=0, to=10, textvariable = self.iv)
        self.sb.pack()
        self.b1 = Button(parent, text="Confirm", command=self.validate)
        self.b1.pack()

    def validate(self):
        nb = self.sb.get()
        try:
            nb = int(nb)
            # do something with the number
            print(nb)
        except Exception:
            showerror('Error', 'Invalid content')


root = Tk()
root.geometry("800x600")
GUI = GUI(root)
root.title("Example")
root.mainloop()
