def findAtsign(s):
    for i in range(len(s)):
        if s[i] == '@':
            return i
    return -1

visitedDomains = set()

count = int(input())

for i in range(count):
    email = input()

    indexOfAtsign = findAtsign(email)
    if indexOfAtsign == -1:
        continue

    domain = email[indexOfAtsign+1:len(email)]

    visitedDomains.add(domain)

visitedDomains = sorted(visitedDomains)
for dom in visitedDomains:
    print(dom)

