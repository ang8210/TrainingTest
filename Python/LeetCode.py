
# TwoSum
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return [i, j]


# Palindrome Number
def isPalindrome(self, x: int) -> bool:
    if x < 0:
        return False
    tmp = x
    sol = 0
    while tmp > 0:
        sol = sol * 10 + tmp % 10
        tmp = int(tmp/10)
    return sol == x


# Search Insert Position
def searchInsert(self, nums: List[int], target: int) -> int:
    for i in range(len(nums)):
        if target <= nums[i]:
            return i
    return len(nums)


# Single Number
def singleNumber(self, nums: List[int]) -> int:
    ans = 0
    for i in range(len(nums)):
        ans = ans ^ nums[i]
    return ans


# Power of Two
def isPowerOfTwo(self, n: int) -> bool:
    return n > 0 and n & n-1 == 0


# Ugly Number
def isUgly(self, n: int) -> bool:
    if n == 1:
        return True
    elif n <= 0:
        return False
    else:
        while n % 2 == 0:
            n = n/2
        while n % 3 == 0:
            n = n/3
        while n % 5 == 0:
            n = n/5
        return n == 1


# Move Zeroes
#Do not return anything, modify nums in-place instead.
def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        right = 0
        while right < len(nums):
            if nums[left] != 0:
                left = left + 1
            elif nums[right] != 0:
                tmp = nums[left]
                nums[left] = nums[right]
                left = left + 1
                nums[right] = tmp
            right = right + 1

