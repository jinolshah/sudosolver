# SudoSolver
SudoSolver is a minimalist sudoku solver made with purely Python. All you have to do is input an unsolved sudoku and the program solves it for you.
### Dependencies
One can use the program through the executable file (.exe, only for windows) and won't need to install anything else.
To run it through the source script, you'll need Python (script written in Python v3.9.1) installed on your computer. 
The GUI is made using Tkinter which is the standard Python interface to the Tk GUI toolkit and is installed by default with your python installation.
### GUI
The input boxes for the numbers are the Tkinter Entry widget. A 9x9 grid of the widget is generated using a for loop. The loop assigns the grid color to make them distinguishablea and adds the Entry widget object to a dictonary along with the color data.
There are just 3 buttons - Clear, Solve, Exit. These buttons are made using the Tkinter Button widget.
The Clear button is to clear the all the entry boxes. Clicking the Solve button returns the solution to the sudoku you enter. The returned solution is green while the entered numbers are black. The Exit box closes the program.
The sudoku grid and the buttons are arranged using the grid method in Tkinter.
### Logic
Upon pressing the Solve button, the program checks whether the input values are valid according to the sudoku rules. If not, the program changes the color of the invalid number entries to red. If yes, the program goes ahead with solving the problem.
For the solution, the program uses a brute force method wherein it performs the following steps. 
  1. Find the first empty block.
  2. Fill in with a valid number.
  3. Move on to the next empty block and fill in with a valid number.
  4. If no number is valid for the block, the program returns to the previously edited block and changes the value to the next valid number.
  5. This loop continues till the last empty block is filled.

Recursion is used to carry out this logic.
Once done, it displays the solution on the screen in green while the entered numbers from the user are still black.
To enter another sudoku problem, the user must clear out the previous solution using the Clear button.
