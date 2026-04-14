class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        dict = {}

        # Loop through the array and add into dictionnary unique elements
        for x in nums: 
            if x in dict:
                return True
            dict[x] = 1
        
        return False