from tkinter import ttk
from tkinter import *

class Student_Entries:

    @staticmethod
    def get_details():
        window = Toplevel()
        window.geometry('+50+80')
        window.resizable(False, False)
        window.grab_set()

        id_label = ttk.Label(window, text='Id', font=('times new roman', 16, 'bold'))
        id_label.grid(row=0, column=0, padx=20, pady=10, sticky=W)

        id_entry = ttk.Entry(window, font=('times new roman', 16, 'bold'), width=30)
        id_entry.grid(row=0, column=1, padx=20, pady=10, sticky=W)
        id_entry.focus_set()

        name_label = ttk.Label(window, text='Name', font=('times new roman', 16, 'bold'))
        name_label.grid(row=1, column=0, padx=20, pady=10, sticky=W)

        name_entry = ttk.Entry(window, font=('times new roman', 16, 'bold'), width=30)
        name_entry.grid(row=1, column=1, padx=20, pady=10, sticky=W)
        id_entry.bind('<Return>', lambda e: name_entry.focus_set())

        gender_label = ttk.Label(window, text='Gender', font=('times new roman', 16, 'bold'))
        gender_label.grid(row=2, column=0, padx=20, pady=10, sticky=W)

        gender_entry = ttk.Entry(window, font=('times new roman', 16, 'bold'), width=30)
        gender_entry.grid(row=2, column=1, padx=20, pady=10, sticky=W)
        name_entry.bind('<Return>', lambda e: gender_entry.focus_set())

        phone_label = ttk.Label(window, text='Phone', font=('times new roman', 16, 'bold'))
        phone_label.grid(row=3, column=0, padx=20, pady=10, sticky=W)

        phone_entry = ttk.Entry(window, font=('times new roman', 16, 'bold'), width=30)
        phone_entry.grid(row=3, column=1, padx=20, pady=10, sticky=W)
        gender_entry.bind('<Return>', lambda e: phone_entry.focus_set())

        email_label = ttk.Label(window, text='Email', font=('times new roman', 16, 'bold'))
        email_label.grid(row=4, column=0, padx=20, pady=10, sticky=W)

        email_entry = ttk.Entry(window, font=('times new roman', 16, 'bold'), width=30)
        email_entry.grid(row=4, column=1, padx=20, pady=10, sticky=W)
        phone_entry.bind('<Return>', lambda e: email_entry.focus_set())

        dob_label = ttk.Label(window, text='DOB', font=('times new roman', 16, 'bold'))
        dob_label.grid(row=5, column=0, padx=20, pady=10, sticky=W)

        dob_entry = ttk.Entry(window, font=('times new roman', 16, 'bold'), width=30)
        dob_entry.grid(row=5, column=1, padx=20, pady=10, sticky=W)
        email_entry.bind('<Return>', lambda e: dob_entry.focus_set())

        entry_objects = [id_entry, name_entry, gender_entry, phone_entry,
                         email_entry, dob_entry]
        return [window, entry_objects]