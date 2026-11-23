# M1 B3: Lists and dicts

## Why it matters
Almost every program holds collections: a list of topics, a dict of marks. In Sarvantha, the syllabus tree and the revision queue are built from these two.

## The ideas
1. **List = JS array.** `append` is `push`, `len(items)`, `items[0]`, `items[-1]` (last), `x in items`.
2. **Dict = JS object.** `marks["os"]` reads, `marks["cn"] = 5` adds or changes, `"os" in marks` checks keys.
3. **Missing key:** `marks["x"]` raises KeyError. `marks.get("x")` returns None.
4. **Lists and dicts are edited in place.** Methods like `append` change them and return `None`. Never write `items = items.append(x)`.
5. **Strings are never edited in place.** A string method returns a new string. Write `s = s.upper()` to keep it.

## The memory hook
A list is like a Google Doc: editing changes the same document. A string is like a photo: a filter makes a new copy, and you need `=` to keep it.

## Common mistakes
- Storing the result of `append` (you get `None`).
- Calling `s.upper()` with no `=` and expecting `s` to change.
- Reading a missing dict key with `[]` and getting a KeyError.

## Cheat sheet
- Add to a list: `items.append(x)` (no `=`)
- Add or change a dict entry: `marks[key] = value`
- Safe dict read: `marks.get(key)`
- Keep a changed string: `s = s.upper()`

## Self-check
1. What does `append` return?
2. Why does `s.upper()` alone not change `s`?
3. What is the difference between `marks["x"]` and `marks.get("x")` when `"x"` is missing?
4. What does `items[-1]` give?