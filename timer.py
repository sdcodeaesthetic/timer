from tkinter import *
from tkinter import messagebox


class Timer_Application(Frame):

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.upperframe = Frame(master)
        self.upperframe.pack()
        self.middleframe = Frame(master)
        self.middleframe.pack()
        self.bottomframe = Frame(master)
        self.bottomframe.pack()
        self.running = False
        self.hrs = 0
        self.mins = 0
        self.secs = 0
        self.app_interface()

    def app_interface(self):
        self.hours = Entry(self.upperframe, width = 5, font = "Helvetica 46 bold", justify = "center", bg = "lavender")
        self.hours.insert(END, self.hrs)
        self.hours.grid(row = 0, column = 0, ipady = 47)
        self.colon_button1 = Button(self.upperframe, text = ':', width = 1, height = 4, font = "Helvetica 24", fg = "black", bg = "LightPink1", relief = SUNKEN)
        self.colon_button1.grid(row = 0, column = 1)
        self.minutes = Entry(self.upperframe, width = 5, font = "Helvetica 46 bold", justify = "center", bg = "lavender")
        self.minutes.insert(END, self.mins)
        self.minutes.grid(row = 0, column = 2, ipady = 47)
        self.colon_button2 = Button(self.upperframe, text = ':', width = 1, height = 4, font = "Helvetica 24", fg = "black", bg = "LightPink1", relief = SUNKEN)
        self.colon_button2.grid(row = 0, column = 3)
        self.seconds = Entry(self.upperframe, width = 5, font = "Helvetica 46 bold", justify = "center", bg = "lavender")
        self.seconds.insert(END, self.secs)
        self.seconds.grid(row = 0, column = 4, ipady = 47)
        self.hrs_label = Label(self.middleframe, width = 20, font = "Calibri 11 bold",  text = 'HOURS')
        self.hrs_label.grid(row = 0, column = 0)
        self.useless_label = Label(self.middleframe, width = 4, text = ' ')
        self.useless_label.grid(row = 0, column = 1)
        self.min_label = Label(self.middleframe, width = 20, font = "Calibri 11 bold",  text = 'MINS')
        self.min_label.grid(row = 0, column = 2)
        self.useless_label = Label(self.middleframe, width = 4, text = ' ')
        self.useless_label.grid(row = 0, column = 3)
        self.secs_label = Label(self.middleframe, width = 20, font = "Calibri 11 bold",  text = 'SECS')
        self.secs_label.grid(row = 0, column = 4)
        self.button_start = Button(self.bottomframe, text = 'Start', width = 25, font = "Calibri 33 bold", fg = "black", bg = "orange", command = lambda: self.start_timer())
        self.button_start.pack(pady = 5)
        self.button_stop = Button(self.bottomframe, text = 'Stop', width = 25, font = "Calibri 33 bold", fg = "black", bg = "orange", state = 'disabled', command = lambda: self.stop_timer())
        self.button_stop.pack(pady = 5)
        self.button_reset = Button(self.bottomframe, text = 'Reset', width = 25, font = "Calibri 33 bold", fg = "black", bg = "orange", state = 'disabled', command = lambda: self.reset_timer())
        self.button_reset.pack(pady = 5)
        
    def calculate(self):
        if self.running:
            if self.hrs <= 0:
                if self.mins <= 0:
                    if self.secs <= 0:
                        self.running = False
                        messagebox.showinfo("Information", "Time's Up!")
                        self.button_start['state'] = 'normal'
                        self.button_stop['state'] = 'disabled'
                        self.button_reset['state'] = 'disabled'
                    else:
                        self.seconds.delete(0, END)
                        self.secs -= 1
                        self.seconds.insert(10, self.secs)
                        self.after(1000, self.calculate)
                elif self.mins > 0 and self.secs <= 0:
                    self.mins -= 1
                    self.secs = 59
                    self.minutes.delete(0, END)
                    self.minutes.insert(10, self.mins)
                    self.seconds.delete(0, END)
                    self.seconds.insert(10, self.secs)
                    self.after(1000, self.calculate)
                else:
                    self.seconds.delete(0, END)
                    self.secs -= 1
                    self.seconds.insert(10, self.secs)
                    self.after(1000, self.calculate)
            else:
                if self.mins <= 0:
                    if self.secs <= 0:
                        self.hrs -= 1
                        self.mins = 59
                        self.secs = 59
                        self.hours.delete(0, END)
                        self.hours.insert(10, self.hrs)
                        self.minutes.delete(0, END)
                        self.minutes.insert(10, self.mins)
                        self.seconds.delete(0, END)
                        self.seconds.insert(10, self.secs)
                        self.after(1000, self.calculate)
                    else:
                        self.seconds.delete(0, END)
                        self.secs -= 1
                        self.seconds.insert(10, self.secs)
                        self.after(1000, self.calculate)
                elif self.mins > 0 and self.secs <= 0:
                    self.mins -= 1
                    self.secs = 59
                    self.minutes.delete(0, END)
                    self.minutes.insert(10, self.mins)
                    self.seconds.delete(0, END)
                    self.seconds.insert(10, self.secs)
                    self.after(1000, self.calculate)
                else:
                    self.seconds.delete(0, END)
                    self.secs -= 1
                    self.seconds.insert(10, self.secs)
                    self.after(1000, self.calculate)

    def start_timer(self):
        try:
            self.hrs = int(self.hours.get())
            self.mins = int(self.minutes.get())
            self.secs = int(self.seconds.get())
        except ValueError:
            messagebox.showwarning("Warning", "Invalid Input")
            return
        h = self.hrs <= 23 and self.hrs >= 0
        m = self.mins <= 59 and self.mins >= 0
        s = self.secs <= 59 and self.mins >= 0
        self.running = True
        if h and m and s:
            self.button_start['state'] = 'disabled'
            self.button_stop['state'] = 'normal'
            self.button_reset['state'] = 'normal'
            self.after(990, self.calculate)
        else:
            messagebox.showwarning("Warning", "Invalid Input")  

    def stop_timer(self):
        self.button_start['state'] = 'normal'
        self.button_stop['state'] = 'disabled'
        self.button_reset['state'] = 'normal'
        self.running = False

    def reset_timer(self):
        self.button_start['state'] = 'normal'
        self.button_stop['state'] = 'disabled'
        self.button_reset['state'] = 'disabled'
        self.running = False
        self.hrs = 0
        self.mins = 0
        self.secs = 0
        self.hours.delete(0, END)
        self.hours.insert(10, self.hrs)
        self.minutes.delete(0, END)
        self.minutes.insert(10, self.mins)
        self.seconds.delete(0, END)
        self.seconds.insert(10, self.secs)


if __name__ == "__main__":
    root = Tk()
    root.title("Countdown Timer")
    my_timer = Timer_Application(root)
    root.mainloop()
