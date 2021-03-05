from collections import Counter

def makeAnagram(a, b):
    count_a = Counter(a)
    count_b = Counter(b)
    count_a.subtract(count_b)
    return sum(abs(i) for i in count_a.values())

print(makeAnagram('fcrx', 'jxwt'))