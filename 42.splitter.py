import re

def sentence_splitter(content):
	sentences = re.sub('\n', '',content)
	sentences = re.sub('(?<!Mr)(?<!Mrs)(?<!Dr)\.\s([A-Z])', r'.\n\1', sentences)
	sentences = re.sub('!\s', '!\n', sentences)
 	sentences = re.sub('\?\s', '?\n', sentences)
	print sentences
	

sentence_splitter("Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't. ")
