def count_words(string, words_set):
    counts = 0
    for word in words_set:
        if string.lower().find(word) >= 0:
            counts +=1
    return counts
