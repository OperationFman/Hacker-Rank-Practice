def makeAnagram(a, b):
    x = set(a) & set(b)
    aDel = len(a) - len(x)
    bDel = len(b) - len(x)
    print(aDel)
    print(bDel)
    return aDel + bDel

print(makeAnagram('fcrx', 'jxwt'))