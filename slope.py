from tkinter import *                                                                   #importing tkinter package
main_window = Tk()                                                                      #creating intance of tk() constructor 
main_window.title("Slope calculator")           
sol = StringVar()                                                                       #StringVar() holds a string

def on_click():                                                                         #callback function definition
    slope = 0
    x1 = float(E1.get())                                                                #get() is used to get values from entry widget
    y1 = float(E2.get())
    x2 = float(E3.get())
    y2 = float(E4.get())
    slope = y2-y1/x2-x1
    sol.set(slope)                                                                      #sets the value stored in tkinter var     
                                                                              
L = Label(main_window, text="Enter the values")                                         #label class is used to display some texts     
L.grid(row=0, column=0, columnspan=2)                                                   #passing instance of tk class(root)
L1 = Label(main_window, text="x1 = ") 
L1.grid(row=1, column=0)                                                                #grid() arrange widgets in row and col 
L2 = Label(main_window, text="y1 = ")
L2.grid(row=2, column=0)
L3 = Label(main_window, text="x2 = ")
L3.grid(row=3, column=0)
L4 = Label(main_window, text="y2 = ")
L4.grid(row=4, column=0)

E1 = Entry(main_window, borderwidth=5)                                                  #entry class is used to take user input
E1.grid(row=1, column=1)
E2 = Entry(main_window, borderwidth=5)
E2.grid(row=2, column=1)
E3 = Entry(main_window, borderwidth=5)
E3.grid(row=3, column=1)               
E4 = Entry(main_window, borderwidth=5) 
E4.grid(row=4, column=1)                

L5 = Label(main_window, text="slope = ")
L5.grid(row=6, column=0)
E5 = Entry(main_window, textvariable=sol, borderwidth=5)               
E5.grid(row=6, column=1)

B = Button(main_window, text="Solve", command=lambda: on_click())                       #calling function using command attribute
B.grid(row=5, column=1)                                                                 #lambda function is used to pass data to callback function
mainloop()                                                                              #an infinite loop used to run the application