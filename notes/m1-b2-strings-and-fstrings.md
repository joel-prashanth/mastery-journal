# M1 B2: Strings and f-strings

## Why it matters
Almost every real input starts as a string: a syllabus line, a file row, a user's text. Cleaning and formatting strings is the first job of nearly every program.

## The ideas

1. **Strings are immutable.** A method returns a new string. If you do not keep the result, it is lost: `s = s.upper()`.
2. **Method names (JS to Python):**
   - `trim()` is `strip()`
   - `toLowerCase()` is `lower()`
   - `includes("x")` is `"x" in s`
   - `s.length` is `len(s)`
   - `s.split(/\s+/)` is `s.split()`
   - `arr.join(", ")` is `", ".join(items)`
   - `` `${a}` `` is `f"{a}"`
3. **`split()` with no argument** cuts on any run of whitespace and drops empty pieces. `split(" ")` does not.
4. **`join` belongs to the separator:** `" ".join(words)`, never `words.join(" ")`.
5. **f-strings** need the `f` before the opening quote. Any expression can go inside `{}`.
6. **Indexing and slicing (preview):** `words[0]` is the first item. `words[1:]` is everything from index 1 on, like `slice(1)` in JS.
7. **`\n` is a newline.** Lines read from a file end with one. `strip()` removes it.

## Common mistakes
- Calling `s.lower()` and forgetting to assign the result.
- Writing `"{name}"` without the `f`, so the braces print literally.
- Writing `words.join(" ")`, which raises an error.
- Forgetting that `in` is case-sensitive.
- Expecting `strip()` to remove spaces in the middle.

## Cheat sheet
- Clean the ends: `s.strip()`
- Clean the middle too: `" ".join(s.split())`
- Test for a piece: `"x" in s`
- Build text: `f"{a} | {b}"`

## Self-check
1. Why does `s.upper()` on its own line not change `s`?
2. What is the difference between `s.split()` and `s.split(" ")`?
3. Whose method is `join`?
4. What does `words[1:]` return for `["1.2", "Process", "Scheduling"]`?
5. What happens if you leave off the `f` in `"{name} is here"`?