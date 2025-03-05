'''
	Given a string, find the length of the longest substring without repeating characters.
	Examples:
	Given "abcabcbb", the answer is "abc", which the length is 3.
	Given "bbbbb", the answer is "b", with the length of 1.
	Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
class Solution(object):
    def length_of_longest_substring(self, s):
        """
        Finds the length of the longest substring without repeating characters.

        Args:
            s (str): The input string.
        Returns:
            int: The length of the longest substring without repeating characters.
        """
        start = max_len = 0  # Initialize the start index of the sliding window and the maximum length found so far.
        seen = set()  # Initialize a set to keep track of characters in the current window.

        for end, char in enumerate(s):  # Iterate through the string using enumerate to get both index (end) and character (char).
            while char in seen:  # If the current character is already in the 'seen' set (meaning it's a repeating character in the current window):
                seen.remove(s[start])  # Remove the character at the 'start' index from the 'seen' set. This effectively shrinks the window from the left.
                start += 1  # Move the 'start' index one step to the right, effectively sliding the window.
                # The while loop continues to shrink the window from the left until the repeating character 'char' is no longer in the 'seen' set.

            seen.add(char)  # Once the 'while' loop finishes (meaning 'char' is not a repeating character in the current window), add 'char' to the 'seen' set.
                              # This expands the window to the right to include the current character.
            max_len = max(max_len, end - start + 1)  # Update 'max_len' if the current window's length is greater than the current 'max_len'.
                                                      # The current window length is calculated as 'end - start + 1'.

        return max_len  # After iterating through the entire string, return the maximum length found.

if __name__ == '__main__':
    sol = Solution()  # Create an instance of the 'Solution' class.
    input_string = "abcabcbb"  # Define the input string for which we want to find the length of the longest substring without repeating characters.
    returned_result_4 = sol.length_of_longest_substring(input_string)  # Call the 'length_of_longest_substring' method with the input string and store the result.
    print(returned_result_4)  
    # Print the returned result to the console. For the input "abcabcbb", 
    #the longest substring without repeating characters is "abc", which has length 3. So, the output will be 3.