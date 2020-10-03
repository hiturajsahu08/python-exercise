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
p_value=8
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
my_label.grid(column=0,row=2)
# add label
my_label = tk.Label(parent, text="Up_Label", font=("Arial", 35))
# position of label
my_label.grid(column=0,row=3)



p = tk.Entry()
p.grid(column=1,row=0)

def save():
    p_value=p.get()
    print(p_value)
#q=tk.messagebox.showinfo(title=None, message="Hello bro")

# Open window having dimension 100x100
# parent.geometry('100x100')
# Create a Button
#btn = tk.Button(parent, text='Click me !', bd='5',command=parent.destroy)
btn = tk.Button(parent, text='Click me !', bd='5', command=save)

# Set the position of button on the top of window.
# btn.pack(side='bottom')
# parent.resizable(0,0)
# position of button
btn.grid(column=2,row=0)
# test check in without username and password
# nnow lets check if username and pass is stored

# call it in loop
parent.mainloop()