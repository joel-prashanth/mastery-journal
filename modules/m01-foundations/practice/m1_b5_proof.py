def add_mark(marks):
    marks.append(7)


def add_mark_and_return(marks):
    marks.append(7)
    return marks


scores = [4, 9]
result = add_mark(scores)
print(scores, result)


scores2 = [4, 9]
result2 = add_mark_and_return(scores2)
print(scores2, result2)
