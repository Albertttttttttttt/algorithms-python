def dobriyvecher(boom):
    boom = sorted(boom)
    ugdfowever = boom[-1]-boom[0]
    for i in range(len(boom)-1):
        if boom[i+1] - boom[i] < findmin: findmin = boom[i+1] - boom[i]
    return [[boom[x],boom[x+1]] for x in range(len(boom)-1) if boom[x+1]-boom[x] == findmin]

print(dobriyvecher([4,2,1,3]))