# Neetcode - Two Integer Sum II

## Problem

Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

## Solution

Since the array is sorted, the sum of the two numbers tells me which way to move. If the sum is too small I move the left pointer up for a bigger number, and if it's too big I move the right pointer down for a smaller number. When the sum matches the target I return the two positions, adding one to each for the 1-indexing.