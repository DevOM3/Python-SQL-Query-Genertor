from tkinter import *
from tkinter import simpledialog
from tkinter.messagebox import askyesno, askquestion, showerror


def show_sidebar():
    def create_query_clicked():
        table_name = simpledialog.askstring(title="Create Table", prompt="Enter a Table name")
        if table_name is not None and table_name != "":
            keys = [StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(),
                    StringVar(), StringVar(), StringVar(), ]
            values = [StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(),
                      StringVar(), StringVar(), StringVar(), ]

            def create_table_for_fields():
                field_table_frame = Frame(enter_table_fields, bg="black")
                field_table_frame.pack(fill=X, padx=7)

                Label(field_table_frame, text="Column Names", fg="white", bg="black").grid(row=0, column=1)
                Label(field_table_frame, text="Column Data-Types", fg="white", bg="black").grid(row=0, column=2)
                field0 = Entry(field_table_frame, width=39, textvariable=keys[0])
                field0.grid(row=1, column=1, padx=2, pady=2)
                value0 = Entry(field_table_frame, width=39, textvariable=values[0])
                value0.grid(row=1, column=2, padx=2, pady=2)
                field1 = Entry(field_table_frame, width=39, textvariable=keys[1])
                field1.grid(row=2, column=1, padx=2, pady=2)
                value1 = Entry(field_table_frame, width=39, textvariable=values[1])
                value1.grid(row=2, column=2, padx=2, pady=2)
                field2 = Entry(field_table_frame, width=39, textvariable=keys[2])
                field2.grid(row=3, column=1, padx=2, pady=2)
                value2 = Entry(field_table_frame, width=39, textvariable=values[2])
                value2.grid(row=3, column=2, padx=2, pady=2)
                field3 = Entry(field_table_frame, width=39, textvariable=keys[3])
                field3.grid(row=4, column=1, padx=2, pady=2)
                value3 = Entry(field_table_frame, width=39, textvariable=values[3])
                value3.grid(row=4, column=2, padx=2, pady=2)
                field4 = Entry(field_table_frame, width=39, textvariable=keys[4])
                field4.grid(row=5, column=1, padx=2, pady=2)
                value4 = Entry(field_table_frame, width=39, textvariable=values[4])
                value4.grid(row=5, column=2, padx=2, pady=2)
                field5 = Entry(field_table_frame, width=39, textvariable=keys[5])
                field5.grid(row=6, column=1, padx=2, pady=2)
                value5 = Entry(field_table_frame, width=39, textvariable=values[5])
                value5.grid(row=6, column=2, padx=2, pady=2)
                field6 = Entry(field_table_frame, width=39, textvariable=keys[6])
                field6.grid(row=7, column=1, padx=2, pady=2)
                value6 = Entry(field_table_frame, width=39, textvariable=values[6])
                value6.grid(row=7, column=2, padx=2, pady=2)
                field7 = Entry(field_table_frame, width=39, textvariable=keys[7])
                field7.grid(row=8, column=1, padx=2, pady=2)
                value7 = Entry(field_table_frame, width=39, textvariable=values[7])
                value7.grid(row=8, column=2, padx=2, pady=2)
                field8 = Entry(field_table_frame, width=39, textvariable=keys[8])
                field8.grid(row=9, column=1, padx=2, pady=2)
                value8 = Entry(field_table_frame, width=39, textvariable=values[8])
                value8.grid(row=9, column=2, padx=2, pady=2)
                field9 = Entry(field_table_frame, width=39, textvariable=keys[9])
                field9.grid(row=10, column=1, padx=2, pady=2)
                value9 = Entry(field_table_frame, width=39, textvariable=values[9])
                value9.grid(row=10, column=2, padx=2, pady=2)

            def field_save_button_clicked():
                key_check = []
                value_check = []
                for i in range(10):
                    key_check.append(keys[i].get() == "")
                    value_check.append(values[i].get() == "")

                if key_check == value_check:
                    columns = []
                    datatype = []
                    create_query = True

                    for key in keys:
                        if key.get() != "":
                            columns.append(key.get())
                    for value in values:
                        if value.get() != "":
                            if value.get().lower().__contains__("text") or value.get().lower().__contains__("string") \
                                    or value.get().lower().__contains__("char"):
                                datatype.append("TEXT")
                            elif value.get().lower().__contains__("time") or value.get().lower().__contains__("date"):
                                datatype.append("DATETIME")
                            elif value.get().lower().__contains__("int") or value.get().lower().__contains__("number"):
                                datatype.append("INTEGER(255)")
                            elif value.get().lower().__contains__("true") or value.get().lower().__contains__("false") \
                                    or value.get().lower().__contains__("bool"):
                                datatype.append("BOOLEAN")
                            elif value.get().lower().__contains__("float") or \
                                    value.get().lower().__contains__("double") or \
                                    value.get().lower().__contains__("decimal"):
                                datatype.append("FLOAT(11, 7)")

                        else:
                            if value.get() != "":
                                showerror("Error", f"Wrong Datatype: {value.get()}")
                                columns.clear()
                                datatype.clear()
                                create_query = False
                                break

                    if create_query:
                        query_field_string = ""
                        for i in range(datatype.__len__()):
                            query_field_string = f"{query_field_string}{'' if query_field_string == '' else ','} " \
                                                 f"{columns[i]} {datatype[i]}"
                        query.config(text=f"CREATE TABLE {table_name} ({query_field_string});")
                        query["text"] = f"CREATE TABLE {table_name} ({query_field_string});"
                        columns.clear()
                        datatype.clear()
                        enter_table_fields.destroy()
                        toggle_copy_button(True)
                else:
                    showerror("Error", "Your fields are not identical")

            enter_table_fields = Toplevel(root)
            enter_table_fields.title(f"Enter fields for {table_name}")
            enter_table_fields.wm_maxsize(500, 300)
            enter_table_fields.wm_minsize(500, 300)

            Label(enter_table_fields, text="Enter column names and data-types").pack()

            create_table_for_fields()

            save_button = Button(enter_table_fields, text="Create Table", relief=SUNKEN, activebackground="lightblue",
                                 command=field_save_button_clicked)
            save_button.pack(side=BOTTOM, fill=X, padx=7)

            enter_table_fields.mainloop()

    def insert_query_button_clicked():
        table_name = simpledialog.askstring(title="Update Table", prompt="Enter a Table name")
        if table_name is not None and table_name != "":
            keys = [StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(),
                    StringVar(), StringVar(), StringVar(), ]
            values = [StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(),
                      StringVar(), StringVar(), StringVar(), ]

            def create_table_for_fields():
                field_table_frame = Frame(enter_table_fields, bg="black")
                field_table_frame.pack(fill=X, padx=7)

                Label(field_table_frame, text="Column Names", fg="white", bg="black").grid(row=0, column=1)
                Label(field_table_frame, text="Values", fg="white", bg="black").grid(row=0, column=2)
                field0 = Entry(field_table_frame, width=39, textvariable=keys[0])
                field0.grid(row=1, column=1, padx=2, pady=2)
                value0 = Entry(field_table_frame, width=39, textvariable=values[0])
                value0.grid(row=1, column=2, padx=2, pady=2)
                field1 = Entry(field_table_frame, width=39, textvariable=keys[1])
                field1.grid(row=2, column=1, padx=2, pady=2)
                value1 = Entry(field_table_frame, width=39, textvariable=values[1])
                value1.grid(row=2, column=2, padx=2, pady=2)
                field2 = Entry(field_table_frame, width=39, textvariable=keys[2])
                field2.grid(row=3, column=1, padx=2, pady=2)
                value2 = Entry(field_table_frame, width=39, textvariable=values[2])
                value2.grid(row=3, column=2, padx=2, pady=2)
                field3 = Entry(field_table_frame, width=39, textvariable=keys[3])
                field3.grid(row=4, column=1, padx=2, pady=2)
                value3 = Entry(field_table_frame, width=39, textvariable=values[3])
                value3.grid(row=4, column=2, padx=2, pady=2)
                field4 = Entry(field_table_frame, width=39, textvariable=keys[4])
                field4.grid(row=5, column=1, padx=2, pady=2)
                value4 = Entry(field_table_frame, width=39, textvariable=values[4])
                value4.grid(row=5, column=2, padx=2, pady=2)
                field5 = Entry(field_table_frame, width=39, textvariable=keys[5])
                field5.grid(row=6, column=1, padx=2, pady=2)
                value5 = Entry(field_table_frame, width=39, textvariable=values[5])
                value5.grid(row=6, column=2, padx=2, pady=2)
                field6 = Entry(field_table_frame, width=39, textvariable=keys[6])
                field6.grid(row=7, column=1, padx=2, pady=2)
                value6 = Entry(field_table_frame, width=39, textvariable=values[6])
                value6.grid(row=7, column=2, padx=2, pady=2)
                field7 = Entry(field_table_frame, width=39, textvariable=keys[7])
                field7.grid(row=8, column=1, padx=2, pady=2)
                value7 = Entry(field_table_frame, width=39, textvariable=values[7])
                value7.grid(row=8, column=2, padx=2, pady=2)
                field8 = Entry(field_table_frame, width=39, textvariable=keys[8])
                field8.grid(row=9, column=1, padx=2, pady=2)
                value8 = Entry(field_table_frame, width=39, textvariable=values[8])
                value8.grid(row=9, column=2, padx=2, pady=2)
                field9 = Entry(field_table_frame, width=39, textvariable=keys[9])
                field9.grid(row=10, column=1, padx=2, pady=2)
                value9 = Entry(field_table_frame, width=39, textvariable=values[9])
                value9.grid(row=10, column=2, padx=2, pady=2)

            def field_save_button_clicked():
                key_check = []
                value_check = []
                for i in range(10):
                    key_check.append(keys[i].get() == "")
                    value_check.append(values[i].get() == "")

                if key_check == value_check:
                    columns = []
                    datatype = []
                    create_query = True

                    for key in keys:
                        if key.get() != "":
                            columns.append(key.get())
                    for value in values:
                        if value.get() != "":
                            if not value.get().isdigit():
                                datatype.append(f'"{value.get()}"')
                            else:
                                datatype.append(value.get())

                        else:
                            if value.get() != "":
                                columns.clear()
                                datatype.clear()
                                create_query = False
                                break

                    if create_query:
                        column_field_string = ""
                        value_field_string = ""
                        for i in range(datatype.__len__()):
                            column_field_string = f"{column_field_string}{'' if column_field_string == '' else ', '}" \
                                                  f"{columns[i]}"
                        for i in range(datatype.__len__()):
                            value_field_string = f"{value_field_string}{'' if value_field_string == '' else ', '}" \
                                                 f"{datatype[i]}"
                        query.config(text=f"INSERT INTO {table_name}({column_field_string}) "
                                          f"VALUES({value_field_string});")
                        query["text"] = f"INSERT INTO {table_name}({column_field_string}) VALUES({value_field_string});"
                        columns.clear()
                        datatype.clear()
                        enter_table_fields.destroy()
                        toggle_copy_button(True)
                else:
                    showerror("Error", "Your fields are not identical")

            enter_table_fields = Toplevel(root)
            enter_table_fields.title(f"Enter fields for {table_name}")
            enter_table_fields.wm_maxsize(500, 300)
            enter_table_fields.wm_minsize(500, 300)

            Label(enter_table_fields, text="Enter column names and data-types").pack()

            create_table_for_fields()

            save_button = Button(enter_table_fields, text="Create Table", relief=SUNKEN, activebackground="lightblue",
                                 command=field_save_button_clicked)
            save_button.pack(side=BOTTOM, fill=X, padx=7)

            enter_table_fields.mainloop()

    def update_query_button_clicked():
        table_name = simpledialog.askstring(title="Update Table", prompt="Enter a Table name")
        if table_name is not None and table_name != "":
            keys = [StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(),
                    StringVar(), StringVar(), StringVar(), ]
            values = [StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(),
                      StringVar(), StringVar(), StringVar(), ]

            def create_table_for_fields():
                field_table_frame = Frame(enter_table_fields, bg="black")
                field_table_frame.pack(fill=X, padx=7)

                Label(field_table_frame, text="Column Names", fg="white", bg="black").grid(row=0, column=1)
                Label(field_table_frame, text="Value to set", fg="white", bg="black").grid(row=0, column=2)
                field0 = Entry(field_table_frame, width=39, textvariable=keys[0])
                field0.grid(row=1, column=1, padx=2, pady=2)
                value0 = Entry(field_table_frame, width=39, textvariable=values[0])
                value0.grid(row=1, column=2, padx=2, pady=2)
                field1 = Entry(field_table_frame, width=39, textvariable=keys[1])
                field1.grid(row=2, column=1, padx=2, pady=2)
                value1 = Entry(field_table_frame, width=39, textvariable=values[1])
                value1.grid(row=2, column=2, padx=2, pady=2)
                field2 = Entry(field_table_frame, width=39, textvariable=keys[2])
                field2.grid(row=3, column=1, padx=2, pady=2)
                value2 = Entry(field_table_frame, width=39, textvariable=values[2])
                value2.grid(row=3, column=2, padx=2, pady=2)
                field3 = Entry(field_table_frame, width=39, textvariable=keys[3])
                field3.grid(row=4, column=1, padx=2, pady=2)
                value3 = Entry(field_table_frame, width=39, textvariable=values[3])
                value3.grid(row=4, column=2, padx=2, pady=2)
                field4 = Entry(field_table_frame, width=39, textvariable=keys[4])
                field4.grid(row=5, column=1, padx=2, pady=2)
                value4 = Entry(field_table_frame, width=39, textvariable=values[4])
                value4.grid(row=5, column=2, padx=2, pady=2)
                field5 = Entry(field_table_frame, width=39, textvariable=keys[5])
                field5.grid(row=6, column=1, padx=2, pady=2)
                value5 = Entry(field_table_frame, width=39, textvariable=values[5])
                value5.grid(row=6, column=2, padx=2, pady=2)
                field6 = Entry(field_table_frame, width=39, textvariable=keys[6])
                field6.grid(row=7, column=1, padx=2, pady=2)
                value6 = Entry(field_table_frame, width=39, textvariable=values[6])
                value6.grid(row=7, column=2, padx=2, pady=2)
                field7 = Entry(field_table_frame, width=39, textvariable=keys[7])
                field7.grid(row=8, column=1, padx=2, pady=2)
                value7 = Entry(field_table_frame, width=39, textvariable=values[7])
                value7.grid(row=8, column=2, padx=2, pady=2)
                field8 = Entry(field_table_frame, width=39, textvariable=keys[8])
                field8.grid(row=9, column=1, padx=2, pady=2)
                value8 = Entry(field_table_frame, width=39, textvariable=values[8])
                value8.grid(row=9, column=2, padx=2, pady=2)
                field9 = Entry(field_table_frame, width=39, textvariable=keys[9])
                field9.grid(row=10, column=1, padx=2, pady=2)
                value9 = Entry(field_table_frame, width=39, textvariable=values[9])
                value9.grid(row=10, column=2, padx=2, pady=2)

            def field_save_button_clicked():
                key_check = []
                value_check = []
                for i in range(10):
                    key_check.append(keys[i].get() == "")
                    value_check.append(values[i].get() == "")

                if key_check == value_check:
                    columns = []
                    datatype = []
                    create_query = True

                    for key in keys:
                        if key.get() != "":
                            columns.append(key.get())
                    for value in values:
                        if value.get() != "":
                            if not value.get().isdigit():
                                datatype.append(f'"{value.get()}"')
                            else:
                                datatype.append(value.get())

                        else:
                            if value.get() != "":
                                columns.clear()
                                datatype.clear()
                                create_query = False
                                break

                    if create_query:
                        query_field_string = ""
                        for i in range(datatype.__len__()):
                            query_field_string = f"{query_field_string}{'' if query_field_string == '' else ', '}"\
                                                 f"{columns[i]}={datatype[i]}"
                        query.config(text=f"UPDATE TABLE {table_name} SET {query_field_string};")
                        query["text"] = f"UPDATE TABLE {table_name} SET {query_field_string};"
                        columns.clear()
                        datatype.clear()
                        enter_table_fields.destroy()
                        toggle_copy_button(True)
                else:
                    showerror("Error", "Your fields are not identical")

            enter_table_fields = Toplevel(root)
            enter_table_fields.title(f"Enter fields for {table_name}")
            enter_table_fields.wm_maxsize(500, 300)
            enter_table_fields.wm_minsize(500, 300)

            Label(enter_table_fields, text="Enter column names and data-types").pack()

            create_table_for_fields()

            save_button = Button(enter_table_fields, text="Create Table", relief=SUNKEN, activebackground="lightblue",
                                 command=field_save_button_clicked)
            save_button.pack(side=BOTTOM, fill=X, padx=7)

            enter_table_fields.mainloop()

    def delete_query_button_clicked():
        yes_no = askyesno("Delete", "Do you want to delete all records?")
        if yes_no:
            sure_to_delete_all_records = askquestion("Delete all Records", "Are sure to delete all records?",
                                                     icon="warning")
            if sure_to_delete_all_records.lower() == "yes":
                table_name = simpledialog.askstring(title="Drop Table", prompt="Which table you want to Drop?")
                query.config(text=f"DELETE FROM {table_name};")
                query["text"] = f"DELETE FROM {table_name};"
                toggle_copy_button(True)
        else:
            table_name = simpledialog.askstring(title="Table name", prompt="Enter a Table name")
            if table_name != "" and table_name is not None:
                condition = simpledialog.askstring(title="Condition",
                                                   prompt="Enter a condition (condition in SQL is similar to other "
                                                          "programming languages and is in the form of column=value "
                                                          "having '=', '!=', '<' '>', etc.)")
                if condition.__contains__('=') or condition.__contains__('!=') or condition.__contains__('<') or \
                        condition.__contains__('<=') or condition.__contains__('>') or condition.__contains__('>=') or \
                        condition.__contains__('<>'):
                    query.config(text=f"DELETE FROM {table_name} WHERE {condition};")
                    query["text"] = f"DELETE FROM {table_name} WHERE {condition};"
                    toggle_copy_button(True)

    def drop_table_button_clicked():
        table_name = simpledialog.askstring(title="Drop Table", prompt="Which table you want to Drop?")
        if table_name is not None and table_name != "":
            table_name = table_name.replace(" ", "_")
            query.config(text=f"DROP TABLE {table_name};")
            query["text"] = f"DROP TABLE {table_name};"
            toggle_copy_button(True)
        else:
            toggle_copy_button(False)

    def clear_button_clicked():
        query.config(text="")
        query["text"] = ""
        copy_button.pack_forget()

    def clear_button_enter(e):
        clear_button["bg"] = "red"
        clear_button["height"] = 3

    def clear_button_leave(e):
        clear_button["bg"] = "tomato"
        clear_button["height"] = 2

    def exit_button_enter(e):
        exit_button["bg"] = "red"
        exit_button["height"] = 3

    def exit_button_leave(e):
        exit_button["bg"] = "tomato"
        exit_button["height"] = 2

    sidebar = Frame(root, bg="gray")
    sidebar.pack(fill=Y, side=LEFT)

    create_query_button = Button(sidebar, text="Create Table Query", activebackground="lightgreen", width=21, height=4,
                                 relief=SUNKEN, command=create_query_clicked)
    create_query_button.pack(padx=4, pady=4, anchor="n")

    insert_query_button = Button(sidebar, text="Insert Query", activebackground="lightgreen", width=21, height=4,
                                 relief=SUNKEN, command=insert_query_button_clicked)
    insert_query_button.pack(padx=4, pady=4, anchor="n")

    update_query_button = Button(sidebar, text="Update Query", activebackground="lightgreen", width=21, height=4,
                                 relief=SUNKEN, command=update_query_button_clicked)
    update_query_button.pack(padx=4, pady=4, anchor="n")

    delete_query_button = Button(sidebar, text="Delete Query", activebackground="lightgreen", width=21, height=4,
                                 relief=SUNKEN, command=delete_query_button_clicked)
    delete_query_button.pack(padx=4, pady=4, anchor="n")

    drop_table_query_button = Button(sidebar, text="Drop Table Query", activebackground="lightgreen", width=21,
                                     height=4, relief=SUNKEN, command=drop_table_button_clicked)

    exit_button = Button(sidebar, text="Exit", bg="tomato", activebackground="red", width=21, height=2, relief=SUNKEN,
                         command=exit)
    exit_button.pack(padx=4, pady=4, side=BOTTOM)
    exit_button.bind("<Enter>", exit_button_enter)
    exit_button.bind("<Leave>", exit_button_leave)

    drop_table_query_button.pack(padx=4, pady=4, anchor="n")

    clear_button = Button(sidebar, text="Reset", bg="tomato", activebackground="red", width=21, height=2, relief=SUNKEN,
                          command=clear_button_clicked)
    clear_button.pack(padx=4, pady=4, side=BOTTOM)
    clear_button.bind("<Enter>", clear_button_enter)
    clear_button.bind("<Leave>", clear_button_leave)


def copy_query():
    root.clipboard_clear()
    root.clipboard_append(query.cget("text"))
    root.update()


def toggle_copy_button(toggle):
    copy_button.pack(side=BOTTOM, fill=X) if toggle else copy_button.pack_forget()


def copy_button_enter(e):
    copy_button["bg"] = "lightblue"
    copy_button["height"] = 2


def copy_button_leave(e):
    copy_button["bg"] = "white"
    copy_button["height"] = 1


root = Tk()
root.title("SQL Query Generator")
root.geometry("1000x700")

show_sidebar()

query_frame = LabelFrame(root, text="Resultant Query", font=11)
query_frame.pack(fill=BOTH, expand=1, padx=11, pady=11)

query = Label(query_frame, text="vhjb", font=7, wraplength=501, fg="gray")
query.pack()

copy_button = Button(query_frame, text="Copy to clipboard", relief=SUNKEN, activebackground="lightgreen",
                     command=copy_query, bg="white", height=1)
copy_button.pack(side=BOTTOM, fill=X) if query.cget("text") != "" else copy_button.pack_forget()
copy_button.bind("<Enter>", copy_button_enter)
copy_button.bind("<Leave>", copy_button_leave)

root.mainloop()
