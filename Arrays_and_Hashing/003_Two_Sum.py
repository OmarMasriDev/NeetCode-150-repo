def two_sum(nums, target):
    """
    This function finds two numbers in list 'nums' that add up to 'target'.
    It returns the indices of these two numbers as a list.

    nums: List of integers
    target: Target sum
    """

    num_map = {} # Dictionary to store numbers and their indices

    # Iterate through the list with both index and value
    for i, num in enumerate(nums):
        diff = target - num # Calculate the difference to reach the target

        # Check if the difference is already in dictionary
        if diff in num_map:
            return [num_map[diff], i] # Returns the indices of the two numbers
        
        # Store the current number with the index in dictionary
        num_map[num] = i

    return [] # Return an empty list

# Example:
nums = [2, 4, 11, 6]
target = 6
print(two_sum(nums, target)) # Output: [0, 1]
        