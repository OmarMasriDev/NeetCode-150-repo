from collections import Counter

def isAnagram(s: str, t: str):
    """
    check if strings are anagrams.

    parameters:
    s (str): First string.
    t (str): Second string.

    Returns:
    bool: True if 't' is an anagram of 's', False if otherwise.
    """
    # Using counter from collections to count frequency of each char in both str.
    # Counter creates a dictionary object where keys are char and values are their count.
    # If both str have same char counts, they are anagrams.
    return Counter(s) == Counter(t)

# Example:
if __name__ =="__main__":
    #Test:
    s = "anagram"
    t = "nagaram"

    # Check if two str are anagrams.
    result = isAnagram(s, t)

    # Output:
    print(f"Are '{s}' and '{t}' anagrams? {result}")