import numpy as np 

class MiniExcel:
    # ---------- Create an excel like grid ----------
    def __init__(self, rows = 5, cols = 5):
        self.grid = np.zeros((rows, cols), dtype=int)

    # ---------- Function to print the grid ----------
    def show_grid(self):
        print("\nCurrent Grid:")
        print(self.grid)
    # ---------- Function to add a cell ----------
    def add_cell(self, r, c):
        row = np.zeros((r, self.grid.shape[1]), dtype=int)
        self.grid = np.vstack([row, self.grid])
        col = np.zeros((self.grid.shape[0], c), dtype=int)
        self.grid = np.hstack([self.grid, col])
    # -----------Updating a cell value -----------
    def change_val(self, r, c, value):
        if r < self.grid.shape[0] and c < self.grid.shape[1]:
            self.grid[r, c] = value
            print(f"Updated cell ({r}, {c}) to {value}")
        else:
            print("Invalid cell position!")
    # ---------- Function to show a cell value ----------
    def show_cell(self, r, c):
        if r < self.grid.shape[0] and c < self.grid.shape[1]:
            print(f"value at {r} and {c} is {self.grid[r, c]}")
        else:
            print("Invalid cell position!")
    #---------- Deleting a row ----------
    def delete_row(self, r):
        if r < self.grid.shape[0]:
            self.grid = np.delete(self.grid, r, axis=0)
            print(f"Deleted row {r}")
        else:
            print("Invalid row index!")

    #---------- Deleting a column ----------
    def delete_column(self, c):
        if c < self.grid.shape[1]:
            self.grid = np.delete(self.grid, c, axis=1)
            print(f"Deleted column {c}")
        else:
            print("Invalid column index!")

def start_excel():
    excel = MiniExcel()

    while True:
        print("\n--- Excel Clone ---")
        print("view grid = 1")
        print("To add a cell = 2")
        print("To show a cell value = 3")
        print("To change a cell value = 4")
        print("To delete a row = 5")
        print("To delete a column = 6")
        print("To exit = 7")

        option = input("Enter your choice (1-7): ")

        if option == '1':
            excel.show_grid()
        elif option == '2':
            r = int(input("Row index: "))
            c = int(input("Column index: "))
            excel.add_cell(r, c)
            excel.show_grid()
        elif option == '3':
            r = int(input("Row index: "))
            c = int(input("Column index: "))
            excel.show_cell(r, c)
        elif option == '4':
            r, c, val = map(int, input("Row index and Column index and value: ").split())
            print(f"Changing value at ({r}, {c}) to {val}")
            excel.change_val(r, c, val)
        elif option == '5':
            r = int(input("Row index to delete: "))
            excel.delete_row(r)
        elif option == '6':
            c = int(input("Column index to delete: "))
            excel.delete_column(c)
        elif option == '7':
            print("Exiting...")
            break
        else:
            print("Invalid option! Please try again.")


if __name__ == "__main__":
    start_excel()