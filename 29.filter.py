def filter_long_words(words, n):
    return list(filter(lambda x: len(x) > n, words))
    

print(filter_long_words(['prashant','suraj', 'sushil', 'vishal'], 7))
