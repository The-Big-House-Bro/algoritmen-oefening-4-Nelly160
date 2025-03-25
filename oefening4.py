
def countTargetPairs(nums, target):
    n = len(nums) 
    count = 0  
    
    for getal in nums: 
        for i in range(n):
            for j in range(i + 1, n):  
                 if nums[i] + nums[j] < target:
                     count += 1
    
    return count

nums = [1, 2, 3, 4]
target = 5
result = countTargetPairs(nums, target)
print("Aantal paren:", result)