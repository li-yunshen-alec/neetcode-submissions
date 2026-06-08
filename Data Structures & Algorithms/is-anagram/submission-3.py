class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occurrences = {}
        for letter in s:
            if letter not in occurrences:
                occurrences[letter] = 0
            else:
                occurrences[letter] += 1
        
        occurrences2 = {}
        for letter in t:
            if letter not in occurrences2:
                occurrences2[letter] = 0
            else:
                occurrences2[letter] += 1

        print(occurrences, occurrences2)

        return occurrences == occurrences2