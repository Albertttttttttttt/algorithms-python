def sixfeetunder(bum):
    boom = 0
    while bum != 0:
        if bum % 5: bum -= 1
        else: bum //= 5
        boom += 1
    return boom

print(sixfeetunder(int(input())))