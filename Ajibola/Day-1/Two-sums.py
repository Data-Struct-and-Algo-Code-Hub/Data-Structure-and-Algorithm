# The solution below isn't optimal because it has a time complexity of O(n^2) and a space complexity of O(n)
# Space Complexity -> O(1)
#   Brute Force


class Solution:
    def twoSum(self, nums, target):
        for i , j in enumerate(nums):
            for k, l in enumerate(nums):
                if j + l == target and i != k:
                    return [i, k]

solution1 = Solution()

answer = solution1.twoSum([2, 7, 11, 15], 9)
answer2 = solution1.twoSum([3, 2, 4], 6)
answer3 = solution1.twoSum([3, 2, 6], 6)
print(answer)
print(answer2)
print(answer3)

## Using HashMap/ Dictionary
## Time complexity -> 0(n)
## Space Complexity -> O(n)

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
