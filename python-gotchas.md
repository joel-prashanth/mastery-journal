# Python gotchas

One entry per surprise: what I expected, what happened, the rule.

## 2026-11-23: a string method did not change my string
- **Expected:** `s.upper()` on its own line would make `s` uppercase.
- **Happened:** `print(s)` still showed `abc`.
- **Rule:** strings are immutable. Methods return a new string, so keep the result with `s = s.upper()`.


## 2026-11-23: I stored the result of a list method
- **Expected:** `items = items.append("c")` would give me the list with "c" added.
- **Happened:** `print(items)` showed `None`.
- **Rule:** list methods like `append` edit the list itself and return nothing. Write `items.append("c")` on its own, with no `=`.


## 2026-11-26: I tried to add a string and a number
- **Expected:** `"age: " + 28` would give `"age: 28"`, like JS.
- **Happened:** Python raised a TypeError.
- **Rule:** Python does not mix text and numbers with `+`. Use an f-string: `f"age: {28}"`.


## 2026-11-26: an empty list or dict is falsy in Python
- **Expected:** `if {}:` would run, because empty objects are truthy in JS.
- **Happened:** `bool({})` is `False`, so the branch is skipped.
- **Rule:** in Python, anything with nothing in it (`0`, `""`, `[]`, `{}`, `None`) is falsy. A non-empty string like `"0"` is truthy.

## Calling a function above its def (M1 B5)
- Expected: Python finds `double` anywhere in the file, like JS hoisting.
- Happened: `NameError`, because `def` runs when Python reaches it.
- Rule: define the function above the line that calls it.

## Storing the result of a function with no return (M1 B5)
- Expected: `result = add_mark(scores)` gives back the edited list.
- Happened: `scores` changed in place, but `result` was `None`.
- Rule: an edit and a returned value are separate. Only `return` hands a value back.

## Relative path in open() (M1 B6)
- Expected: `open("../../syllabus.txt")` finds the file next to the Python file.
- Happened: `FileNotFoundError`. Relative paths start from the folder where the command runs.
- Rule: check which folder you ran from. `uv run` from the project root means `"syllabus.txt"`.

## Passing the list instead of the item (M1 B6)
- Expected: `clean_line(lines)` cleans every line.
- Happened: `AttributeError: 'list' object has no attribute 'split'`.
- Rule: inside `for line in lines:`, the function gets `line`, one string, never `lines`.

## print inside the counting loop (M1 B6)
- Expected: one total per chapter.
- Happened: a running count printed on every pass.
- Rule: finish counting in one loop, then print in a second loop at the same level.

## join belongs to the separator (M2 B1)
- Expected: `line.split().join(" ")` joins the words.
- Happened: `AttributeError`, because a list has no `join`.
- Rule: write `" ".join(line.split())`. The separator string owns `join`.

## One-item tuple needs a comma (M2 B1)
- Expected: `(5)` is a tuple.
- Happened: it is the int 5. The comma makes the tuple.
- Rule: `(5,)`.

## No return means None, and None can't be unpacked (M2 B1)
- Expected: `a, b, c = parse_line(...)` works once the function prints the values.
- Happened: `TypeError: cannot unpack non-iterable NoneType`.
- Rule: unpacking needs `return a, b, c`. Printing is not returning.

## Starred names are lists (M2 B1)
- Expected: `first, *rest = (1, 2, 3)` gives a tuple for `rest`.
- Happened: `rest` is the list `[2, 3]`.
- Rule: a starred name always collects into a list.