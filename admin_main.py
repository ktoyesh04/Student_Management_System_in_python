import time
from tkinter import ttk, messagebox
import ttkthemes

from left_frame import LeftFrame
from right_frame import RightFrame

# Define constants
SLIDER_DELAY = 300  # Delay for slider animation
SLIDER_TEXT = "Student Management System"


# Function to update the datetime label with current date and time
def update_datetime_label():
    current_date = time.strftime('%d/%m/%Y')
    current_time = time.strftime('%H:%M:%S')
    datetime_label.config(text=f"Date: {current_date}\nTime: {current_time}")
    datetime_label.after(1000, update_datetime_label)


# Function for the sliding text effect
def update_slider_label():
    global slider_index
    slider_label.config(text=SLIDER_TEXT[:slider_index + 1])
    slider_index = (slider_index + 1) % len(SLIDER_TEXT)
    slider_label.after(SLIDER_DELAY, update_slider_label)


# Function to handle program exit
def exit_program():
    result = messagebox.askyesno('Confirm', 'Do you want to exit?')
    if result:
        root.destroy()


root = ttkthemes.ThemedTk()
root.title("Student Management System")
root.geometry('1400x700+50+50')
root.resizable(False, False)
root.get_themes()
root.set_theme('clearlooks')

# Create the datetime label
datetime_label = ttk.Label(root, text="Time: ", font=('times new roman', 16, ''))
datetime_label.place(x=50, y=8)
update_datetime_label()

# Create the exit button
exit_button = ttk.Button(root, text='Exit', width=14, command=exit_program)
exit_button.place(x=8, y=650)

# Create the sliding label
slider_label = ttk.Label(root, text=SLIDER_TEXT, font=('arial', 28, 'italic bold'), width=25)
slider_label.place(x=400, y=0)
slider_index = 0
update_slider_label()

# Create the frames
rf = RightFrame(root)
LeftFrame(root, rf)

# Start the GUI event loop
root.mainloop()
