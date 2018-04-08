def translate(words):
    lexicon = {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott", "new": "nytt", "year": "ar"}
    return list(map(lambda word: lexicon[word], words)) 
    
print (translate(["merry","christmas","happy","new","year"]))

