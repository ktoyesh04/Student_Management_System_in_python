from tkinter import *
from PIL import ImageTk
from tkinter import messagebox


class Login:

    @staticmethod
    def main():

        # Function to handle the login button click event
        def login():
            if username_entry.get() == "" or password_entry.get() == "":
                messagebox.showerror(title='Error', message='Fields cannot be empty!')
            elif username_entry.get() == 'admin' and password_entry.get() == 'admin':
                messagebox.showinfo('Success', 'Welcome!')
                window.destroy()
                import admin
            else:
                messagebox.showerror(title='Error', message='Invalid username or password')

        # Function to toggle the visibility of the password entry field
        def toggle_password():
            if password_entry.cget('show') == '':
                password_entry.config(show='*')
                toggle_password_button.config(image=show_password)
            else:
                password_entry.config(show='')
                toggle_password_button.config(image=hide_password)

        # Create the main window
        window = Tk()
        window.title('Login System')
        window.geometry('1400x700+50+50')
        window.resizable(False, False)

         # Load the background image
        bg_image = ImageTk.PhotoImage(file=r'media\bg.jpg')

        # Create a label to display the background image
        bg_label = Label(window, image=bg_image)
        bg_label.place(x=0, y=0)

        # Create a frame for the login section
        login_frame = Frame(window, bg='#f5f5f7')
        login_frame.place(x=450, y=300)

        # Load and display the logo image
        logo_img = ImageTk.PhotoImage(file=r'media\logo.jpg')
        logo_label = Label(login_frame, image=logo_img)
        logo_label.grid(column=0, row=0, columnspan=2, pady=10)

        # Create the username label and entry field
        username_logo = PhotoImage(file=r'media\username.png')
        username_label = Label(login_frame, image=username_logo, bg='#f5f5f7', text='Username',
                               font=('times new roman', 18, 'bold'), compound=LEFT)
        username_label.grid(column=0, row=1, padx=10, pady=10)
        username_entry = Entry(login_frame, font=('times new roman', 18, 'bold'),
                               bg='#f5f5f7', bd=4, )
        username_entry.focus_set()
        username_entry.insert(0, 'admin')
        username_entry.grid(row=1, column=1, padx=20, pady=10)

        # Create the password label and entry field
        password_logo = PhotoImage(file=r'media\password.png')
        password_label = Label(login_frame, image=password_logo, bg='#f5f5f7', text='Password',
                               font=('times new roman', 18, 'bold'), compound=LEFT)
        password_label.grid(column=0, row=2, padx=20, pady=10)
        password_entry = Entry(login_frame, font=('times new roman', 18, 'bold'),
                               bg='#f5f5f7', bd=4, show='*')
        password_entry.insert(0, 'admin')
        password_entry.grid(row=2, column=1, padx=20, pady=10)

        # Create the login button
        login_button = Button(login_frame, text='Login', font=('times new roman', 18, 'bold'),
                              bg='#f5f5f7', bd=4, cursor='hand2', command=login)
        login_button.grid(row=3, column=1, pady=10)

        # Load the show/hide password icons
        show_password = PhotoImage(file=r'media\show_password.png')
        hide_password = PhotoImage(file=r'media\hide_password.png')

        # Create the toggle password visibility button
        toggle_password_button = Button(login_frame, image=show_password, command=toggle_password)
        toggle_password_button.grid(row=2, column=2)

        # Bind the Enter key press event to focus on the password entry field
        username_entry.bind('<Return>', lambda e: password_entry.focus_set())

        # Bind the Enter key press event to the login function
        password_entry.bind('<Return>', lambda e: login())

        # Start the main event loop
        window.mainloop()

if __name__ == '__main__':
    Login.main()
    