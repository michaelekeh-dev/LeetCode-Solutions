## Leetcode - Valid Sudoku

## Problem

You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.

## Solution

I used a set for each row, column and box to track digits which i had seen. I looped through every cell then skipped the empty ones and worked out its box with (r // 3) * 3 + (c // 3). If the digit was already in its row/column/box set, I returned false. Otherwise I added it to all three. If nothing clashed, I returned True. Runs in O(1) since the board is a fixed 9 x 9. (Quite a difficult problem)