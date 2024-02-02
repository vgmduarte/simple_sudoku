"""
Finds a possible solution (if there is one) for a sudoku problem.
"""

#!/usr/bin/env python
# coding: utf-8


import sys
from copy import copy
from time import time


class Node:
    def __init__(self, board, parent=None):
        self.board=board
        self.parent=parent
        self.children=[]
        if parent:
            parent.children.append(self)
        self.is_solution=False


def found_duplicates(row):
    occurrencies=[0]*10
    for i in range(9):
        occurrencies[row[i]]+=1
    return any([occurrency>1 for occurrency in occurrencies[1::]])


def is_valid(board):
    for row in board:
        if found_duplicates(row):
            return False
    for j in range(9):
        col=[board[i][j] for i in range(9)]
        if found_duplicates(col):
            return False
    for i in [0,3,6]:
        for j in [0,3,6]:
            square=[]
            for k in range(i,i+3):
                square+=board[k][j:j+3]
            if found_duplicates(square):
                return False
    return True


def get_next_empty_position(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return [i,j]
    return None


def bcopy(board):
    new_board=[]
    for row in board:
        new_board.append(copy(row))
    return new_board


def expand(node):
    position = get_next_empty_position(node.board)
    if position:
        [i,j] = position
        for number in range(1, 10):
            board=bcopy(node.board)
            board[i][j]=number
            if is_valid(board):
                Node(board,parent=node);
    else:
        node.is_solution=True


def search(node):
    bprint(node.board)
    expand(node)
    if node.is_solution:
        return node
    else:
        delete_output()
    for child in node.children:
        capture=search(child)
        if capture:
            return capture


def bprint(board):
    bp='- - - - - - - - - - - - -'
    for i in range(9):
        if i in [3,6]:
            bp+='\n- - - - - - - - - - - - -'
        bp+='\n|'
        for j in range(9):
            number=board[i][j]
            if number == 0:
                bp+='  '
            else:
                bp+=f' {number}'
            if j in [2,5]:
                bp+=' |'
        bp+=' |'
    bp+='\n- - - - - - - - - - - - -'
    print(bp)


def delete_output():
    for _ in range(13):
        #cursor up one line
        sys.stdout.write('\x1b[1A')
        #delete last line
        sys.stdout.write('\x1b[2K')


if __name__ == '__main__':
    start=time()

    # set the initial sudoku board here
    # empty spots should be filled with zeros
    board=[
        [9, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 1, 0, 3, 0, 0],
        [0, 5, 4, 0, 0, 0, 0, 9, 0],
        [0, 7, 0, 0, 3, 1, 0, 8, 5],
        [1, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 9, 0, 6],
        [7, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 3]
    ]

    root=Node(board)
    print('Puzzle')
    bprint(root.board)

    print('\nSolution')
    node=search(root)

    end=time()
    print(f'\nExecution time: {end-start:.2f} seconds.')
