from tkinter import *


if __name__ == "__main__":
    root = Tk()
    root.title("Timer")
    
    upperframe = Frame(root, bg = "azure")
    upperframe.pack()
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    hours = Entry(upperframe, textvariable = var1, width = 5, font = "Helvetica 46 bold", justify = "center", bg = "lavender")
    hours.grid(row = 0, column = 0, ipady = 47)
    colon_button1 = Button(upperframe, text = ':', width = 1, height = 4, font = "Helvetica 24", fg = "black", bg = "LightPink1", relief = SUNKEN)
    colon_button1.grid(row = 0, column = 1)
    minutes = Entry(upperframe, textvariable = var2, width = 5, font = "Helvetica 46 bold", justify = "center", bg = "lavender")
    minutes.grid(row = 0, column = 2, ipady = 47)
    colon_button2 = Button(upperframe, text = ':', width = 1, height = 4, font = "Helvetica 24", fg = "black", bg = "LightPink1", relief = SUNKEN)
    colon_button2.grid(row = 0, column = 3)
    seconds = Entry(upperframe, textvariable = var3, width = 5, font = "Helvetica 46 bold", justify = "center", bg = "lavender")
    seconds.grid(row = 0, column = 4, ipady = 47)

    bottomframe = Frame(root, bg = "azure")
    bottomframe.pack()
    button_start = Button(bottomframe, text = 'Start', width = 25, font = "Calibri 33 bold", fg = "black", bg = "orange")
    button_start.pack(pady = 5)
    button_stop = Button(bottomframe, text = 'Stop', width = 25, font = "Calibri 33 bold", fg = "black", bg = "orange", state = 'disabled')
    button_stop.pack(pady = 5)
    button_reset = Button(bottomframe, text = 'Reset', width = 25, font = "Calibri 33 bold", fg = "black", bg = "orange", state = 'disabled')
    button_reset.pack(pady = 5)

    root.mainloop()
