from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         for i in range(len(nums)):
              for j in range(i+1,len(nums)):
                   if nums[i]==nums[j]:
                        return True
         return False          
                   


sol=Solution()
print(sol.hasDuplicate([1,2,3,3]))