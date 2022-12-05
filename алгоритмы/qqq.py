def numwhiteIntee(white,tee):
    return len([x for x in tee if x in white])

print(numwhiteIntee('aA','aAAbbbb'))