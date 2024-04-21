def printinfo_bigger(Global_height, canvas):
    print("globle height is longer:", Global_height, 
        ">",  
        "canvas height:", canvas.winfo_height())
    return

def printinfo_lesser(Global_height, canvas, new_frame):
    print("globle height is lesser:", Global_height, 
    "<=",
    "canvas height:", canvas.winfo_height(), 
    "canvas width:", canvas.winfo_width(), 
    "new_frame width:", new_frame.winfo_width())
    return