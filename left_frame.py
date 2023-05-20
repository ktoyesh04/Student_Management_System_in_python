from datetime import datetime
from tkinter import *
from tkinter import ttk, messagebox, filedialog

import pandas

entry_objects = []


def get_details(title, button_text, command, rf):

    if button_text == 'Update':
        indexing = rf.student_table.focus()
        if indexing == '':
            messagebox.showwarning(title='Error', message='Select a record!')
            return

    global entry_objects
    window = Toplevel()
    window.geometry('+50+80')
    window.resizable(False, False)
    window.grab_set()
    window.title(title)

    id_label = ttk.Label(window, text='Id', font=('times new roman', 16, 'bold'))
    id_label.grid(row=0, column=0, padx=20, pady=10, sticky=W)

    id_entry = ttk.Entry(window, font=('times new roman', 16, 'bold'), width=30, show='')
    id_entry.grid(row=0, column=1, padx=20, pady=10, sticky=W)
    id_entry.focus_set()

    name_label = ttk.Label(window, text='Name', font=('times new roman', 16, 'bold'))
    name_label.grid(row=1, column=0, padx=20, pady=10, sticky=W)

    name_entry = ttk.Entry(window, font=('times new roman', 16, 'bold'), width=30, show='')
    name_entry.grid(row=1, column=1, padx=20, pady=10, sticky=W)
    id_entry.bind('<Return>', lambda e: name_entry.focus_set())

    gender_label = ttk.Label(window, text='Gender', font=('times new roman', 16, 'bold'))
    gender_label.grid(row=2, column=0, padx=20, pady=10, sticky=W)

    gender_entry = ttk.Entry(window, font=('times new roman', 16, 'bold'), width=30, show='')
    gender_entry.grid(row=2, column=1, padx=20, pady=10, sticky=W)
    name_entry.bind('<Return>', lambda e: gender_entry.focus_set())

    phone_label = ttk.Label(window, text='Phone', font=('times new roman', 16, 'bold'))
    phone_label.grid(row=3, column=0, padx=20, pady=10, sticky=W)

    phone_entry = ttk.Entry(window, font=('times new roman', 16, 'bold'), width=30, show='')
    phone_entry.grid(row=3, column=1, padx=20, pady=10, sticky=W)
    gender_entry.bind('<Return>', lambda e: phone_entry.focus_set())

    email_label = ttk.Label(window, text='Email', font=('times new roman', 16, 'bold'))
    email_label.grid(row=4, column=0, padx=20, pady=10, sticky=W)

    email_entry = ttk.Entry(window, font=('times new roman', 16, 'bold'), width=30, show='')
    email_entry.grid(row=4, column=1, padx=20, pady=10, sticky=W)
    phone_entry.bind('<Return>', lambda e: email_entry.focus_set())

    dob_label = ttk.Label(window, text='DOB', font=('times new roman', 16, 'bold'))
    dob_label.grid(row=5, column=0, padx=20, pady=10, sticky=W)

    dob_entry = ttk.Entry(window, font=('times new roman', 16, 'bold'), width=30, show='')
    dob_entry.grid(row=5, column=1, padx=20, pady=10, sticky=W)
    email_entry.bind('<Return>', lambda e: dob_entry.focus_set())

    entry_objects = [id_entry, name_entry, gender_entry, phone_entry,
                     email_entry, dob_entry, window]
    if button_text == 'Update':
        content = rf.student_table.item(indexing)

        list_data = content['values']
        for i in range(len(entry_objects) - 2):
            if i == 3:
                entry_objects[3].insert(0, '+' + str(list_data[3]))
            else:
                entry_objects[i].insert(0, list_data[i])
        entry_objects[-2].insert(0, datetime.strptime(list_data[-2], '%Y-%m-%d').strftime('%d-%m-%Y'))
        entry_objects[0].config(state=DISABLED)

    button = ttk.Button(window, text=button_text, command=command)
    button.grid(row=7, columnspan=2, pady=10)


class LeftFrame:

    def __init__(self, root, rt_frame):
        self.root = root
        self.rf = rt_frame
        self.left_frame = ttk.Frame(root)
        self.left_frame.place(x=50, y=80, width=140, height=600)

        self.logo_image = PhotoImage(file='admin.png')
        self.logo_label = ttk.Label(self.left_frame, image=self.logo_image)
        self.logo_label.grid(row=0, column=0, columnspan=2)

        self.add_student_button = ttk.Button(self.left_frame, text='Add Student',
                                             width=14, state=NORMAL,
                                             command=lambda: get_details('Add Student', 'Add', self.add_student, None))
        self.add_student_button.grid(row=1, column=0, pady=20)

        self.search_student_button = ttk.Button(self.left_frame, text='Search Student', width=14, state=NORMAL,
                                                command=lambda: get_details('Search Student(s)', 'Search',
                                                                            self.search_student, None))
        self.search_student_button.grid(row=2, column=0, pady=20)

        self.update_student_button = ttk.Button(self.left_frame, text='Update Student', width=14, state=NORMAL,
                                                command=lambda: get_details('Update Student', 'Update', self.update_student,
                                                                    self.rf))
        self.update_student_button.grid(row=3, column=0, pady=20)

        self.delete_student_button = ttk.Button(self.left_frame, text='Delete Student', width=14, state=NORMAL,
                                                command=self.rf.delete_student)
        self.delete_student_button.grid(row=4, column=0, pady=20)

        self.show_student_button = ttk.Button(self.left_frame, text='Show Student', width=14, state=NORMAL,
                                              command=self.rf.get_data)
        self.show_student_button.grid(row=5, column=0, pady=20)

        self.export_button = ttk.Button(self.left_frame, text='Export Data', width=14, state=NORMAL,
                                        command=self.export_data)
        self.export_button.grid(row=6, column=0, pady=20)

    def add_student(self):
        entries = [obj.get() for obj in entry_objects[:-1]]
        if "" in entries:
            messagebox.showerror(title='Error', message='Fields are Empty!')
            entry_objects[1][0].focus_set()
        else:
            entries[-1] = datetime.strptime(entries[-1], '%d-%m-%Y').strftime('%Y-%m-%d')
            if self.rf.add_data('student', entries):
                title = 'Success'
                message = 'Student Successfully Added!'
            else:
                title = 'Failure'
                message = ''
            result = messagebox.askyesno(title=f'{title}',
                                         message=f'{message}\nClear the fields')
            self.rf.get_data()
            print(entries)
            if result:
                for obj in entry_objects[:-1]:
                    obj.delete(0, END)

    def search_student(self):
        entries = [obj.get() for obj in entry_objects[:-1]]
        entries[1] = entries[1].title()
        entries[2] = entries[2].title()
        if entries[5] != "":
            entries[5] = f"{datetime.strptime(entries[5], '%d-%m-%Y').strftime('%Y-%m-%d')}"
        else:
            entries[5] = None
        self.rf.search_data(entries=tuple(entries))

    def update_student(self):

        window = entry_objects[-1]
        entries = [entry.get() for entry in entry_objects[:-1]]
        entries[1] = entries[1].title()
        entries[2] = entries[2].title()
        entries[-1] = datetime.strptime(entries[-1], '%d-%m-%Y').strftime('%Y-%m-%d')
        query_entries = tuple(entries[1:]+[entries[0]])
        print(query_entries)
        if self.rf.update_and_show(query_entries):
            messagebox.showinfo('Success', f'Id {entries[0]} is modified successfully', parent=window)
            window.destroy()

    def export_data(self):

        url = filedialog.asksaveasfilename(defaultextension='.csv')
        indexing = self.rf.student_table.get_children()
        new_list = []
        for index in indexing:
            content = self.rf.student_table.item(index)
            data_list = content['values']
            new_list.append(data_list)

        table = pandas.DataFrame(new_list,
                                 columns=['Id', 'Name', 'Mobile', 'Email', 'Gender', 'DOB', 'Added Date'])
        table.to_csv(url, index=False)
        messagebox.showinfo('Success', 'Data is saved successfully')
