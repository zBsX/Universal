from tkinter import *
from tkinter import ttk
from Script import *


class UI:
    ## Main UI
    def __init__(self):
        self.root = Tk()
        self.mainframe = Frame(self.root)
        self.root.title("ToDoList")
        self.root.geometry("400x500")
        self.mainframe.pack(fill="both", expand=True)
        self.root.iconbitmap("aw.ico")


        # Fields
        self.field1 = ttk.Entry(self.mainframe, width=40)
        self.field1.pack()

        # Buttons
        self.button1 = ttk.Button(self.mainframe, text="Done", command=lambda: Scripts(self.field1, self.mainframe))
        self.button1.pack()
        
        # self.button2 = ttk.Button(self.mainframe, text="Clear", command=lambda: Clear(self.field1))
        # self.button2.pack()

        # Main Loop
        self.mainloop = mainloop()

    ## Customs

UI()