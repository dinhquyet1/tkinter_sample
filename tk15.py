import tkinter as tk
rooot=tk.Tk()
root.geometry('300x200')
lb=tk.Label(text='this is a Label.This is a Label.this is a Label.')
ms=tk.Message(text='this is a Message.this is a Message.this is a Message.')
[widget.pack() for widget in (lb,ms)]
root.mainloop()