#           eoijjnsoiwioo soiw#qo #     wij@sioj#@@ isjij\n woij#  #
text = input()

indexOfHashtagsToRemove = set()

for i in range(len(text)):
    if text[i] == '@':
        for j in range(i + 1, len(text)):
            if text[j] == '#' and j not in indexOfHashtagsToRemove:
                indexOfHashtagsToRemove.add(j)
                break

newText = ''.join([text[i] for i in range(len(text)) if i not in indexOfHashtagsToRemove])
newText = ' '.join(newText.split())

newText = newText.replace('\\n' , '\n')

print('Formatted Text: ' , end='')
print(newText)