from tkinter import *
from solver import *

root = Tk()
root.title("SudoSolver")

def clearer(entry):
    for i in entry:
        for j in i:
            j['obj'].delete(0, END)

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
        subentry.append({'obj': Entry(root, name=str(i)+str(j), justify='center', bg=color(i,j), width=3, font = "Helvetica 16",
                            validate='all', validatecommand=validator), 
                        'bg': color(i,j), 
                        'fg': 'black'})
        subentry[j]['obj'].grid(row=i, column=j, ipady=6, padx=1, pady=1)
    entry.append(subentry)

clear = Button(text='Clear', width=14, command=lambda:clearer(entry))
clear.grid(column=0, row = 10, columnspan=3, pady=6)

solve = Button(text='Solve', width=14, command=lambda:solver(entry))
solve.grid(column=3, row=10, columnspan=3, pady=6)

exitter = Button(text='Exit', width=14, command=root.quit)
exitter.grid(column=6, row=10, columnspan=3, pady=6)



root.mainloop()