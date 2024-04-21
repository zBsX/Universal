from tkinter import *
from tkinter import ttk
from Script import *


class UI:
    ## Main UI
    def __init__(self):
        # Main Root
        self.root = Tk()
        self.mainframe = Frame(self.root)
        self.root.title("ToDoList")
        self.root.geometry("400x500")
        self.mainframe.pack(fill="both", expand=True)
        self.root.iconbitmap("aw.ico")

        # Fields
        self.field1 = ttk.Entry(self.mainframe, width=40)
        self.field1.pack(anchor="center")

        # Buttons
        self.button1 = ttk.Button(self.mainframe, text="Done", command=lambda: Scripts(self.field1, self.new_frame, self.canvas1, self.mainframe, self.slider1))
        self.button1.pack(anchor="center")

        # Canvas
        self.canvas1 = Canvas(self.mainframe, width=self.mainframe.winfo_width(), height=self.mainframe.winfo_height(), scrollregion=(0,0,self.mainframe.winfo_width(),Global_height))
        
        self.canvas1.pack(side="left", fill="both", expand=True)

        # NewFrame
        self.new_frame = Frame(self.canvas1)

        # Slider !!!!!!!!
        self.slider1 = ttk.Scrollbar(self.mainframe, orient="vertical", command=self.canvas1.yview)
        self.slider1.pack(side="right", fill="y")


        # Configs !!!!!!!!
        self.canvas1.configure(yscrollcommand=self.slider1.set)

        ## bar !!!!!!!! 
        self.canvas1.bind_all("<MouseWheel>", lambda event: self.canvas1.yview_scroll(-int(event.delta / 60), "units"))

        # resize the frame !!!!!!!!
        self.mainframe.bind("<Configure>", lambda event: Resize(self.canvas1, self.new_frame, self.mainframe, event, self.slider1))

        # Main Loop
        self.mainloop = mainloop()


    ## Customs

UI()