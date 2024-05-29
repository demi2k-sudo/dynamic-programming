'''
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of
the symbols '+' and '-' before each integer in nums and then 
concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and 
a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, 
which evaluates to target.
'''

def findTargetSumWays(nums, target: int) -> int:
    def Solve(currentSum, loc, memo=None):
        if memo is None:
            memo = {}
        if (loc,currentSum) in memo:
            return memo[(loc,currentSum)]
        if loc == len(nums):
            if currentSum == target:
                memo[(loc,currentSum)] =1
                return 1
            else:
                memo[(loc,currentSum)] =0
                return 0
        
        # Without changing the current element
        count = Solve(currentSum+nums[loc], loc + 1, memo)
        
        # Change the current element by flipping its sign
        
        count += Solve(currentSum-nums[loc], loc + 1, memo)
        
        
        memo[(loc,currentSum)] = count
        return count
    
    return Solve(0,0)

#test cases'
nums = [1,1,1,1,1]
target = 3
print(findTargetSumWays(nums, target))
nums = [1]
target = 1
print(findTargetSumWays(nums, target))
nums = [1,2]
target = 2
print(findTargetSumWays(nums, target))
nums = [1,2,3]
target = 2
print(findTargetSumWays(nums, target))