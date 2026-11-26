# M1 B4: Control flow and loops

## Why it matters
Programs make decisions and repeat work. Every parser, scheduler and report in Sarvantha is an `if` inside a `for`.

## The ideas
1. **Blocks use a colon and indentation** (4 spaces), not braces. Wrong indentation is an error.
2. **`if / elif / else`**, with no parentheses around the condition.
3. **Logic words:** `and`, `or`, `not`. Equality is only `==`.
4. **Truthiness:** falsy is `0`, `""`, `[]`, `{}`, `None`, `False`. Everything else is truthy, including `"0"`.
5. **`for item in items:`** goes straight over the items. No `i++`.
6. **`range(3)`** gives 0, 1, 2 and stops before 3.
7. **Once a branch runs,** the later `elif` and `else` are skipped.

## Common mistakes
- Forgetting the colon at the end of the `for` or `if` line.
- Indenting inconsistently, so a line falls inside or outside a block by accident.
- Assuming `[]` or `{}` is truthy, as in JS.
- Expecting `range(3)` to include 3.

## Cheat sheet
- Loop over a list: `for topic in topics:`
- Count: `for n in range(3):`
- Branch: `if a: ... elif b: ... else: ...`
- Is a list not empty: `if items:`

## Self-check
1. What does `range(3)` give?
2. Which of `[]`, `"0"`, `0` and `{}` are falsy?
3. What happens if the line after `for ...:` is not indented?