# This is a sample Python script.
import tkinter as tk
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# tkinter exercise
# init tk function
parent = tk.Tk()
# name a title for your window
parent.title("Hello Window")
# add label
my_label = tk.Label(parent, text="My_Label", font=("Arial", 30))
# position of label
my_label.grid(column=0,row=0)
# add label
my_label = tk.Label(parent, text="Your_Label", font=("Arial", 25))
# position of label
my_label.grid(column=0,row=1)
# add label
my_label = tk.Label(parent, text="bottom_Label", font=("Arial", 15))
# position of label
my_label.grid(column=1,row=1)
# add label
my_label = tk.Label(parent, text="Up_Label", font=("Arial", 35))
# position of label
my_label.grid(column=1,row=0)

parent.resizable(0,0)
# call it in loop
parent.mainloop()