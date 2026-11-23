topics = ["os", "dbms", "cn"]

topics.append("toc")

print(topics)
print(len(topics), topics[0], topics[-1])


marks = {"os": 8, "dbms": 6}
marks["cn"] = 8

print(marks)
print(marks["os"], marks.get("toc"), "cn" in marks)

print(f"{topics[0]}: {marks[topics[0]]}")
print(f"{topics[1]}: {marks[topics[1]]}")