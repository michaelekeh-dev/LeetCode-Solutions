## Neetcode - Best Time to Buy and Sell Stock

## Problem 

You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

## Solution

My solution was to loop through prices and check for the CURRENT cheapest price to be used to calculate the current profit so far until the end of the loop and return that profit.
