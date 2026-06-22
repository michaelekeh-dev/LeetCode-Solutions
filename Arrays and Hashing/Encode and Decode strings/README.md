## Neetcode - Encode and Decode Strings

## Problem

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains any possible characters out of 256 valid ASCII characters.

## Solution

My inital idea was to use a seperator alone (eg :) but then I read that it can include ANY of the 256 valid ASCII characters which could also by my seperator character. So what I did was i used the length of each word in the array to count up the full length of every item in the array and then simply decoded it by searching for the : and counting the length of indexes after the seperator and then continued through the rest of the array. Though I did want to have some fun and use real decoding method, this was the most efficent with a time complexity of O(N).