#[1,8,6,2,5,4,8,3,7]


def maxArea(height) -> int:
    i = 0
    j = len(height) - 1
    area = 0
    
    while (i<j):
        area = max(min(height[i],height[len(height)-1]) * (j - i),area)
        




maxArea([1,8,6,2,5,4,8,3,7])


        