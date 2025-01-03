from tkinter import *

window = Tk()
window.title("A Simple Calculator App")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)
my_label = Label(text="Welcome!", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)


def new_button_clicked():
    print("New Button Clicked")


# new button 0,2
new_button = Button(text="New Button", width=10, command=new_button_clicked)
new_button.grid(column=2, row=0)

# Entry
user_input = Entry(width=10)
user_input.grid(column=3, row=2)


def get_user_input():
    my_label.config(text=user_input.get())


# Button

def button_click():
    my_label.config(text=f"Button Clicked!")


button = Button(text="Calculate", width=10, command=get_user_input)
button.grid(column=1, row=1)
window.mainloop()
