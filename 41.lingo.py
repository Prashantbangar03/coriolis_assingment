from random import randrange

def lingo(words):
    hidden = words[randrange(0, len(words))]
    print hidden
    sym_map = {0: "%s", 1:"(%s)", 2: "[%s]"}
    def lingo_finder(guess):
        cenc = [(int(guess[i] == hidden[i])) + int(guess[i] in hidden) for i in range(5)] 
        print cenc
	print "".join([sym_map[cenc[i]]%guess[i] for i in range(5)])
        return hidden != guess
        

    if len(hidden) == 5:
        is_wrong=True
        while is_wrong:
            guess = raw_input()[:5]
            is_wrong = lingo_finder(guess.lower())
        print "You guessed it!"



lingo(['alley', 'tally', 'valet', 'tiger', 'house', 'cigar', 'opera', 'modem', 'horse', 'plane', 'white', 'fiery'])
