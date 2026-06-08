class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ALPHA = "abcdefghijklmnopqrstuvwxyz"
        anagrams = {}
        for s in strs:
            letters = [0 for _ in range(27)]
            for l in s:
                letters[ALPHA.index(l)] += 1
            
            key = str(letters)

            if key in anagrams:
                print(s)
                anagrams[key] = anagrams[key] + [s]
            else:
                anagrams[key] = [s]
    
        output = []
        for group in anagrams:
            output += [anagrams[group]]

        print(anagrams)
        print(output)

        return output