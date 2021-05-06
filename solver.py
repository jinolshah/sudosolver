from checker import *
from pprint import pprint
import copy

def row(unsudoku, k, i, j):
    inval = False
    for x in range(9):
        if x == j:
            continue
        if k == unsudoku[i][x]:
            inval = True
    if inval:
        return False
    else:
        return True

def column(unsudoku, k, i, j):
    inval = False
    for y in range(9):
        if y == i:
            continue
        if k == unsudoku[y][j]:
            inval = True
    if inval:
        return False
    else:
        return True

def box(unsudoku, k, i, j):
    inval = False
    a = ((i//3)*3)
    b = ((j//3)*3)
    for x in range(a, a+3):
        for y in range(b, b+3):
            if x == i and y == j:
                continue
            if k == unsudoku[x][y]:
                inval = True
    if inval:
        return False
    else:
        return True

def checked(unsudoku, k, i, j):
    check1 = row(unsudoku, k, i, j)
    if check1:
        check2 = column(unsudoku, k, i, j)
        if check2:
            check3 = box(unsudoku, k, i, j)
            if check3:
                return True
            else: return False
        else: return False
    else: return False

def matrixgen(entry):
    sudoku = []
    for i in range(9):
        sublst = []
        for j in range(9):
            if entry[i][j]['obj'].get():
                sublst.append(int(entry[i][j]['obj'].get()))
            else:
                sublst.append(0)
        sudoku.append(sublst)
    return sudoku

def finder(unsudoku):
    for i in range(9):
        for j in range(9):
            if not unsudoku[i][j]:
                return i, j
    return None, None

def solution(unsudoku):
    i, j = finder(unsudoku)
    if i is None and j is None:
        return True
    for k in range(1,10):
        flag = checked(unsudoku, k, i, j)
        if flag:
            unsudoku[i][j] = k
            if solution(unsudoku):
                return True
            else:
                continue
    unsudoku[i][j] = 0
    return False

def solver(entry):
    entValid = checker(entry)
    if entValid:
        sudoku = matrixgen(entry)
        unsudoku = copy.deepcopy(sudoku)
        if solution(unsudoku):
            pprint(unsudoku)
            for i in range(9):
                for j in range(9):
                    if not sudoku[i][j]:
                        entry[i][j]['obj'].config(fg='#5E8C77')
                        entry[i][j]['obj'].insert(0, unsudoku[i][j])
