numbers = list(map(int, input().split()))
majmoo = int(input())

indexes = dict()
matloobs = set()

for i, num in enumerate(numbers):
    indexes[num] = i

for i, num1 in enumerate(numbers):
    num2 = majmoo - num1
    if num2 in indexes and indexes[num2] > i:
        matloobs.add((num1, num2))

result = [indexes[c[0]] + indexes[c[1]] for c in matloobs]
result.sort()

if len(result) == 0:
    print('Not Found!')
else:
    for num in result:
        print(num)