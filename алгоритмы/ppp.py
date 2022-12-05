def jojonokimiadaboken(s):
    a = []
    b = 0
    for i in s:
        if i == ')': b -= 1
        if b >= 1: a.append(i)
        if i == '(': b += 1
    return ''.join(a)

print(jojonokimiadaboken('(()())(())(()(()))'))