def capitalize(s):
    """комментарий первый"""
    result = ""
    capitalize_next = True

    for i in range(len(s)):
        if s[i] == " ":
            result += " "
            capitalize_next = True
        elif capitalize_next:
            result += s[i].upper()
            capitalize_next = False
        else:
            result += s[i]

        if s[i] in ".!?":
            capitalize_next = True

    return result

def emphasise(txt):
    """коментарий четвертого задания"""
    return ' '.join(w[0].upper()+w[1:].lower() for w in txt.split())