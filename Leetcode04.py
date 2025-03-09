'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
'''
class Solution(object):
    def two_median_arrays(self, nums1, nums2):
        first = nums1
        second = nums2
        l_1 = len(first)
        l_2 = len(second)
        # Make sure L_2 is bigger, if not then swap
        if l_1 > l_2:
            first, second = second, first
            l_1, l_2 = l_2, l_1

        low = 0 # Initialize the lower bound for binary search
        high = l_1 # Initialize the upper bound for binary search
        halflen = (l_1 + l_2 + 1) // 2 # Calculate the 'half length' - the number of elements in the left partition of the combined array
        
        # Binary Search to find the correct partition
        while low <= high:
            partitionX = (low + high) // 2 # Calculate the partition index for 'first' array using binary search midpoint
            partitionY = halflen - partitionX # Calculate the corresponding partition index for 'second' array
            # We want the total elements in the left partitions (from both arrays) to be 'halflen'
            
            # Get the max element on the left side and min element on the right side for both partitions
            # Handle edge cases where partition is at the beginning (partition == 0) or end (partition == length)
            maxLeftX = float('-inf') if partitionX == 0 else first[partitionX -1]
            minRightX = float('inf') if partitionX == l_1 else first[partitionX]
            maxLeftY = float('-inf') if partitionY == 0 else second[partitionY -1]
            minRightY = float('inf') if partitionY == l_2 else second[partitionY]
            #print("maxLeftX", maxLeftX)
            #print("minRightX", minRightX)
            #print("maxLeftY", maxLeftY)
            #print("minRightY", minRightY)
            
            # Check if we have found the correct partition
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # Condition for correct partition is met
                # Now we can calculate the median based on whether the combined length is even or odd.
                if (l_1 + l_2) % 2 == 0:
                    # Median is the average of the two middle elements
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
                else:   # Odd total length
                # Median is the largest element of the left partition
                    return max(maxLeftX, maxLeftY)
                
            # If partitions are not correct, adjust binary search range
            elif maxLeftX > minRightY:
                # 'first' array's left partition is too large (elements are too big), so move partition to the left
                high = partitionX - 1
            else: # maxLeftY > minRightX (implicitly)
                # 'first' array's left partition is too small (elements are too small), so move partition to the right
                low = partitionX + 1
        return 0.0

if __name__ == '__main__':
    sol = Solution()
    print(sol.two_median_arrays([1,3], [2]))
    #Output: 2
    print(sol.two_median_arrays([1,2], [3,4]))
    #Output: 2.5