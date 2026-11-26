# M1 B5: Functions

## Why it matters
Sarvantha will do the same jobs over and over: clean a line, label a mark,
count topics. A function gives each job a name so you write it once and call
it everywhere.

## Concepts
- `def name(params):` then an indented body. No braces, no `function` keyword.
- `return value` hands a value back to the caller and ends the function.
- No `return` means the function gives back `None`.
- `print` shows something on screen. `return` gives it back so you can store it.
- Defaults: `def label(mark, low=5):`. Call by name: `label(7, low=6)`.
- Define before you call. A `def` is a command that runs when Python reaches it.
  No hoisting like JS function declarations.
- A function gets the same list/dict you pass in, not a copy. Edits inside
  show outside. Strings and numbers cannot be edited, so they never change.

## Edit vs return (two channels)
1. Edits: `marks.append(7)` changes the caller's list.
2. Returned value: only what follows `return`. No return = `None`.
`result = add_mark(scores)` stores only channel 2.

## JS comparison
| JS | Python |
| --- | --- |
| `function clean(line) { ... }` | `def clean(line):` |
| hoisted, callable above | must be defined above the call |
| no return gives `undefined` | no return gives `None` |
| `(x = 5) =>` defaults | `def f(x=5):` |

## Common mistakes
- Using `print` where you needed `return`, then getting `None` back.
- Storing the result of a function that only edits in place: `b = add_tag(a)`.
- Calling a function above its `def`: NameError.
- Forgetting the colon or the indentation.

## Cheat sheet
```python
def clean(line):
    return " ".join(line.split())


def label(mark):
    if mark < 5:
        return "weak"
    elif mark < 8:
        return "ok"
    return "strong"
```

## Self-check
1. What does a function with no `return` give back?
2. Why can `print(double(4))` fail above its `def`?
3. If a function appends to a list you passed in, does your list change?