def alternatingCharacters(s):
    index = 0
    for i in s:
        if i != None:
            index += 1
            if s[index] == s[index+1]:
                print(i)

alternatingCharacters('AAABBBAABB')