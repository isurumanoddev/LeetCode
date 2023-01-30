class Solution(object):

    def twoSum(self, nums, target):

        for i in range(len(nums)):
            for j in range(i):
                if target ==  nums[i]+nums[j]:
                    return i,j
            print()





nums = [2, 7, 11, 15,20,25,30,0]
target = 9

sol = Solution()
two_sum = sol.twoSum(nums, target)
print(two_sum)
