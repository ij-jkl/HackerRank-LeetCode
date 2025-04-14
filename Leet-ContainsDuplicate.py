""" https://leetcode.com/problems/contains-duplicate/ """

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False

"""Run Time 51ms Beats 5.02%, Memory beats 97.40% """

"""
Input : nums = [1,2,3,1] - Output : True
Input : nums = [1,2,3,4] = Output : False
"""