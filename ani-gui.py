import tkinter as tk
master = tk.Tk()


def searchbar():
    frametop = tk.Frame(master)
    frametop.pack(side='top', anchor='ne')
    Root = tk.Button(text='Search', master=frametop)

    entry = tk.Entry(frametop)
    entry.grid(column=1, row=0)
    Root.grid(column=0, row=0, sticky='w')

notfoundtext = tk.Label(master, text='Begin searching')




#start stuff
searchbar()
notfoundtext.pack(anchor='n', side='top')
#finalize loop
master.mainloop()