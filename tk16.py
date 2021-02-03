# tk16.pyw

import tkinter as tk
def btn_press():
     print('buttton was pressed')

root=tk.Tk()
root.geometry('150x80')
bt=tk.Button(text='button',command=btn_press)
bt.pack()
root.mainloop()

