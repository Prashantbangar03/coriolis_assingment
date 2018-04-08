import re
 
def correct(inputString):
 
    correctedString = re.sub('\ +',' ',inputString)
 
    correctedString = re.sub('\.','. ',correctedString)
 
    return correctedString 
 
 
 
inputString = "This   is  very funny  and    cool.Indeed!. But      you should.try  this also"
 
print(correct(inputString))
