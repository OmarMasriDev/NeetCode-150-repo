from collections import defaultdict

def group_anagrams(words):
    anagrams = defaultdict(list)

    for word in words:
        sorted_word = "".join(sorted(word))
        anagrams[sorted_word].append(word)

    return list(anagrams.values())
    
# Example:
words = ["below", "angle", "stone", "elbow", "angel", "notes"]
print(group_anagrams(words))