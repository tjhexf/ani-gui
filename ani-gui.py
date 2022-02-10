import tkinter as tk
master = tk.Tk()


def searchbar():
    frametop = tk.Frame(master)
    frametop.pack(side='top', anchor='ne')
    Root = tk.Button(text='Search', master=frametop)

    entry = tk.Entry(frametop)
    entry.grid(column=1, row=0)
    Root.grid(column=0, row=0, sticky='w')
searchbar()



#Finalize loop
master.mainloop()