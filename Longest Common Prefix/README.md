## Leetcode - Longest Common Prefix

## Problem

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

## Solution

I started by creating the return string prefix and looped through every index of the first string and grabbed the character at that index. Then I created another loop and that checked the same index across the other strings with a condition to make sure that the word was not too short that has a index to match. Then i returned the prefix I had so far and then outside of the loop i appended the character to the prefix and at the end of the both loops i returned prefix.