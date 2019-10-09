def twoSum(nums,target):
    i = 0
    j = len(nums)-1

    while (True):
        val = nums[i]+nums[j]

        if (val > target):
            j -= 1
        elif (val < target):
            i += 1
        else:
            return [i,j]


print(twoSum([2,7,11,15,33,3434],26))       