def validParenthesis(string):
    queue = []
    answer = True
    lst = []
    lst[:]= string
    print(lst)
    opn = ["(", "{", "["]
    for char in lst:
        if char in opn:
            queue.append(char)
        elif queue[-1] == "(":
            if char == ")":
                queue.pop()
            else:
                return False
        elif queue[-1] == "{":
            if char == "}":
                queue.pop()
            else:
                return False            
        elif queue[-1] == "[":
            if char == "]":
                queue.pop()
            else:
                return False

    if len(queue) != 0:
        return False
    return True


string_par= "({{}{]}})"
print(validParenthesis(string_par))