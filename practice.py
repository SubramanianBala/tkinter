import tkinter as tk
from tkinter import*

#button
m=tk.Tk()   # T should ne capital

button=tk.Button(m,text='stop',width=10,height=5,command=m.destroy)
button.pack()          #align the Button in windoW
m.mainloop()



#checkbutton
m=Tk()
Checkbutton(m,text='songs').grid(row=0,sticky=W)
Checkbutton(m,text='music').grid(row=1,sticky=W)
m.mainloop()



#radiobuttons
m=Tk()
selected_option = tk.IntVar()

Radiobutton(m, text='yes', value=0, variable=selected_option).grid(row=0)
Radiobutton(m, text='no', value=1, variable=selected_option).grid(row=1)

def show_selection():
    # Map the integer values to their corresponding strings
    value_map = {0: 'yes', 1: 'no'}
    selected_value = selected_option.get()
    print("Selected option:", value_map.get(selected_value, "Unknown"))


tk.Button(m, text='Show Selection', command=show_selection).grid(row=2)

m.mainloop()




#list
top=Tk()
L=Listbox(top)
L.insert(1,'python')
L.insert(2,'java')
L.insert(3,'C++')
L.pack()
mainloop()



#text
m=Tk()
text=Text(m)
text.pack()
text.insert(END,'python is a language')
mainloop()



#message
m=Tk()
msg="this is a message"
m1=Message(m,text='msg')
m1.config(bg='green')
m1.pack()
mainloop()



#frame
m=Tk()
frame=Frame(m)
frame.pack(side=LEFT)
redbutton=Button(frame,text='red',fg='red')
redbutton.pack(side=LEFT)
mainloop()



#scale
m=Tk()
W=Scale(m,from_=0,to=30,orient=HORIZONTAL) #orient=HORIZONTAL: The orientation of the slider is horizontal.
W.pack()
mainloop()



#spinbox
m=Tk()
W=Spinbox(m,from_=10,to=50)
W.pack()
mainloop()




#toplevel
m=Tk()
m.title('python')
m=Toplevel()
m.title('program')
mainloop()




#entry
root = Tk()
Label(root, text='First Name').grid(row=0, column=0)  # Place the label in row 0, column 0
Label(root, text='Last Name').grid(row=1, column=0)   # Place the label in row 1, column 0

e1 = Entry(root)
e2 = Entry(root)

e1.grid(row=0, column=1)  # Place the entry in row 0, column 1
e2.grid(row=1, column=1)  # Place the entry in row 1, column 1

root.mainloop()




#scrollbar
m = Tk()

scroll = Scrollbar(m)
scroll.pack(side=RIGHT, fill=Y)
# Create the Listbox and attach the scrollbar to it using 'yscrollcommand'
L = Listbox(m, yscrollcommand=scroll.set)
# Insert 100 items (0 to 99) into the Listbox
for i in range(100):
    L.insert(END, str(i))

L.pack()
# Configure the scrollbar to scroll the Listbox
scroll.config(command=L.yview)
mainloop()



#menubutton
m = Tk()
mb = Menubutton(m, text='File')
mb.grid(row=1, column=0)
mb.menu = Menu(mb)
mb['menu'] = mb.menu
#options to the Menubutton's menu
mb.menu.add_command(label="Open")
mb.menu.add_command(label="Save")
mb.menu.add_command(label="Exit")

mainloop()


#menu
m = tk.Tk()
menu_bar = Menu(m)
filemenu = Menu(menu_bar, tearoff=0)
filemenu.add_command(label='New')
filemenu.add_command(label='Open')
# Add the 'File' menu to the menu bar
menu_bar.add_cascade(label='File', menu=filemenu)
m.config(menu=menu_bar)
m.mainloop()


#paned window

root = tk.Tk()
# Create a horizontal PanedWindow
paned_window = PanedWindow(root, orient=tk.HORIZONTAL)
# Add the PanedWindow to the root window
paned_window.pack(fill=tk.BOTH, expand=1)
# Create two frames to be added to the paned window
left_frame = tk.Frame(paned_window, bg="lightblue", width=200, height=300)
right_frame = tk.Frame(paned_window, bg="lightgreen", width=200, height=300)
# Add the frames to the paned window
paned_window.add(left_frame)
paned_window.add(right_frame)

root.mainloop()



#message box
from tkinter import Tk, Button, messagebox

m = Tk()
m.geometry('100x100')
# Function to show a message box
def hello():
    messagebox.showinfo('Say Hello', 'Hello World')
# Create a button that triggers the hello() function
button = Button(m, text='Say Hello', command=hello)
button.place(x=35, y=0)
m.mainloop()

