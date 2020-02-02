from tkinter import *


class Timer_Application(Frame):

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.running = True
        self.hrs = 0
        self.mins = 0
        self.secs = 0
        self.app_interface()

    def app_interface(self):
        self.upperframe = Frame(root)
        self.upperframe.pack()
        self.bottomframe = Frame(root)
        self.bottomframe.pack()
        self.hours = Entry(self.upperframe, width = 5, font = "Helvetica 46 bold", justify = "center", bg = "lavender")
        self.hours.grid(row = 0, column = 0, ipady = 47)
        self.colon_button1 = Button(self.upperframe, text = ':', width = 1, height = 4, font = "Helvetica 24", fg = "black", bg = "LightPink1", relief = SUNKEN)
        self.colon_button1.grid(row = 0, column = 1)
        self.minutes = Entry(self.upperframe, width = 5, font = "Helvetica 46 bold", justify = "center", bg = "lavender")
        self.minutes.grid(row = 0, column = 2, ipady = 47)
        self.colon_button2 = Button(self.upperframe, text = ':', width = 1, height = 4, font = "Helvetica 24", fg = "black", bg = "LightPink1", relief = SUNKEN)
        self.colon_button2.grid(row = 0, column = 3)
        self.seconds = Entry(self.upperframe, width = 5, font = "Helvetica 46 bold", justify = "center", bg = "lavender")
        self.seconds.grid(row = 0, column = 4, ipady = 47)        
        self.button_start = Button(self.bottomframe, text = 'Start', width = 25, font = "Calibri 33 bold", fg = "black", bg = "orange", command = lambda: self.start_timer())
        self.button_start.pack(pady = 5)
        self.button_stop = Button(self.bottomframe, text = 'Stop', width = 25, font = "Calibri 33 bold", fg = "black", bg = "orange", state = 'disabled', command = lambda: self.stop_timer)
        self.button_stop.pack(pady = 5)
        self.button_reset = Button(self.bottomframe, text = 'Reset', width = 25, font = "Calibri 33 bold", fg = "black", bg = "orange", state = 'disabled', command = lambda: self.reset_timer)
        self.button_reset.pack(pady = 5)
        
    def calculate(self):
        if self.running:
            if self.secs <= 0:
                self.running = False
            else:
                self.seconds.delete(0, END)
                self.secs -= 1
                self.seconds.insert(10, self.secs)
                self.after(1000, self.calculate)

    def start_timer(self):
        self.hrs = int(self.hours.get())
        self.mins = int(self.minutes.get())
        self.secs = int(self.seconds.get())
        h = self.hrs <= 23 and self.hrs >= 0
        m = self.mins <= 59 and self.mins >= 0
        s = self.secs <= 59 and self.mins >= 0
        if h and m and s:
            self.calculate()

    def stop_timer(self):
        return

    def reset_timer(self):
        return

if __name__ == "__main__":
    root = Tk()
    root.title("Timer")
    Timer_Application(root)
    root.mainloop()
