'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
'''
class Solution(object):
    def trapping_rain_water(self, height):
        if not height:
            return 0

        left, right = 0, len(height) - 1
        max_left, max_right = 0, 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    water += max_left - height[left]
                left += 1
            else:
                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    water += max_right - height[right]
                right -= 1

        return water

if __name__ == '__main__':
    sol = Solution()  # Create an instance of the 'Solution' class.
    #Example 1:
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    #Output: 6

    #Example 2:
    height2 = [4,2,0,3,2,5]
    #Output: 9

    print(sol.trapping_rain_water(height))
    print(sol.trapping_rain_water(height2))
