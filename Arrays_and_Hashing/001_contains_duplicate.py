def contains_duplicate(nums):
    # Create an empty dictionary to store elements
    elements = {}

    # Cycle through each number
    for num in nums:
        if num in elements:
            return True
        
        # Otherwise, add element to dicionary
        elements[num] = True

    # If no duplicates found, return false
    return False

# Example:
nums1 = [1, 2, 3, 4]
nums2 = [1, 2, 2, 3]

print(contains_duplicate(nums1))
print(contains_duplicate(nums2))

