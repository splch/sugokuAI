# sugokuAI
 CS 171 Sudoku AI Project

# Installation

Run:

```shell
make # to build
make submission # to build the zip
```

# Coding

Edit the `src/BTSolver.py` file. Find the methods that correspond with the assigned `Part`.

# Running

To run the AI, use python3.

```shell
python3 src/Main.py
```

A random sudoku board will be generated and the AI will attempt to solve it. The output should look like this:

```shell
p:3     q:3
0 0 0 | 9 0 0 | 0 1 0 
0 0 0 | 0 0 0 | 0 0 0 
0 0 0 | 0 0 0 | 0 0 0 
- - - - - - - - - - - 
0 0 0 | 5 0 0 | 0 0 0 
0 0 2 | 0 0 0 | 0 0 0 
0 0 0 | 0 0 0 | 0 0 0 
- - - - - - - - - - - 
0 0 0 | 0 0 0 | 0 0 0 
6 0 0 | 0 0 0 | 0 7 0 
0 0 0 | 0 0 0 | 5 0 0 

p:3     q:3
2 3 4 | 9 5 6 | 7 1 8 
1 5 6 | 2 7 8 | 3 4 9 
7 8 9 | 1 3 4 | 2 5 6 
- - - - - - - - - - - 
3 1 7 | 5 2 9 | 6 8 4 
4 6 2 | 7 8 1 | 9 3 5 
5 9 8 | 4 6 3 | 1 2 7 
- - - - - - - - - - - 
8 2 5 | 6 1 7 | 4 9 3 
6 4 1 | 3 9 5 | 8 7 2 
9 7 3 | 8 4 2 | 5 6 1 

Trail Pushes: 1639
Backtracks: 1565
```

