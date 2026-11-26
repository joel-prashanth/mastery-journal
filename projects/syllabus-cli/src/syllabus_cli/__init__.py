def clean_line(raw):
    words = raw.split()
    return " ".join(words)


def main() -> None:
    
    with open("syllabus.txt", "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
        # print(lines)
        counts = {}

        for line in lines:
            cleaned = clean_line(line)
            chapter = cleaned.split(".")[0]
            counts[chapter] = counts.get(chapter, 0) + 1

        for chapter in counts:
            print(f"chapter {chapter}: {counts[chapter]}")
        print(f"total: {len(lines)}")
