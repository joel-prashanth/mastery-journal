raw = "  1.2   Process   Scheduling \n"
clean = raw.strip()
# print(clean)
# print(len(raw), len(clean))


words = clean.split()

tidy = " ".join(words)
print(tidy)
print(words)

number = words[0]
title = " ".join(words[1:]).lower()
print(f"{number} | {title} ({len(title)} chars)")