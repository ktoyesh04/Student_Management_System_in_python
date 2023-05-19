from datetime import datetime
from tkinter import *
from tkinter import ttk, messagebox

from admin.set import Student_Entries


class LeftFrame:

    def __init__(self, root, rf):
        self.root = root
        self.rf = rf
        self.left_frame = ttk.Frame(root)
        self.left_frame.place(x=50, y=80, width=162, height=600)

        self.logo_image = PhotoImage(file=r'admin.png')
        self.logo_label = ttk.Label(self.left_frame, image=self.logo_image)
        self.logo_label.grid(row=0, column=0, columnspan=2)

        self.add_student_button = ttk.Button(self.left_frame, text='Add Student',
                                             width=14, state=NORMAL, command=self.add_student)
        self.add_student_button.grid(row=1, column=0, pady=20)

        self.search_student_button = ttk.Button(self.left_frame, text='Search Student', width=14, state=NORMAL,
                                                command=self.search_student)
        self.search_student_button.grid(row=2, column=0, pady=20)

        self.update_student_button = ttk.Button(self.left_frame, text='Update Student', width=14, state=NORMAL)
        self.update_student_button.grid(row=3, column=0, pady=20)

        self.delete_student_button = ttk.Button(self.left_frame, text='Delete Student', width=14, state=NORMAL)
        self.delete_student_button.grid(row=4, column=0, pady=20)

        self.show_student_button = ttk.Button(self.left_frame, text='Show Student', width=14, state=NORMAL,
                                              command=self.rf.get_data)
        self.show_student_button.grid(row=5, column=0, pady=20)

        self.export_button = ttk.Button(self.left_frame, text='Export Data', width=14, state=NORMAL)
        self.export_button.grid(row=6, column=0, pady=20)

    # def enable_all_buttons(self):
    #     self.add_student_button.config(state=NORMAL)
    #     self.delete_student_button.config(state=NORMAL)
    #     self.export_button.config(state=NORMAL)
    #     self.search_student_button.config(state=NORMAL)
    #     self.show_student_button.config(state=NORMAL)
    #     self.update_student_button.config(state=NORMAL)

    def add_student(self):
        data = Student_Entries.get_details()
        data[0].title('Add Student')

        def check():

            entries = [obj.get() for obj in data[1]]
            if "" in entries:
                messagebox.showerror(parent=data[0], title='Error', message='Fields are Empty!')
                data[1][0].focus_set()
            else:
                entries[-1] = datetime.strptime(entries[-1], '%d-%m-%Y').strftime('%Y-%m-%d')
                if self.rf.add_data('student', entries):
                    title = 'Success'
                    message = 'Student Successfully Added!'
                else:
                    title = 'Failure'
                    message = ''
                result = messagebox.askyesno(parent=data[0], title=f'{title}',
                                             message=f'{message}\nClear the fields')

                self.rf.get_data()
                print(entries)
                if result:
                    for obj in data[1]:
                        obj.delete(0, END)

        button = ttk.Button(data[0], text=f'Add Student', command=check)
        button.grid(row=7, columnspan=2, pady=10)

    def search_student(self):
        data = Student_Entries.get_details()
        data[0].title('Search')

        def check():
            entries = [obj.get().title() for obj in data[1]]
            if all(entries) == "":
                messagebox.showerror(parent=data[0], title='Error', message='Fields are Empty!')
                data[1][0].focus_set()
            else:
                entries[4] = entries[4].lower()
                if entries[5] != "":
                    entries[5] = f"{datetime.strptime(entries[5], '%d-%m-%Y').strftime('%Y-%m-%d')}"
                else:
                    entries[5] = None
                self.rf.search_data(entries=tuple(entries))

        button = ttk.Button(data[0], text=f'Search', command=check)
        button.grid(row=7, columnspan=2, pady=10)
