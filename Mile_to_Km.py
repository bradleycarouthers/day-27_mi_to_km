#   Mile_to_Km.py
# Program that converts miles to km

from tkinter import *


# Takes the entry, converts to int, calculates Km, then converts to str
def calculate():
    output = input_box.get()
    miles = int(output)
    km = round(miles * 1.60934, 2)
    new_output = str(km)
    output_label.config(text=new_output)


# Create Window
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=25, pady=25)

# Create 'is equal to' label
result_label = Label(text="is equal to", font=("Arial", 15, "normal"))
result_label.grid(column=0, row=1)

# Entry box (user input)
input_box = Entry(width=13)
input_box.grid(column=1, row=0)

# Output Label (needs to be defined as a func)
output_label = Label(font="Arial")
output_label.grid(column=1, row=1)

# Miles Label
miles_label = Label(text="Miles", font=("Arial", 15, "normal"))
miles_label.grid(column=2, row=0)

# Km label
km_label = Label(text="Km", font=("Arial", 15, "normal"))
km_label.grid(column=2, row=1)

# Convert Button
convert = Button(text="Convert", command=calculate)
convert.grid(column=1, row=2)

window.mainloop()
