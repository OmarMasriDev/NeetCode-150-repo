from collections import Counter

def top_c_frequent_elements(nums, c):
    # Step 1: Count the frequency of each element
    count = Counter(nums)

    # Step 2: Sort elements by frequency (high to low)
    sorted_elements = sorted(count.items(), key=lambda x: x[1], reverse=True)

    # Step 3: Return the Top C frequent elements
    return [item[0] for item in sorted_elements[:c]]

# Examlpe:
nums = [1, 1, 1, 2, 2, 3]
c = 2
print(top_c_frequent_elements(nums, c))
# Output = [1, 2])