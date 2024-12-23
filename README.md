# Sudoku Solver Using Backtracking Method

## (1) 程式的主要功能 Main Features

The sudoku solver provides the following functionalities:

- **Customized Sudoku**: By using keybroad to input numbers into the grid.
- **Backtracking Process**: Show the full process of backtracking.
- **Customized Speed**: Choose the speed of the process showing, or just skip it.(The speed of skipping depends on the settings.)
- **Show all solution**: Show all possible solution.

## (2) 使用方式 Usage

Follow these steps to use the sudoku solver:

### 1. Set Up Your Environment

Please Make sure that you have Tkinter. If not, see this:
[DelftStack](https://www.delftstack.com/howto/python-tkinter/install-tkinter/)

### 2. Customize Your Sudoku

Run the Script, and it will generate a grid.
Click on the blocks on the grid, and input numbers by your keybroad.
If you think your unsolved sudoku is done, just click the "Start" button, and the script will examine if your sudoku is solvable.
If not, show the error message.

### 3. Choose the Speed of Backtracking Method

After the sudoku passes the examination, the script will start to solve it.
There are five buttons below: “1x”, “2x”, “4x”, “8x”, “Skip”. “1x” is for original speed, “2x” is for two times of original speed, and so on.
“Skip” is for skipping the process.(The speed of skipping depends on the settings.)

### 4. Show the Result

Show the solutions found one by one. If the sudoku has no solution, show the error message.

## (3) 程式的架構 Program Architecture

The project is organized as follows:

```
SudokuSolver/
├─ SudokuSolver/    # Script  
│  └ SudokuSolver/  # Class
│    ├ __init__         ┐ 
│    ├ create_grid      │# Pre_action
│    ├ create_buttons   ┘
│    ├ set_speed        # Solving speed
│    ├ start            # About Solving
│    ├ get_grid         # About Solving
│    ├ validate_grid    ┐
│    ├ is_valid_num     │
│    ├ is_valid_row     │# Examine the sudoku
│    ├ is_valid_col     │
│    ├ is_valid_box     ┘
│    ├ solve            # About Solving
│    ├ is_safe          # About Solving
│    ├ update_ui        # Continuously display the current process
│    └ show_solutions   # Display the solutions
└─ README.md        # Documentation
```

## (4) 開發過程 Development Process

The development of the sudoku solver followed these steps:

1. **Ideation and Planning**: Just think this topic is fun.
2. **Implementation**: Write a prompt for ChatGPT, and get a fundamental structure of the script.
3. **Enhancements**: Added some enhancements.(See "(6) 程式修改或增強的內容 Enhancements and Contributions" for more)
4. **Testing and Debugging**: Test the script and make sure that it can run correctly.

## (5) 參考資料來源 References

1. [Wikipedia](https://en.wikipedia.org/wiki/Sudoku_solving_algorithms) - For inspiration and concept understanding.
2. ChatGPT - Assisted with fundamental structuring of the project.

## (6) 程式修改或增強的內容 Enhancements and Contributions

The following modifications and enhancements were added to the project:

1. **Adjust the Speed of the Process**: Adjust the original speed of the process, making it not too fast or too slow.
2. **New features**: Examine that if the inputted numbers is within 1 and 9. If not, show the error message.
3. **Optimize Error Message Texts**: Clearly indicate which column or row the error is in, making it easier to understand.
4. **Optimize Solution Showing Message Texts**: Clearly indicate which solution is currently displayed and how many solutions there are in total, making it easier to understand.
