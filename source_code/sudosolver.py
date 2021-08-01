from tkinter import *
from solver import *
from mover import *
from version import *
import webbrowser

root = Tk()
root.title("SudoSolver")

def linker(event):
    webbrowser.open_new_tab(repolink)

def binder(ele, entry):
    ele.bind('<Down>', lambda event, enter=entry: downer(event, enter))
    ele.bind('<Up>', lambda event, enter=entry: upper(event, enter))
    ele.bind('<Left>', lambda event, enter=entry: lefter(event, enter))
    ele.bind('<Right>', lambda event, enter=entry: righter(event, enter))

def clearer(entry, solve):
    for i in entry:
        for j in i:
            j['obj'].config(state='normal', disabledforeground='black')
            j['obj'].delete(0, END)
    blacker(entry)
    solve.config(state='normal')
    entry[0][0]['obj'].focus()

def color(i, j):
    if i in range(0,3) or i in range (6,9):
        if j in range(0,3) or j in range(6,9):
            return 'white'
        else:
            return '#e3e3e3'
    else:
        if j in range(0,3) or j in range(6,9):
            return '#e3e3e3'
        else:
            return 'white'


def callback(inpt, name):
    if (inpt.isdecimal() and 0 < int(inpt) < 10) or inpt == '':
        return True
    else:
        return False
validator = (root.register(callback), '%P', '%W')

entry = []

for i in range(9):
    subentry = []
    for j in range(9):
        colored = color(i,j)
        subentry.append({'obj': Entry(root, name=str(i)+str(j), justify='center',
                                bg=colored, disabledbackground=colored, disabledforeground='black', 
                                width=3, font = "Helvetica 16",
                                validate='all', validatecommand=validator),
                        'bg': colored,
                        'fg': 'black'})
        subentry[j]['obj'].grid(row=i, column=j, ipady=6, padx=1, pady=1)
    entry.append(subentry)

for i in entry:
    for j in i:
        binder(j['obj'], entry)

solve = Button(text='Solve', cursor="hand2", width=14, command=lambda:solver(entry, solve))
solve.grid(column=3, row=10, columnspan=3, pady=6)

clear = Button(text='Clear', cursor="hand2", width=14, command=lambda:clearer(entry, solve))
clear.grid(column=0, row = 10, columnspan=3, pady=6)

exitter = Button(text='Exit', width=14, command=root.quit, cursor="hand2")
exitter.grid(column=6, row=10, columnspan=3, pady=6)

author = Label(text='by Jinol Shah', fg='#696969', font='Helvetica 9 italic', cursor="hand2")
author.grid(row=11, column=6, columnspan=3, padx=(30,0), pady=(0,4))
author.bind("<ButtonRelease-1>", linker)

version = Label(text=version, fg='#696969', font='Helvetica 9 italic', cursor="hand2")
version.grid(row=11, column=0, columnspan=1, padx=(2,0), pady=(0,4))
version.bind("<ButtonRelease-1>", linker)

# root.update()
# print(root.winfo_height())
# print(root.winfo_width())

root.mainloop()