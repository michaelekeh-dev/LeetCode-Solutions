# Neetcode - 3Sum

## Problem

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

## Solution

I sort the array first, then fix one number as an anchor and look for the other two that sum to its negative, which is basically the same idea as Two Sum on a sorted array. Since the array is sorted the total tells me which way to move, so if the sum is too small I move the left pointer up for a bigger number, and if its too big I move the right pointer down for a smaller number, recording a triplet whenever they hit zero. 