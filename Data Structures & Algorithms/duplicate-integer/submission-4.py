class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasSeen = {}
        for n in nums:
            if n in hasSeen: return True
            hasSeen[n] = True
        return False