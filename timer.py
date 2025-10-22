import time
from tkinter import *
from tkinter import messagebox

# Initialize the main window
root = Tk()
root.geometry("400x300")
root.title("Countdown Timer")
root.config(bg='#345')

# Declaration of variables
hour = StringVar()
minute = StringVar()
second = StringVar()

# Setting the default value as 0
hour.set("00")
minute.set("00")
second.set("00")

# Using Entry widgets to take input from the user
hour_box = Entry(
    root,
    width=3,
    font=("Arial", 18, ""),
    textvariable=hour
)
hour_box.place(x=80, y=20)

mins_box = Entry(
    root,
    width=3,
    font=("Arial", 18, ""),
    textvariable=minute
)
mins_box.place(x=130, y=20)

sec_box = Entry(
    root,
    width=3,
    font=("Arial", 18, ""),
    textvariable=second
)
sec_box.place(x=180, y=20)

# Countdown timer function
def countdowntimer():
    try:
        # Convert user input to total seconds
        user_input = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
    except ValueError:
        messagebox.showwarning("", "Invalid Input! Please enter numeric values.")
        return

    while user_input > -1:
        mins, secs = divmod(user_input, 60)
        hours = 0
        if mins >= 60:
            hours, mins = divmod(mins, 60)

        # Update the variables
        hour.set("{:02d}".format(hours))
        minute.set("{:02d}".format(mins))
        second.set("{:02d}".format(secs))

        # Update the UI
        root.update()
        time.sleep(1)

        if user_input == 0:
            messagebox.showinfo("Time Countdown", "Time Over")
        user_input -= 1

# Button to start the timer
btn = Button(root, text='Set Time Countdown', bd='5', command=countdowntimer)
btn.place(x=80, y=120)

root.mainloop()