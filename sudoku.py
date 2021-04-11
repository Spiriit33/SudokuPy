from tkinter import *

root = Tk()
root.geometry('600x600')

# Matrix where are stored numbers.
storedNumbers = []


# Set all grid to zero
def all_to_zero():
    for i in range(9):
        for j in range(9):
            if storedNumbers[i][j].get() not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                storedNumbers[i][j].set(0)


# Check the Validity of savedNumbers
def is_valid(i, j, e):
    for x in range(9):
        if storedNumbers[i][x].get() == str(e):
            return False

    for x in range(9):
        if storedNumbers[x][j].get() == str(e):
            return False

    # Finding the Top x,y Co-ordinates of the section containing the i,j cell
    secTopX, secTopY = 3 * int((i / 3)), 3 * int((j / 3))
    for x in range(secTopX, secTopX + 3):
        for y in range(secTopY, secTopY + 3):
            if storedNumbers[x][y].get() == str(e):
                return False
    return True


def find_next_cell_to_fill(i, j):
    for x in range(i, 9):
        for y in range(j, 9):
            if storedNumbers[x][y].get() == '0':
                return x, y

    for x in range(0, 9):
        for y in range(0, 9):
            if storedNumbers[x][y].get() == '0':
                return x, y

    return -1, -1


class SolveSudoku:
    def __init__(self):
        # Set the empty cells to 0
        all_to_zero()
        self.start_solution()

    # Start the Algorithm
    def start_solution(self, i=0, j=0):
        i, j = find_next_cell_to_fill(i, j)

        # If i == -1 then  the position is okay or the Sudoku is Solved
        if i == -1:
            return True
        for e in range(1, 10):
            if is_valid(i, j, e):
                storedNumbers[i][j].set(e)
                if self.start_solution(i, j):
                    return True
                # Undo the current cell
                storedNumbers[i][j].set(0)
        return False


def correct_grid(e):
    for i in range(9):
        for j in range(9):
            if storedNumbers[i][j].get() == "":
                continue
            if len(storedNumbers[i][j].get()) > 1 or storedNumbers[i][j].get() not in ['1', '2', '3', '4', '5', '6',
                                                                                     '7', '8', '9']: storedNumbers[i][j].set('')


def solve_input():
    SolveSudoku()


# Sell all to null
def clear_all():
    for i in range(9):
        for j in range(9):
            storedNumbers[i][j].set('')


class Play:
    def __init__(self, master):

        # Title and settings
        self.master = master
        master.title("Sudoku Project")
        font = ('Arial', 20)

        # Front-end Grid
        self.__table = []
        for i in range(1, 10):
            self.__table += [[0, 0, 0, 0, 0, 0, 0, 0, 0]]

        for i in range(0, 9):
            for j in range(0, 9):

                if (i < 3 or i > 5) and (j < 3 or j > 5):
                    color = 'lightgray'
                elif i in [3, 4, 5] and j in [3, 4, 5]:
                    color = 'lightgray'
                else:
                    color = 'white'

                self.__table[i][j] = Entry(master, width=4, font=font, bg=color, cursor='arrow', borderwidth=0,
                                           highlightcolor='orange', highlightthickness=1, highlightbackground='black',
                                           textvar=storedNumbers[i][j])
                self.__table[i][j].bind('<Motion>', correct_grid)
                self.__table[i][j].bind('<FocusIn>', correct_grid)
                self.__table[i][j].bind('<Button-1>', correct_grid)
                self.__table[i][j].grid(row=i, column=j)

        # Tkinter front
        menu = Menu(master)
        master.config(menu=menu)

        file = Menu(menu)
        menu.add_cascade(label='Fichier', menu=file)
        file.add_command(label='Quitter', command=master.quit)
        file.add_command(label='Resoudre', command=solve_input)
        file.add_command(label='Reset', command=clear_all)


for i in range(1, 10):
    storedNumbers += [[0, 0, 0, 0, 0, 0, 0, 0, 0]]
for i in range(0, 9):
    for j in range(0, 9):
        storedNumbers[i][j] = StringVar(root)

app = Play(root)
root.mainloop()
