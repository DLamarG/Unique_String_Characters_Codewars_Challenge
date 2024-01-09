def solve(a,b):
    absent_letters = []
    for char in a:
        if char not in b:
            absent_letters.append(char)
    for char in b:
        if char not in a:
            absent_letters.append(char)
    return ''.join(absent_letters)


print(solve("xyab", "xzca")) #"ybzc"
print(solve("xyabb", "xzca")) #"ybbzc"
print(solve("abcd", "xyz")) #"abcdxyz"
print(solve("xxx", "xzca")) #"zca"