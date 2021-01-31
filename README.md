# simple_sudoku

Finds a possible solution for a sudoku problem, using native python libraries exclusively.

### files
- `sudoku.py`: the proper code.
- `board`: text file containing the initial configuration of the board.

### usage
Setup `board` according to the example and run `python sudoku.py`.

### example
```bash
$ cat board
board=[
    [9,0,0,7,0,0,0,0,0],
    [0,0,0,5,1,0,3,0,0],
    [0,5,4,0,0,0,0,9,0],
    [0,7,0,0,3,1,0,8,5],
    [1,0,0,0,9,0,0,0,0],
    [0,0,0,0,6,0,0,0,0],
    [0,0,0,0,0,8,9,0,6],
    [7,2,0,0,0,0,0,0,0],
    [0,0,0,0,0,2,0,0,3],
]
```

```bash
$ python sudoku.py
Puzzle
- - - - - - - - - - - - -
| 9     | 7     |       |
|       | 5 1   | 3     |
|   5 4 |       |   9   |
- - - - - - - - - - - - -
|   7   |   3 1 |   8 5 |
| 1     |   9   |       |
|       |   6   |       |
- - - - - - - - - - - - -
|       |     8 | 9   6 |
| 7 2   |       |       |
|       |     2 |     3 |
- - - - - - - - - - - - -


Solution
- - - - - - - - - - - - -
| 9 1 3 | 7 2 4 | 5 6 8 |
| 6 8 7 | 5 1 9 | 3 4 2 |
| 2 5 4 | 3 8 6 | 1 9 7 |
- - - - - - - - - - - - -
| 4 7 9 | 2 3 1 | 6 8 5 |
| 1 6 2 | 8 9 5 | 7 3 4 |
| 5 3 8 | 4 6 7 | 2 1 9 |
- - - - - - - - - - - - -
| 3 4 5 | 1 7 8 | 9 2 6 |
| 7 2 6 | 9 4 3 | 8 5 1 |
| 8 9 1 | 6 5 2 | 4 7 3 |
- - - - - - - - - - - - -


Execution time: 1.19 seconds.
```