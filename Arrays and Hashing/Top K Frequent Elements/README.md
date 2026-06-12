# NeetCode - TOP K Frequent Elements

## Problem

Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

## MY solution

My solution uses a hashmap to count how many times each number appears in the array. After creating the frequency hashmap, I sort the unique numbers based on their frequency in descending order. This means the numbers that appear the most will come first. Finally, I return the first k numbers from the sorted list. This solution is simple and easy to understand, although it is not the most efficient possible approach because sorting takes O(n log n) time.