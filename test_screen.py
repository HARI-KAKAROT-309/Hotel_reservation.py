from tkinter import *

from time import *

main_window = Tk()

main_frame2 = LabelFrame(main_window, width=1200, height=800)

main_frame2.grid(row=0, column=0)


for i in range (5):
    Label(main_frame2, text="Please wait .     ", font=("bold", 40)).place(x=500, y=400)

    main_window.update()
    
    sleep(0.5)

    Label(main_frame2, text="Please wait . .  ", font=("bold", 40)).place(x=500, y=400)

    main_window.update()
    
    sleep(0.5)

    Label(main_frame2, text="Please wait . . .", font=("bold", 40)).place(x=500, y=400)

    main_window.update()
    
    sleep(0.5)

main_frame2.destroy()
