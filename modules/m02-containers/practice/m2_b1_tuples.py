def parse_line(line):

    # clean the line first: split, then join with one space
    cleaned_line = " ".join(line.split())

    # split the cleaned line at the first space only: number, title
    number, title = cleaned_line.split(" ", 1)

    # chapter = the part of number before the dot
    chapter = number.split(".")[0]

    # return chapter, number, title (one return line)
    return chapter, number, title


chapter, number, title = parse_line("  1.2   Process   Scheduling \n")
print(chapter, number, title)
