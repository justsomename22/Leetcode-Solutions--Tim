'''
	Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
    You may assume all four edges of the grid are all surrounded by water.
'''
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # **Algorithm Explanation:**
        # This function counts the number of islands in a 2D grid using Depth First Search (DFS).
        # An island is formed by connected '1's (land) horizontally or vertically and surrounded by '0's (water).
        # The algorithm works by iterating through each cell in the grid.
        # When it encounters a '1' (land) that hasn't been visited yet, it means a new island is found.
        # It then uses DFS to explore the entire island, marking all connected '1's as visited.
        # This prevents recounting the same island if we encounter another '1' cell belonging to it.

        # **Base Case: Empty Grid**
        if not grid:
            return 0  # If the grid is empty (no rows), there are no islands, so return 0.

        # **Get Grid Dimensions**
        rows, cols = len(grid), len(grid[0])  # Get the number of rows and columns in the input grid.

        # **Initialize Visited Grid**
        # Create a 2D boolean grid 'visited' of the same dimensions as 'grid'.
        # 'visited[r][c]' will be True if the cell at (r, c) has been visited/explored, and False otherwise.
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        # **Initialize Island Counter**
        num_islands = 0  # Initialize a counter to keep track of the number of islands found.

        # **Depth First Search (DFS) Function**
        def dfs(row, col):
            """
            Recursively explores the island starting from cell (row, col) and marks all connected land cells as visited.
            :param row: The row index of the current cell.
            :param col: The column index of the current cell.
            :return: None (modifies the 'visited' grid in place).
            """
            # **Base Cases for Recursion Termination**
            # 1. Out of Bounds Check:
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return  # If the current cell is outside the grid boundaries, stop recursion.
            # 2. Already Visited Check:
            if visited[row][col]:
                return  # If the current cell has already been visited, stop recursion to avoid infinite loops.
            # 3. Water Cell Check:
            if grid[row][col] == '0':
                return  # If the current cell is water ('0'), it's not part of an island, so stop recursion.

            # **Mark Current Cell as Visited**
            visited[row][col] = True  # Mark the current land cell (row, col) as visited.

            # **Recursive Calls to Explore Neighbors**
            # Explore adjacent cells in all four directions (up, down, left, right):
            dfs(row + 1, col)  # Explore the cell below the current cell.
            dfs(row - 1, col)  # Explore the cell above the current cell.
            dfs(row, col + 1)  # Explore the cell to the right of the current cell.
            dfs(row, col - 1)  # Explore the cell to the left of the current cell.
            # The recursion will continue until it hits water, grid boundaries, or already visited cells,
            # effectively exploring the entire connected island.


        # **Iterate Through the Grid to Find Islands**
        for r in range(rows):  # Iterate through each row index from 0 to rows-1.
            for c in range(cols):  # Iterate through each column index from 0 to cols-1.
                # **Check for Unvisited Land Cell**
                if grid[r][c] == '1' and not visited[r][c]:
                    # If the current cell is land ('1') and has not been visited yet:
                    num_islands += 1  # Increment the island counter because we've found a new island.
                    dfs(r, c)  # Start DFS from this land cell to explore and mark the entire island as visited.
                    # The DFS call will explore all connected land cells belonging to the current island.

        # **Return the Total Number of Islands**
        return num_islands  # Return the final count of islands found in the grid.


if __name__ == '__main__':
    sol = Solution()  # Create an instance of the 'Solution' class to use its methods.

    # **Example Input Grid 1**
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    returned_result = sol.numIslands(grid)  # Call the numIslands method with the input grid 1 and store the result.

    # **Example Input Grid 2**
    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    returned_result_2 = sol.numIslands(grid2) # You can uncomment this to test with grid2
    print(returned_result_2) # You can uncomment this to print the result for grid2

    print(returned_result)  # Print the returned result (number of islands) for grid1.