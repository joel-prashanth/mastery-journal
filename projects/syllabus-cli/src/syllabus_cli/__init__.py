def parse_line(line):

    # clean the line first: split, then join with one space
    cleaned_line = " ".join(line.split())

    # split the cleaned line at the first space only: number, title
    number, title = cleaned_line.split(" ", 1)

    # chapter = the part of number before the dot
    chapter = number.split(".")[0]

    # return chapter, number, title (one return line)
    return chapter, number, title


def main() -> None:

    with open("syllabus.txt", "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
        # print(lines)
        counts = {}

        for line in lines:
            chapter, number, title = parse_line(line)
            counts[chapter] = counts.get(chapter, 0) + 1

        for chapter in counts:
            print(f"chapter {chapter}: {counts[chapter]}")
        print(f"total: {len(lines)}")
