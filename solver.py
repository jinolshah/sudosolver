def blacker(entry):
    for i in range(9):
        for j in range(9):
            entry[i][j]['fg'] = 'black'
            entry[i][j]['obj'].config(fg='black')


def rowChecker(entry, i):
    inval = False
    for j in range(8):
        if entry[i][j]['obj'].get():
            for y in range(j+1, 9):
                if (entry[i][j]['obj'].get() == entry[i][y]['obj'].get()):
                    entry[i][j]['fg'] = '#B00020'
                    entry[i][j]['obj'].config(fg='#B00020')
                    entry[i][y]['fg'] = '#B00020'
                    entry[i][y]['obj'].config(fg='#B00020')
                    inval = True
    if inval:
        return False
    else:
        return True

                
def columnChecker(entry, j):
    inval = False
    for i in range(8):
        if entry[i][j]['obj'].get(): 
            for y in range(i+1, 9):
                if (entry[i][j]['obj'].get() == entry[y][j]['obj'].get()):
                    entry[i][j]['fg'] = '#B00020'
                    entry[i][j]['obj'].config(fg='#B00020')
                    entry[y][j]['fg'] = '#B00020'
                    entry[y][j]['obj'].config(fg='#B00020')
                    inval = True
    if inval:
        return False
    else:
        return True

def boxChecker(entry, x):
    inval = False
    a = ((x//3)*3)
    b = ((x%3)*3)
    for i in range(a,a+3):
        for j in range(b,b+3):
            if i==a+2 and j==b+2:
                continue
            if entry[i][j]['obj'].get(): 
                for y in range(i, a+3):
                    for z in range(b, b+3):
                        if y==i and z==j:
                            continue
                        if (entry[i][j]['obj'].get() == entry[y][z]['obj'].get()):
                            entry[i][j]['fg'] = '#B00020'
                            entry[i][j]['obj'].config(fg='#B00020')
                            entry[y][z]['fg'] = '#B00020'
                            entry[y][z]['obj'].config(fg='#B00020')
                            inval = True
    if inval:
        return False
    else:
        return True


def checker(entry):
    blacker(entry)
    rowVal = True
    colVal = True
    boxVal = True
    for i in range(9):
        rowVal = rowVal and rowChecker(entry, i)
        colVal = colVal and columnChecker(entry, i)
        boxVal = boxVal and boxChecker(entry, i)
    if rowVal and colVal and boxVal:
        return True
    else:
        return False

def solver(entry):
    entValid = checker(entry)
    print(entValid)