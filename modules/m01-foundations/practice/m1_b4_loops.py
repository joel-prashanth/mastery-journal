topics = ["os", "dbms", "cn"]
marks = {"os": 8, "dbms": 6, "cn": 4}

for topic in topics:
    mark = marks[topic]
    if mark < 5:
        label = "weak"
    elif mark < 8:
        label = "ok"
    else:
        label = "strong"
    print(f"{topic}: {mark} ({label})")
