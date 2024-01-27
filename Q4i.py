number = int(input())
sentence = input().split()
word = input()

characters = {'.', '،', '!', '?', ':', ';', '/', '(', ')'}


def shorterString(s1, s2):
    if len(s1) > len(s2):
        return s2
    else:
        return s1


def distance(s1, s2):
    shorter = shorterString(s1, s2)
    longer = ''
    if s1 == shorter:
        longer = s2
    else:
        longer = s1

    chandUnder = len(longer) - len(shorter)
    for i in range(chandUnder):
        shorter = f'{shorter}_'

    counter = 0
    for i in range(0, len(shorter)):
        if shorter[i] != longer[i]:
            counter += 1
    return counter


for i in range(len(sentence)):
    kalame = sentence[i]
    if kalame[-1] in characters:
        kalame = kalame[0:len(kalame) - 1]
    if distance(word, kalame) <= number:
        print(kalame)
