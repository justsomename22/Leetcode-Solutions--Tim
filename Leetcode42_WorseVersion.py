'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
O(n^2) version
'''
class Solution(object):
    def trapping_rain_water(self, height):
        if not height:
            return 0
        
        max_height = max(height)
        width = len(height)
        
        # Calculate air (0)
        matrix = [[0 for _ in range(width)] for _ in range(max_height)]
        
        # Calculate land (1)
        for col, h in enumerate(height):
            for row in range(h):
                matrix[max_height - 1 - row][col] = 1
        
        # Calculate water (2)
        water = 0
        
        for col in range(width):
            # Skip edges as they can't trap water
            if col == 0 or col == width - 1:
                continue
            # Find maximum height to the left
            max_left = 0
            for left in range(col):
                max_left = max(max_left, height[left])
            # Find maximum height to the right
            max_right = 0
            for right in range(col + 1, width):
                max_right = max(max_right, height[right])
                
            water_height = min(max_left, max_right) - height[col]
            if water_height > 0:
                water += water_height
                
                for row in range(water_height):
                    matrix[max_height - height[col] - 1 - row][col] = 2
        
        
        print("\n(0=air, 1=solid, 2=water):")
        for row in matrix:
            print(row)
        
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
    #print(sol.trapping_rain_water(height2))