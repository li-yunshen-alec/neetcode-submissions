class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ALPHA = "abcdefghijklmnopqrstuvwxyz"
        anagrams = defaultdict(list)
        for s in strs:
            letters = [0 for _ in range(27)]
            for l in s:
                letters[ALPHA.index(l)] += 1
            
            anagrams[tuple(letters)].append(s)
    
        return list(anagrams.values())