## Neetcode -  Group Anagrams

## Problem

Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Constraints:

1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.

## Solution

The key realization in this problem is that anagrams are just the same letters in a different order for eg: 'eat', 'tea', 'ate' all become 'aet'. So I use a dictionary mapping each sorted word to the list of words that share it and make one pass dropping each word into its group then return the dictionary's values. This solution has a time complexitiy of O(n * k log k)
