                    rf_et1 = Entry(rf_lf1, font=("bold", 16))

                    rf_et1.place(x=235, y=15)

                    g_name = StringVar()

                    rf_et2_1 = Entry(rf_lf1, font=("bold", 16), textvariable=g_name)

                    rf_et2_1.place(x=235, y=95)

                    rf_et2_2 = Spinbox(rf_lf1, from_=0, to=5, font=("bold", 16))

                    rf_et2_2.place(x=805, y=95)

                    room_data = db.cursor()

                    content = "select room_no from room where check1='-'"

                    room_data.execute(content)

                    table = room_data.fetchall()

                    leng = len(table)

                    table1 = '"Select"'

                    for i in range(len(table)):
                        table1 = table1 + ',"' + str(table[i][0]) + '"'

                    rf_et3_1 = ttk.Combobox(rf_lf1, textvariable=spinvar1)

                    rf_et3_1['values'] = (eval(table1))

                    rf_et3_1.place(x=235, y=175)

                    rf_et3_2 = Spinbox(rf_lf1, from_=0, to=5, font=("bold", 16))

                    rf_et3_2.place(x=805, y=175)

                    spinvar2.set("Select")

                    rf_et4_1 = OptionMenu(rf_lf1, spinvar2, "AC", "Non-AC")

                    rf_et4_1.place(x=235, y=255)

                    spinvar3.set("None")

                    rf_et4_2 = OptionMenu(rf_lf1, spinvar3, "None", "Regular", "VIP")

                    rf_et4_2.place(x=805, y=255)

                    rf_et5_1_1 = StringVar()

                    rf_et5_2_1 = StringVar()

                    rf_et6_2_1 = IntVar()

                    rf_et7_2_1 = StringVar()

                    rf_et5_1 = Entry(rf_lf1, font=("bold", 16), textvariable=rf_et5_1_1, state=DISABLED)

                    rf_et5_1.place(x=235, y=335)

                    def rate():

                        rate = db.cursor()

                        content = "select * from discount"

                        rate.execute(content)

                        rate_var = rate.fetchall()

                        if spinvar2.get() == "AC":
                            rf_et5_1_1.set("3000")

                            rf_et5_2_1.set(str(3000 + (int(rf_et2_2.get()) * 900) + (int(rf_et3_2.get()) * 300)))

                            if spinvar3.get() == "Regular":
                                rf_et5_2_1.set(
                                    str(int(rf_et5_2_1.get()) - (int(rf_et5_2_1.get()) * (rate_var[1][1] / 100))))

                            elif spinvar3.get() == "VIP":
                                rf_et5_2_1.set(
                                    str(int(rf_et5_2_1.get()) - (int(rf_et5_2_1.get()) * (rate_var[2][1] / 100))))

                            else:
                                rf_et5_2_1.set(
                                    str(int(rf_et5_2_1.get()) - (int(rf_et5_2_1.get()) * (rate_var[0][1] / 100))))

                        elif spinvar2.get() == "Non-AC":
                            rf_et5_1_1.set("2200")

                            rf_et5_2_1.set(str(2200 + (int(rf_et2_2.get()) * 800) + (int(rf_et3_2.get()) * 250)))

                            if spinvar3.get() == "Regular":
                                rf_et5_2_1.set(
                                    str(int(rf_et5_2_1.get()) - (int(rf_et5_2_1.get()) * (rate_var[1][1] / 100))))

                            elif spinvar3.get() == "VIP":
                                rf_et5_2_1.set(
                                    str(int(rf_et5_2_1.get()) - (int(rf_et5_2_1.get()) * (rate_var[2][1] / 100))))

                            else:
                                rf_et5_2_1.set(
                                    str(int(rf_et5_2_1.get()) - (int(rf_et5_2_1.get()) * (rate_var[0][1] / 100))))

                        else:
                            messagebox.showerror("Error", "select room type correctly")

                        

                    Button(rf_lf1, text="check", command=rate).place(x=435, y=335)

                    rf_et5_2 = Entry(rf_lf1, font=("bold", 16), textvariable=rf_et5_2_1, state=DISABLED)

                    rf_et5_2.place(x=805, y=335)

                    rf_et6_1 = Entry(rf_lf1, font=("bold", 16), textvariable=date1, state=DISABLED)

                    rf_et6_1.place(x=235, y=415)

                    Button(rf_lf1, text="Select", command=calendar1).place(x=434, y=416)

                    rf_et6_2 = Entry(rf_lf1, font=("bold", 16), textvariable=rf_et6_2_1)

                    rf_et6_2.place(x=235, y=575)

                    rf_et7_1 = Entry(rf_lf1, font=("bold", 16), textvariable=date2, state=DISABLED)

                    rf_et7_1.place(x=235, y=495)

                    Button(rf_lf1, text="Select", command=calendar2).place(x=434, y=496)

                    rf_et7_2 = Entry(rf_lf1, font=("bold", 16), textvariable=rf_et7_2_1, state=DISABLED)

                    rf_et7_2.place(x=805, y=575)

                    spinvar4.set("Will be auto filled")

                    rf_et8_1 = Entry(rf_lf1, font=("bold", 16), textvariable=spinvar4, state=DISABLED)

                    rf_et8_1.place(x=805, y=415)

                    spinvar5 = StringVar()

                    rf_et8_2 = Entry(rf_lf1, font=("bold", 16), textvariable=spinvar5, state=DISABLED)

                    rf_et8_2.place(x=805, y=495)

                    go = 0

                    

                        val = rf_et5_2_1.get()

                        leng = len(rf_et5_2_1.get())

                        if (int(val[:leng-2])) >0:

                            spinvar5.set(int(val[:leng-2])*int(spinvar4.get()))

                        
                            
                        

                    def rate2():
                        try:
                            a = int(rf_et6_2_1.get())
                            
                            if len(spinvar5.get()) >0 :

                                if (int(spinvar5.get()) - int(rf_et6_2_1.get())) >=0:
                                    rf_et7_2_1.set(str(int(spinvar5.get()) - int(rf_et6_2_1.get())))

                                else:
                                    messagebox.showinfo('Info', "You don't need to Pay more amount than the actual room rate")
                                
                            else:
                                messagebox.showerror('Error', 'Enter Proper Advance amount..')
                                
                        except Exception:

                            messagebox.showerror('Error', 'Enter Proper Advance amount..')
                            

                    Button(rf_lf1, text="check", command=rate1).place(x=1005, y=495)

                    Button(rf_lf1, text="check", command=rate2).place(x=1005, y=575)

                    def checkin_2():

                        

                        try:
                            a = int(spinvar1.get())

                            room_data = db.cursor()

                            content = "select room_no from room where check1='-'"

                            room_data.execute(content)

                            table = room_data.fetchall()

                            for i in range(len(table)):

                                if (int(spinvar1.get()) == int(table[i][0])):
                                    
                                    go+=1

                                    break
                            else:
                                messagebox.showerror('Error', 'Enter correct room number')                            
                            
                        except Exception:
                            messagebox.showerror('Error', 'Enter correct room number')
                        
                        try:
                            a = int(rf_et2_2.get())

                            go+=1

                            if a >5:

                                messagebox.showerror('Error', 'Enter Proper Adult count')

                                go-=1
                            
                        except Exception:
                            messagebox.showerror('Error', 'Enter Proper Adult count')

                        try:
                            a = int(rf_et3_2.get())

                            go+=1

                            if a >5:

                                messagebox.showerror('Error', 'Enter Proper child count')

                                go-=1
                            
                        except Exception:
                            messagebox.showerror('Error', 'Enter Proper child count')

                        try:
                            if int(rf_et7_2_1.get()) >= 0:

                                go+=1
                            
                            else:
                                messagebox.showerror('Error', 'Check the balance amount')
                                
                        except Exception:
                            messagebox.showerror('Error', 'Check the balance amount')

                        if g_name.get().isalpha() and g_name.get() != "" and g_name.get() != " " and g_name.get() != "  ":
                            go+=1
                            
                        else:
                            
                            messagebox.showerror('Error', 'Enter the Guest name correctly')

                        if rf_et6_1.get() != "":
                            go+=1
                            
                        else:
                            
                            messagebox.showerror('Error', 'Enter the check in date')

                        if rf_et7_1.get() != "":
                            
                            go+=1
                            
                        else:
                            
                            messagebox.showerror('Error', 'Enter the check out date')

                        
                        """if go == 7:
                            c_in_data = db.cursor()

                            content0 = 'select p_id from registration'

                            c_in_data.execute(content0)

                            test = c_in_data.fetchall()

                            test_val = 0

                            for i in range(len(test)):
                                if test[i][0] == int(rf_et1.get()):
                                    content = "insert into c_in_out(p_id, g_name, n_o_a, rm_no, n_o_c, rm_type, discount_type, rm_rate, sub_tot, ch_in, ad_py, ch_out, tot_bal, n_o_d) values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
                                        rf_et1.get(), rf_et2_1.get(), rf_et2_2.get(), spinvar1.get(), rf_et3_2.get(),
                                        spinvar2.get(), spinvar3.get(), rf_et5_1.get(),
                                        rf_et5_2.get(), rf_et6_1.get(), rf_et6_2.get(), rf_et7_1.get(), rf_et7_2.get(),
                                        spinvar4.get())

                                    content3 = "insert into permanent_data(p_id, g_name, n_o_a, rm_no, n_o_c, rm_type, discount_type, rm_rate, sub_tot, ch_in, ad_py, ch_out, tot_bal, n_o_d, c_in_check, c_out_check) values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
                                        rf_et1.get(), rf_et2_1.get(), rf_et2_2.get(), spinvar1.get(), rf_et3_2.get(),
                                        spinvar2.get(), spinvar3.get(), rf_et5_1.get(),
                                        rf_et5_2.get(), rf_et6_1.get(), rf_et6_2.get(), rf_et7_1.get(), rf_et7_2.get(),
                                        spinvar4.get(), 'yes', 'no')

                                    content1 = "update room set check1='/' where room_no='" + spinvar1.get() + "'"

                                    c_in_data.execute(content)

                                    c_in_data.execute(content3)

                                    c_in_data.execute(content1)

                                    db.commit()

                                    test_val = 3

                                    messagebox.showinfo("success", "Successfully reserved...")

                            if test_val == 0:
                                messagebox.showwarning("Warning", "Please register first")"""
                                
                    def clear_1():
                        rf_et1.delete(0, END)
                        rf_et2_1.delete(0, END)
                        rf_et2_2.delete(0, END)
                        rf_et3_1.delete(0, END)
                        rf_et3_2.delete(0, END)
                        spinvar2.set("None")
                        spinvar3.set("None")
                        rf_et5_1.delete(0, END)
                        rf_et5_2.delete(0, END)
                        rf_et6_1.delete(0, END)
                        rf_et6_2.delete(0, END)
                        rf_et7_1.delete(0, END)
                        rf_et7_2.delete(0, END)
                        spinvar4.set("None")

                    rf_b1 = Button(rf_lf1, text="Reserve", command=checkin_2, font=("bold", 16),
                                   activeforeground="white",
                                   activebackground="black", width=20)
                    rf_b1.place(x=235, y=675)

                    rf_b2 = Button(rf_lf1, text="Clear", command=clear_1, font=("bold", 16), activeforeground="white",
                                   activebackground="blue", width=20)
                    rf_b2.place(x=635, y=675)

                Button(left_frame, text="Reservation", command=reservation1, width=15).place(x=90, y=250)
