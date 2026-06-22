## Leetcode - Roman To Integer

## Problem

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

## My Solution

I created a dictonary to first store the values and attribute them to each roman numeral. Then I created a running total and looped until the 2nd last value of the string with the condition that if the next number is larger then the current number, I make the current number negative and add it to the total. Then I had an else statement simply adding the next number to the total calling the dictonary to attribute it to the correct value and finally I added the last number to the total as the loop only loops to the 2nd last value of the string, afterwards returning the total.