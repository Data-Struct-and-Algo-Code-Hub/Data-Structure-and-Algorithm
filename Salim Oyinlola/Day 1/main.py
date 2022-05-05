
class Solution2:
    def twoSum(self, nums, target):
        empty_dict = {}
        i = 0
        for i in range(len(nums)):
            empty_dict[nums[i]] = i
        for i in range(len(nums)):
            comp = target - nums[i]

            if comp in empty_dict and empty_dict[comp] != i:
                return [i, empty_dict[comp]]

solution2 = Solution2()
answer4 = solution2.twoSum([2, 7, 11, 15], 9)
answer5 = solution2.twoSum([3, 2, 4], 6)
answer6 = solution2.twoSum([3, 2, 6], 6)
print(answer4)
print(answer5)
print(answer6)
