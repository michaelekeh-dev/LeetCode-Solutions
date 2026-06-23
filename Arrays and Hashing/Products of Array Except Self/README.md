# NeetCode - Products of Array Except Self

## Problem

Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

## Solution

This solution gets the prefix and suffix of all the values around the value your on and multiplies them together returning the output. It does this in two passes, one for all the values before the other one for all the values after likewise. This solution has a time complexitiy of O(n)