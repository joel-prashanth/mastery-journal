# M1 B6: Files, the main guard and counting

## Why it matters
Sarvantha reads a student's syllabus from a file, cleans each line and counts
topics. This block puts Module 1 together in one runnable project.

## Concepts
- Read a file:
  `with open("syllabus.txt", encoding="utf-8") as f: lines = f.read().splitlines()`
  `with` closes the file when its body ends. `splitlines()` gives one string per line.
- Main guard: put the work in `def main():`, then end the file with
  `if __name__ == "__main__": main()`.
  `__name__` is `"__main__"` only when the file is run directly. On `import helper` it is `"helper"`.
- Importing a file still runs its top-level lines, but not a guard that is False.
- Count with a dict: `counts[key] = counts.get(key, 0) + 1`.
- `"1.2".split(".")[0]` gives the string `"1"`, not the number 1.
- uv project: `uv init` makes pyproject.toml and main.py. `uv run main.py` runs it.

## JS comparison
| JS | Python |
| --- | --- |
| `fs.readFileSync(p, "utf8").split("\n")` | `open(...).read().splitlines()` inside `with` |
| `require.main === module` | `__name__ == "__main__"` |
| `package.json`, `npm run` | `pyproject.toml`, `uv run` |
| `counts[k] = (counts[k] \|\| 0) + 1` | `counts[k] = counts.get(k, 0) + 1` |

## Common mistakes
- Forgetting `encoding="utf-8"` on Windows.
- `counts[key] += 1` on a new key: KeyError.
- Comparing `"1"` with `1`: always False.
- Expecting `import` to skip top-level code. Only the guarded code is skipped.
- Running from the wrong folder, so `open("syllabus.txt")` cannot find the file.

## Cheat sheet
```python
def main():
    with open("syllabus.txt", encoding="utf-8") as f:
        lines = f.read().splitlines()
    counts = {}
    for line in lines:
        chapter = line.split(".")[0]
        counts[chapter] = counts.get(chapter, 0) + 1
    print(counts)


if __name__ == "__main__":
    main()
```

## Self-check
1. Why does `with` matter when reading a file?
2. What is `__name__` inside a file you import?
3. Why does `counts[key] += 1` fail on a new key?