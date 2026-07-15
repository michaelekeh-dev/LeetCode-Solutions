# Neetcode - Container With Most Water

## Problem
You are given an integer array heights where heights[i] represents the height of the i^th bar

You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Example 1:

## Solution

I brute forced this by checking every pair of bars with two loops, working out each container's area as min(heights[i], heights[j]) * (j - i) since water is capped by the shorter wall times the distance between them. I kept a running best in res and took the max each time, which gives the largest area across all pairs. Time is O(n^2) could be better.