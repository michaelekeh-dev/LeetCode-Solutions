# NeetCode - Valid Anagram

## Problem

Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

## Solution

Firstly, I validated the length of each string to confirm if they are the same length. Then I created two hashmaps and counted each instance of a letter in string s and string t. Each hashmap stores every character as a key and its mode in the string as a value. Now I compare both hashmaps character counts and if they of the counts differ I return False otherwise I return True.

