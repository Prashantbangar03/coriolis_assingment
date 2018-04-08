def make_3sg_form(inputword):

    if inputword.endswith('y'):
        thirdForm=inputword+'ies'
    
    elif inputword.endswith(('o','ch','s','sh','x','z')):
        thirdForm=inputword+'es'
    
    else:
        thirdForm=inputword+'s'
 
    return thirdForm
 
print(make_3sg_form('Understand'))
 
