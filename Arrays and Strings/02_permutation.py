"""Check permutation: Given two strings write a method to decide if one is a permutation of the other"""
# Type-01 manually permutation determine
'''s = input()
result = []


def permutation(data, i, length):
    if i == length:
        result.append(''.join(data))
    else:
        for j in range(i, length):
            data[i], data[j] = data[j], data[i]
            permutation(data, i+1, length)


permutation(list(s), 0, len(s))
print(result)'''

# Type-02 Though this algorithm is not as optimal in some senses, it may be preferable in one sense: It's clean, simple
# and easy to understand
s = input()
t = input()


def makesort(s):
    return ''.join(sorted(s))


def isPermutation(s, t):
    if len(s) != len(t):
        return False
    return makesort(s) == (makesort(t))


if isPermutation(s, t):
    print("Yes")
else:
    print("No")

