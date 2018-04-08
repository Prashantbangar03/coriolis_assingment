def map_to_lengths_for(words):
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths


def map_to_lengths_map(words):
    
    wordlist=list(map(len, words))
    print(wordlist)

def map_to_lengths_lists(words):
    return [len(word) for word in words]


words = ['abv', 'try me', 'test']
print (map_to_lengths_for(words))
map_to_lengths_map(words)
print (map_to_lengths_lists(words))
