from tkinter import *
window = Tk()
window.mainloop()

# Tkinter also offers access to the geometric configuration of the widgets which can organize the widgets in the parent windows.
# There are mainly three geometry manager classes class.
# pack() method:It organizes the widgets in blocks(in rowswise or columnwise) before placing in the parent widget.
# grid() method:It organizes the widgets in table-like structure before placing in the parent widget (puts in 2 dimensional table).
# place() method:It organizes the widgets by placing them on specific positions directed by the programmer.
from tkinter import *
window = Tk()
label1 = Label(window, text = 'welcome to PYTHON',bg = 'green') # used to display text
label2 = Label(window, text = 'welcome to GUI',bg = '#00FF00')
label1.pack()
label2.pack()
window.mainloop()

# organization ,button and formatting
from tkinter import *
window = Tk()
window.title('button_window')   # to change the name of the window#
topFrame = Frame(window)
topFrame.pack()
bottomFrame = Frame(window)
bottomFrame.pack(side=BOTTOM)
button1 = Button(topFrame, text='Button_1', fg='red')
button2 = Button(topFrame, text='Button_2', fg='magenta')
button3 = Button(topFrame, text='Button_3', fg='blue')
button4 = Button(bottomFrame, text='Button_4', fg='black')
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=RIGHT)
button4.pack(side=BOTTOM)
first = Label(window, text='FIRST', bg='blue', fg='red')
first.pack()
second = Label(window, text='SECOND', bg='crimson', fg='blue')
second.pack(fill=X)
window.mainloop()

# grid layout
root = Tk()
label_1 = Label(root, text='Username', fg='red', bg='beige')
label_2 = Label(root, text='Password', fg='black', bg='white')
entry_1 = Entry(root)
entry_2 = Entry(root)
label_1.grid(row=0)      # widgets are centered in their cell by default
label_2.grid(row=1)
entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)
root.mainloop()

# change in layout
root = Tk()
label_1 = Label(root, text='Username', fg='red', bg='beige')
label_2 = Label(root, text='Password', fg='black', bg='beige')
entry_1 = Entry(root)
entry_2 = Entry(root)
label_1.grid(row=0, sticky=E)   # u can change the position of the widget in their cell using sticky option
label_2.grid(row=1, sticky=E)
entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)
a = Checkbutton(root, text='Keep me logged in')  # elect any number of options by displaying a number of options to a user
a.grid(columnspan=2)
root.mainloop()


# FUNCTION BIND TO LAYOUTS
def print_name():
    print("Hey, my name is Aishwarya G. Shet")


root = Tk()
button_1 = Button(root, text='Click me', command=print_name)
button_1.pack()
root.mainloop()
