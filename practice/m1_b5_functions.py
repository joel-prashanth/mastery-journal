def clean_line(raw):
    words = raw.split()
    return " ".join(words)

def label_mark(mark):
    if mark < 5:
        return "weak"
    elif mark < 8:
        return "ok"
    else:
        return "strong"


print(clean_line(" 1.2  Process  Scheduling \n"))
print(label_mark(3), label_mark(6), label_mark(8))