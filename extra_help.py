def checkin_1():
    print(entry1.get(), entry2.get(), spinbox1.get(), spinvar1.get(), spinbox2.get(), spinvar2.get(),
          spinvar3.get(), entry3.get(), entry4.get(), entry5.get(), entry6.get(), entry7.get(),
          entry8.get(), spinvar4.get())
    content = "insert into c_in_out (t_id, guest_name, N_O_A, room_no, N_O_C, room_type, disount_type, room_rate, subtotal, chech_in_date, advance, check_out_date, totalbalance, no_of_days) values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
        entry1.get(), entry2.get(), spinbox1.get(), spinvar1.get(), spinbox2.get(), spinvar2.get(),
        spinvar3.get(),
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
               activeforeground="white", activebackground="black", width=20, fg="white", bg="black")
ci_b1.grid(row=17, column=3)

ci_b2 = Button(ci_lf1, text="Clear", command=clear_1, font=("bold", 16),
               activeforeground="white", activebackground="blue", width=20, fg="white", bg="black")
ci_b2.grid(row=17, column=7)

Label(ci_lf1, text=" ", font=("bold", 16), bg="grey18").grid(row=17, column=10)
Label(ci_lf1, text=" ", font=("bold", 16), bg="grey18").grid(row=19, column=1)

else:
messagebox.showerror("Incorrect", "Username or password is incorrect")
except Exception:
messagebox.showerror("Incorrect", "Username or password is incorrect")