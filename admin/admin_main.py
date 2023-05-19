import time
from PIL import ImageTk
import ttkthemes
from tkinter import *
from tkinter import ttk
from admin.right_frame import RightFrame
from admin.left_frame import LeftFrame


def clock():
    date = time.strftime('%d/%m/%Y')
    current_time = time.strftime('%H:%M:%S')
    datetime_label.config(text=f"Date: {date}\nTime: {current_time}")
    datetime_label.after(1000, clock)


count = 0
def slider():
    global count
    slider_label.config(text=text[:count + 1])
    if count == 25:
        count = 0
    else:
        count += 1
    slider_label.after(300, slider)


def return_to_login(self):
    root.destroy()


root = ttkthemes.ThemedTk()
root.title("Student Management System")
root.geometry('1400x700+50+50')
root.resizable(False, False)

root.get_themes()
root.set_theme('clearlooks')

datetime_label = ttk.Label(root, text="Time: ", font=('times new roman', 16, ''))
datetime_label.place(x=50, y=8)
clock()

# bg_img = ImageTk.PhotoImage(file='media/admin.jpg')
# bg_label = Label(self.root, image=bg_img)
# bg_label.place(x=60, y=10)

exit_button = ttk.Button(text='Exit', width=14, command=return_to_login)
exit_button.grid(row=7, column=0, pady=20)
exit_button.place(x=8, y=650)

text = "Student Management System"
slider_label = ttk.Label(root, text=text, font=('arial', 28, 'italic bold'), width=25)
slider_label.place(x=400, y=0)
count = 0
slider()

rf = RightFrame(root)
LeftFrame(root, rf)

root.mainloop()
