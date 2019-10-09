var twoSum = function(nums, target) {
    nums.sort(function(a, b){return a - b})
    console.log(nums)

    let i = 0
    let j = nums.length-1
    let key = nums[i] + nums[j]
    
    while (true) {
        console.log(nums[i] + nums[j])
        if (nums[i] + nums[j] > target) {
            j--
            console.log("too big")
        }
        else if (nums[i] + nums[j] < target) {
            i++
            console.log("too small")
        }
        else {
            arr = []
            arr.push(i)
            arr.push(j)
            return arr
        }
        
    }
    
}
//Given nums = [2, 7, 11, 15], target = 9,
console.log(twoSum([2,7,11,15],9))
console.log(twoSum([-1,-2,-3,-4,-5],-8))