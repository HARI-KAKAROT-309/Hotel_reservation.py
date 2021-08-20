from tkinter import *
from tkinter import Tk, messagebox

from PIL import ImageTk, Image

def chech_in1():
    ci_window = Tk()

    ci_window.title("Check In")

    ci_window.configure(bg="black")

    #                           Variable declaration
    spinvar1 = StringVar()
    spinvar2 = StringVar()
    spinvar3 = StringVar()
    spinvar4 = StringVar()

    ci_lf1 = LabelFrame(ci_window, text="Check In", font=("bold", 32))

    ci_lf1.grid(row=0, column=0)

    x = "bed2.jpg"
    img = Image.open(x)
    img = img.resize((1200, 800), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(ci_lf1, image=img)
    panel.image = img
    panel.place(x=0, y=0)

    #                                  Label declaration

    ci_lst = ["Transaction ID ", "  ", "Guest Name ", "No.Of.Adults ", "Room Number ", "No.Of.Children ", "Room Type ",
              "Discount Type ", "Room Rate ", "SubTotal ", "Check In Date ", "Advance Payment ", "Check Out Date ",
              "Total Balance ", "No.Of.Days "]

    Label(ci_lf1, text="   ", font=("bold", 16)).grid(row=0, column=4)

    for i in range(len(ci_lst)):

        if i % 2 == 0:

            Label(ci_lf1, font=("bold", 22)).grid(row=i + 2, column=1)

            Label(ci_lf1, text=ci_lst[i], font=("bold", 18)).grid(row=i + 1, column=1)

        else:

            Label(ci_lf1, text=ci_lst[i], font=("bold", 18)).grid(row=i, column=5)

    #                                       Entry declaration

    entry1 = StringVar()

    entry2 = StringVar()

    spinbox1 = StringVar()

    spinbox2 = StringVar()

    entry3 = StringVar()

    entry4 = StringVar()

    entry5 = StringVar()

    entry6 = StringVar()

    entry7 = StringVar()

    entry8 = StringVar()

    ci_et1 = Entry(ci_lf1, textvariable=entry1, font=("bold", 16))

    ci_et1.grid(row=1, column=3)

    ci_et2_1 = Entry(ci_lf1, textvariable=entry2, font=("bold", 16))

    ci_et2_1.grid(row=3, column=3)

    ci_et2_2 = Spinbox(ci_lf1, textvariable=spinbox1, from_=0, to=20, font=("bold", 16))

    ci_et2_2.grid(row=3, column=7)

    spinvar1.set("Select")

    ci_et3_1 = OptionMenu(ci_lf1, spinvar1, "100", "101", "102", "104", "105", "106", "107", "108", "109")

    ci_et3_1.grid(row=5, column=3)

    ci_et3_2 = Spinbox(ci_lf1, textvariable=spinbox2, from_=0, to=20, font=("bold", 16))

    ci_et3_2.grid(row=5, column=7)

    spinvar2.set("Select")

    ci_et4_1 = OptionMenu(ci_lf1, spinvar2, "AC", "Non-AC")

    ci_et4_1.grid(row=7, column=3)

    spinvar3.set("Select")

    ci_et4_2 = OptionMenu(ci_lf1, spinvar3, "None", "Regular", "VIP")

    ci_et4_2.grid(row=7, column=7)

    ci_et5_1 = Entry(ci_lf1, textvariable=entry3, font=("bold", 16))

    ci_et5_1.grid(row=9, column=3)

    ci_et5_2 = Entry(ci_lf1, textvariable=entry4, font=("bold", 16))

    ci_et5_2.grid(row=9, column=7)

    ci_et6_1 = Entry(ci_lf1, textvariable=entry5, font=("bold", 16))

    ci_et6_1.grid(row=11, column=3)

    ci_et6_2 = Entry(ci_lf1, textvariable=entry6, font=("bold", 16))

    ci_et6_2.grid(row=11, column=7)

    ci_et7_1 = Entry(ci_lf1, textvariable=entry7, font=("bold", 16))

    ci_et7_1.grid(row=13, column=3)

    ci_et7_2 = Entry(ci_lf1, textvariable=entry8, font=("bold", 16), state=DISABLED)

    ci_et7_2.grid(row=13, column=7)

    def balance():
        entry8.set(int(entry3.get())+int(entry4.get())-int(entry6.get()))

    Button(ci_lf1, text="check", command=balance).place(x=875, y=465)

    spinvar4.set("Select")

    ci_et8_1 = OptionMenu(ci_lf1, spinvar4, "1", "2", "3", "4", "5", "6", "7", 'etc')

    ci_et8_1.grid(row=15, column=3)

    def checkin_1():
        print(entry1.get(), entry2.get(), spinbox1.get(), spinvar1.get(), spinbox2.get(), spinvar2.get(),
              spinvar3.get(), entry3.get(), entry4.get(), entry5.get(), entry6.get(), entry7.get(),
              entry8.get(), spinvar4.get())
        content = "insert into c_in_out (t_id, guest_name, N_O_A, room_no, N_O_C, room_type, disount_type, room_rate, subtotal, chech_in_date, advance, check_out_date, totalbalance, no_of_days) values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
            entry1.get(), entry2.get(), spinbox1.get(), spinvar1.get(), spinbox2.get(), spinvar2.get(), spinvar3.get(),
            entry3.get(), entry4.get(), entry5.get(), entry6.get(), entry7.get(), entry8.get(), spinvar4.get())
        table.execute(content)

        c_in1.commit()

        c_in1.close()

        messagebox.showinfo("success", "checked in successfully")

    def clear_1():
        ci_et1.delete(0, END)
        ci_et2_1.delete(0, END)
        ci_et2_2.delete(0, END)
        spinvar1.set("Select")
        ci_et3_2.delete(0, END)
        spinvar2.set("Select")
        spinvar3.set("Select")
        ci_et5_1.delete(0, END)
        ci_et5_2.delete(0, END)
        ci_et6_1.delete(0, END)
        ci_et6_2.delete(0, END)
        ci_et7_1.delete(0, END)
        ci_et7_2.delete(0, END)
        spinvar4.set("Select")

    ci_b1 = Button(ci_lf1, text="Check In", command=checkin_1, font=("bold", 16),
                   activeforeground="white", activebackground="black", width=20)
    ci_b1.grid(row=17, column=3)

    ci_b2 = Button(ci_lf1, text="Clear", command=clear_1, font=("bold", 16),
                   activeforeground="white", activebackground="blue", width=20)
    ci_b2.grid(row=17, column=7)

    Label(ci_lf1, text=" ", font=("bold", 16)).grid(row=17, column=10)
    Label(ci_lf1, text=" ", font=("bold", 16)).grid(row=19, column=1)

    ci_window.mainloop()


if __name__ == "__main__":
    chech_in1()
