# Leetcode - Palindrome Number

## Problem

Given an integer x, return true if x is a palindrome, and false otherwise.

## Solution

I stripped the string down to just its alphanumeric characters and lowercased them, then compared that cleaned version against its reverse [::-1] which confirms if its a palindrome or not.