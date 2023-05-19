from tkinter import *
from PIL import ImageTk
from tkinter import messagebox


class Login:

    @staticmethod
    def main():

        def login():
            if username_entry.get() == "" or password_entry.get() == "":
                messagebox.showerror(title='Error', message='Fields cannot be empty!')
            elif username_entry.get() == 'admin' and password_entry.get() == 'admin':
                messagebox.showinfo('Success', 'Welcome!')
                window.destroy()
                import admin.admin_main
            else:
                messagebox.showerror(title='Error', message='Invalid username or password')

        def toggle_password():
            if password_entry.cget('show') == '':
                password_entry.config(show='*')
                toggle_password_button.config(image=show_password)
            else:
                password_entry.config(show='')
                toggle_password_button.config(image=hide_password)

        window = Tk()
        window.title('Login System')
        window.geometry('1400x700+50+50')
        window.resizable(False, False)
        bg_image = ImageTk.PhotoImage(file='bg.jpg')

        bg_label = Label(window, image=bg_image)
        bg_label.place(x=0, y=0)

        login_frame = Frame(window, bg='#f5f5f7')
        login_frame.place(x=450, y=300)

        logo_img = ImageTk.PhotoImage(file='logo.jpg')
        logo_label = Label(login_frame, image=logo_img)
        logo_label.grid(column=0, row=0, columnspan=2, pady=10)

        username_logo = PhotoImage(file='username.png')
        username_label = Label(login_frame, image=username_logo, bg='#f5f5f7', text='Username',
                               font=('times new roman', 18, 'bold'), compound=LEFT)
        username_label.grid(column=0, row=1, padx=10, pady=10)

        username_entry = Entry(login_frame, font=('times new roman', 18, 'bold'),
                               bg='#f5f5f7', bd=4, )
        username_entry.focus_set()
        username_entry.insert(0, 'admin')
        username_entry.grid(row=1, column=1, padx=20, pady=10)

        password_logo = PhotoImage(file='password.png')
        password_label = Label(login_frame, image=password_logo, bg='#f5f5f7', text='Password',
                               font=('times new roman', 18, 'bold'), compound=LEFT)
        password_label.grid(column=0, row=2, padx=20, pady=10)

        password_entry = Entry(login_frame, font=('times new roman', 18, 'bold'),
                               bg='#f5f5f7', bd=4, show='*')
        password_entry.insert(0, 'admin')
        password_entry.grid(row=2, column=1, padx=20, pady=10)

        login_button = Button(login_frame, text='Login', font=('times new roman', 18, 'bold'),
                              bg='#f5f5f7', bd=4, cursor='hand2', command=login)
        login_button.grid(row=3, column=1, pady=10)

        show_password = PhotoImage(file='show_password.png')
        hide_password = PhotoImage(file='hide_password.png')

        toggle_password_button = Button(login_frame, image=show_password, command=toggle_password)
        toggle_password_button.grid(row=2, column=2)

        username_entry.bind('<Return>', lambda e: password_entry.focus_set())
        password_entry.bind('<Return>', lambda e: login())

        window.mainloop()


if __name__ == '__main__':
    Login.main()
