import tkinter as tk
from tkinter import messagebox
import time

class SudokuSolver:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sudoku Solver")
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.speed = 1
        self.solutions = []
        self.create_grid()
        self.create_buttons()
        self.root.mainloop()

    def create_grid(self):
        for i in range(9):
            for j in range(9):
                entry = tk.Entry(self.root, width=2, font=('Arial', 18), justify='center', fg='red')
                entry.grid(row=i, column=j, padx=5, pady=5)
                self.entries[i][j] = entry

    def create_buttons(self):
        start_button = tk.Button(self.root, text="Start", command=self.start)
        start_button.grid(row=10, column=0, columnspan=3, pady=10)
        speed_frame = tk.Frame(self.root)
        speed_frame.grid(row=10, column=3, columnspan=6, pady=10)
        for i, speed in enumerate(["1x", "2x", "4x", "8x", "Skip"]):
            btn = tk.Button(speed_frame, text=speed, command=lambda s=speed: self.set_speed(s))
            btn.grid(row=0, column=i, padx=5)

    def set_speed(self, speed):
        if speed == "Skip":
            self.speed = 0
        else:
            self.speed = int(speed[:-1])

    def start(self):
        self.grid = self.get_grid()
        if not self.validate_grid():
            return
        self.solutions = []
        self.solve(0,0)
        if not self.solutions:
            messagebox.showwarning("No Solution", "No solutions found for the given Sudoku.")
        else:
            self.show_solutions()

    def get_grid(self):
        grid = []
        for i in range(9):
            row = []
            for j in range(9):
                value = self.entries[i][j].get()
                row.append(int(value) if value.isdigit() else 0)
            grid.append(row)
        return grid

    def validate_grid(self):
        for i in range(9):
            if not self.is_valid_row(i):
                messagebox.showwarning("Error", f"Duplicate number in row {i + 1}.")
                return False
            if not self.is_valid_col(i):
                messagebox.showwarning("Error", f"Duplicate number in column {i + 1}.")
                return False
        for i in range(9):
            for j in range(9):
                if not self.is_valid_num(i,j):
                    messagebox.showwarning("Error", f"Invalid number at row {i + 1} column {j + 1}.")
                    return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not self.is_valid_box(i, j):
                    messagebox.showwarning("Error", f"Duplicate number in box from row {i + 1} column {j + 1} to row {i + 3} column {j + 3}.")
                    return False
        return True
    
    def is_valid_num(self, row, col):
        if self.grid[row][col] > 9 or self.grid[row][col] < 0: return False
        else: return True

    def is_valid_row(self, row):
        nums = [num for num in self.grid[row] if num != 0]
        return len(nums) == len(set(nums))

    def is_valid_col(self, col):
        nums = [self.grid[row][col] for row in range(9) if self.grid[row][col] != 0]
        return len(nums) == len(set(nums))

    def is_valid_box(self, start_row, start_col):
        nums = []
        for i in range(3):
            for j in range(3):
                num = self.grid[start_row + i][start_col + j]
                if num != 0:
                    nums.append(num)
        return len(nums) == len(set(nums))

    def solve(self, row, col):
        if row == 9:
            self.solutions.append([row[:] for row in self.grid])
            return True

        if col == 9:
            return self.solve(row + 1, 0)

        if self.grid[row][col] != 0:
            return self.solve(row, col + 1)

        for num in range(1, 10):
            if self.is_safe(row, col, num):
                self.grid[row][col] = num
                self.update_ui(row, col, num, "blue")
                if self.speed > 0:
                    time.sleep(0.1 / self.speed)
                if self.solve(row, col + 1):
                    if self.speed == 0:
                        break
                self.grid[row][col] = 0
                self.update_ui(row, col, "", "blue")
        return False

    def is_safe(self, row, col, num):
        for x in range(9):
            if self.grid[row][x] == num or self.grid[x][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.grid[start_row + i][start_col + j] == num:
                    return False
        return True

    def update_ui(self, row, col, value, color):
        self.entries[row][col].delete(0, tk.END)
        self.entries[row][col].insert(0, value)
        self.entries[row][col].config(fg=color)
        self.root.update()

    def show_solutions(self):
        a=1
        for solution in self.solutions:
            for i in range(9):
                for j in range(9):
                    self.entries[i][j].delete(0, tk.END)
                    self.entries[i][j].insert(0, solution[i][j])
            if a%10==1:
                messagebox.showinfo("Solution",f"This is the {1+10*(a//10)}st solution among {len(self.solutions)} solutions found.")
            elif a%10==2:
                messagebox.showinfo("Solution",f"This is the {2+10*(a//10)}nd solution among {len(self.solutions)} solutions found.")
            elif a%10==3:
                messagebox.showinfo("Solution",f"This is the {3+10*(a//10)}rd solution among {len(self.solutions)} solutions found.")
            else:
                messagebox.showinfo("Solution",f"This is the {a+10*(a//10)}th solution among {len(self.solutions)} solutions found.")
            a+=1

if __name__ == "__main__":
    SudokuSolver()
