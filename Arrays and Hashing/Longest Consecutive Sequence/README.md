## Leetcode - Longest Consecutive Sequence

## Problem

Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

## Solution

I placed all the numbers into a set and I loop through and only start counting from a number thats the beginning of a sequence, meaning (n - 1) isn't in the set. From there I keep checking (n + length) upward, growing the length until the next number isnt there and track the longest run as I go. This solution has a time complexity of O(n)