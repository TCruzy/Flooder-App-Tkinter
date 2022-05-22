from tkinter import *
import pyautogui
from time import sleep

app = Tk()


class Flooder:
    def __init__(self, master):
        self.master = master
        self.master.title("Flooder")
        self.master.geometry("800x200")
        self.master.iconbitmap("flood.ico")
        self.master.resizable(False, False)

        self.label_1 = Label(self.master, text="Enter Text To Flood:", font=("BPG Nino Mtavruli", 12))
        self.label_1.grid(row=0, column=0)

        self.label_2 = Label(self.master, text="How Many Times U Want To Flood This Text?:", font=("BPG Nino Mtavruli", 12))
        self.label_2.grid(row=1, column=0)

        self.entry_1 = Entry(self.master, width=30)
        self.entry_1.grid(row=0, column=1)

        self.entry_2 = Entry(self.master, width=30)
        self.entry_2.grid(row=1, column=1)

        self.button = Button(self.master, text="Submit", command=self.submit, font=("BPG Nino Mtavruli", 12))
        self.button.grid(row=2, column=1)
        
        self.warning = Label(self.master, text="Warning!!!", fg="red" , font=("BPG Nino Mtavruli", 12))
        self.warning.grid(row=3, column=1)
        
        self.ready = Label(self.master, text="Go To Input Field, Flooder activates In 2 Seconds when you click Submit button", fg="green",font=("BPG Nino Mtavruli", 12))
        self.ready.grid(row=4, column=1)

    def submit(self):
        text = self.entry_1.get()
        times = self.entry_2.get()
        sleep(2)
        for i in range(int(times)):
            pyautogui.typewrite(text)
            pyautogui.press("enter")
        
        



flooder = Flooder(app)

app.mainloop()









