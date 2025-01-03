from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)
window.config(padx=20, pady=20)

userInput = Entry(width=10)
userInput.grid(column=1, row=0)
userInput.grid(padx=20, pady=20)
userInput.focus()
userInput.config(justify="center")
userInput.config(font=("Arial", 16))

miles = Label(text="Miles")
miles.grid(column=2, row=0)
miles.config(font=("Arial", 16))

equalsLabel = Label(text="is equal to")
equalsLabel.grid(column=0, row=1)
equalsLabel.config(font=("Arial", 16))

kmOutput = Label(text="0")
kmOutput.grid(column=1, row=1)
kmOutput.config(font=("Arial", 16))

kmLabel = Label(text="Km")
kmLabel.grid(column=2, row=1)
kmLabel.config(font=("Arial", 16))


def calculateButtonClicked():
    kmOutput.config(text=round(float(userInput.get()) * 1.60934, 2))


calculateButton = Button(text="Calculate",
                         command=calculateButtonClicked)
calculateButton.grid(column=1, row=2)
calculateButton.config(font=("Arial", 16, "bold"))

window.mainloop()
