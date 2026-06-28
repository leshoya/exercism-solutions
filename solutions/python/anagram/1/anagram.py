from collections import Counter
def find_anagrams(word, candidates):
    res = []
    word_lower = word.lower()
    word_count = Counter(word_lower)
    for candidate in candidates:
        candidate_lower = candidate.lower()
        if candidate_lower == word_lower:
            continue
        if Counter(candidate_lower) == word_count:
            res.append(candidate)
    return res
