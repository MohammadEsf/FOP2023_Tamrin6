def create_stack():
    stack = []
    return stack


def isEmpty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)


def pop(stack):
    if isEmpty(stack):
        return "stack is empty"

    return stack.pop()


def top(stack):
    if isEmpty(stack):
        return "stack is empty"

    return stack[-1]


def jostojoo(s):
    for i in range(len(s)):
        if s[i] == 'x':
            return i  # TODO: maybe 1 based
    return ''


def merge_sort(s):
    if len(s) <= 1:
        return s

    mid = len(s) // 2
    left_half = s[:mid]
    right_half = s[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return ''.join(result)


class Kharchang:

    def chaap(self, s):
        if len(s) >= 10:
            return f'{s}{s[0:10]}'
        else:
            return f'{s}{s}'


class SpongeBob:
    def chaap(self, s):
        kharchang = Kharchang()
        result = kharchang.chaap(s)
        result = merge_sort(str(len(result)))

        return result


class Okhtapus:
    def chaap(self, s):
        s = f'{s}{jostojoo(s)}'
        stack = create_stack()

        i = 0
        while i < len(s):
            if isEmpty(stack) or top(stack) != s[i]:
                push(stack, s[i])
            elif i == len(s) - 1:
                push(stack , s[i])
            elif top(stack) == s[i] and s[i] == s[i + 1]:
                pop(stack)
                push(stack, ")0_0(")
                i += 1
            else:
                push(stack, s[i])
            i += 1

        res = ''
        while not isEmpty(stack):
            res = f'{res}{pop(stack)}'

        return res[::-1]


vorodi = input()
if vorodi[0] == 'm':
    kharchang = Kharchang()
    print(kharchang.chaap(vorodi).replace('tt', 'o'))
elif vorodi[0:2] == 'sb':
    spongeBob = SpongeBob()
    print(spongeBob.chaap(vorodi))
elif vorodi[0] == 's':
    okhtapus = Okhtapus()
    print(okhtapus.chaap(vorodi))
else:
    vorodi = vorodi[::-1]
    if vorodi[0] == 'm':
        kharchang = Kharchang()
        print(kharchang.chaap(vorodi).replace('tt', 'o'))
    elif vorodi[0:2] == 'sb':
        spongeBob = SpongeBob()
        print(spongeBob.chaap(vorodi))
    elif vorodi[0] == 's':
        okhtapus = Okhtapus()
        print(okhtapus.chaap(vorodi))
    else:
        print('invalid input')
