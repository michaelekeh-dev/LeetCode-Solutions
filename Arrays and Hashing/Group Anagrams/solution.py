class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        letters = {}
        
        for word in strs:
            key = "".join(sorted(word))   
            if key not in letters:      
                letters[key] = []         
            letters[key].append(word)  

        return list(letters.values())        