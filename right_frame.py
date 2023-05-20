from tkinter import *
from tkinter import ttk, messagebox
import pymysql
from tkinter import messagebox


class RightFrame:
    def __init__(self, root):
        self.root = root
        self.connect_data_base()
        self.root = root
        self.column_sort_order = {}
        right_frame = ttk.Frame(root)
        right_frame.place(x=300, y=80, width=1040, height=600)

        scroll_bar_x = ttk.Scrollbar(right_frame, orient=HORIZONTAL)
        scroll_bar_y = ttk.Scrollbar(right_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(right_frame, columns=('Id', 'Name', 'Gender',
                                                                'Mobile', 'Email', 'DOB', 'Added Date'),
                                          xscrollcommand=scroll_bar_x.set, yscrollcommand=scroll_bar_y.set,
                                          show='headings')
        self.student_table.pack(fill=BOTH, expand=1)

        scroll_bar_x.config(command=self.student_table.xview)
        scroll_bar_y.config(command=self.student_table.yview)

        scroll_bar_x.pack(side=BOTTOM, fill=X)
        scroll_bar_y.pack(side=RIGHT, fill=Y)

        self.student_table.heading('Id', text='Id', command=lambda: self.sort_by_column('Id'))
        self.student_table.heading('Name', text='Name', command=lambda: self.sort_by_column('Name'))
        self.student_table.heading('Gender', text='Gender', command=lambda: self.sort_by_column('Gender'))
        self.student_table.heading('Mobile', text='Mobile', command=lambda: self.sort_by_column('Mobile'))
        self.student_table.heading('Email', text='Email', command=lambda: self.sort_by_column('Email'))
        self.student_table.heading('DOB', text='DOB', command=lambda: self.sort_by_column('DOB'))
        self.student_table.heading('Added Date', text='Added Date', command=lambda: self.sort_by_column('Added_Date'))

    def connect_data_base(self):
        entries = {'host': 'localhost', 'user': 'root', 'password': 'anjaneya78'}
        try:
            connection = pymysql.connect(host=entries['host'], user=entries['user'],
                                         password=entries['password'])
            cursor = connection.cursor()
        except Exception as e:
            print(e)
            messagebox.showerror(title='Error', message='Cannot Connect to data base')
            # return False
        else:
            self.my_cursor = cursor
            self.my_connection = connection
            cursor.execute('use sms1;')
            messagebox.showinfo(title='Success!',
                                message='Database connection is successful!')
        return True

    def show_data(self):
        self.student_table.delete(*self.student_table.get_children())
        fetched_data = self.my_cursor.fetchall()
        for data in fetched_data:
            data_list = list(data)
            self.student_table.insert('', END, values=data_list)

    def add_data(self, table, entries):
        query = f'INSERT INTO {table} VALUES('
        placeholders = ','.join(['%s'] * len(entries))
        query += placeholders + ', CURDATE())'
        try:
            self.my_cursor.execute(query, entries)
            self.my_connection.commit()
            self.get_data()
        except Exception as e:
            messagebox.showerror(title='Error', message=f'{e}')
            return False
        return True

    def get_data(self, table='student', order_by='added_date', order='ASC', condition='id!=0'):
        query = f"SELECT * FROM {table} WHERE {condition} ORDER BY {order_by} {order} "
        self.my_cursor.execute(query)
        self.show_data()

    def sort_by_column(self, column):
        if column in self.column_sort_order:
            if self.column_sort_order[column] == 'ASC':
                self.get_data(order_by=column, order='ASC')
                self.column_sort_order[column] = 'DESC'
            else:
                self.get_data(order_by=column, order='DESC')
                self.column_sort_order[column] = 'ASC'
        else:
            self.get_data(order_by=column, order='ASC')
            self.column_sort_order[column] = 'DESC'

    def search_data(self, entries):
        print(entries)
        query = 'SELECT * FROM STUDENT WHERE id=%s OR name=%s OR gender=%s OR mobile=%s OR email=%s OR dob=%s'
        print(query)
        self.my_cursor.execute(query, entries)
        self.show_data()

    def delete_student(self):
        indexing = self.student_table.focus()
        content = self.student_table.item(indexing)
        content_id = content['values'][0]
        query = 'DELETE FROM student WHERE id=%s'
        self.my_cursor.execute(query, content_id)
        self.my_connection.commit()
        self.get_data()
        messagebox.showinfo('Deleted', f'Id {content_id} is deleted successfully')

    def update_and_show(self, entries):
        query = 'update student set name=%s,gender=%s, mobile=%s,email=%s,dob=%s, added_date=CURDATE() where id=%s'
        try:
            self.my_cursor.execute(query, entries)
        except Exception as e:
            print(e)
            messagebox.showerror(title='Error', message=f'{e}')
            return False
        else:
            self.my_connection.commit()
            self.get_data()
            return True
