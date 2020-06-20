def validParenthesis(string):
    queue = []
    answer = True
    lst = []
    lst[:]= string
    print(lst)
    parens = {"(": ")", "{": "}", "[":"]"}
    opn = ["(", "{", "["]
    for char in lst:
        if char in opn:
            queue.append(char)
        elif queue == 0:
            return False
        elif char != parens[queue[-1]]:
            return False
        elif char == parens[queue[-1]]:
            queue.pop()
    if len(queue) != 0:
        return False
    return True


string_par= "({{}{[]}})"
print(validParenthesis(string_par))