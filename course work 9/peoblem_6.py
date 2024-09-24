# 6. trap rain water 

def trap(height):
    if not height:
        return 0
    
    # Initialize two pointers and the variables to store the trapped water
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    ans = 0

    # Move the two pointers toward each other
    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            ans += max(0, left_max - height[left])
        else:
            right -= 1
            right_max = max(right_max, height[right])
            ans += max(0, right_max - height[right])
    
    return ans