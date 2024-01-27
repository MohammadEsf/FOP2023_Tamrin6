def splitCharAndNumber(string):
    char = string[0]

    number = string[1 : len(string)]
    number = int(number)

    result = [number , char]
    return result

chars = input().split()

# print(chars)
word = []

for char in chars:
    a = splitCharAndNumber(char)
    word.append(a)

word = sorted(word)

kalame = ''

for i in word:
    n = i[1]
    kalame = kalame + n

print(kalame)