# M1 B1: Variables and types

## Why it matters
Every program is values held in variables. Knowing a value's type tells you what you can do with it and why some lines fail.

## The ideas
1. **No declaration keyword.** `age = 28`, with no `let`, `const` or `var`, and no semicolon.
2. **Dynamic but strong typing.** A variable can be reassigned to a different type, but Python will not mix types silently: `"age: " + 28` raises an error.
3. **Basic types:** `int`, `float`, `str`, `bool` (`True` and `False`, capitalised) and `None` (JS `null` and `undefined` in one).
4. **Division:** `7 / 2` is `3.5` (always a float), `7 // 2` is `3` (floor division).
5. **Integers never overflow:** `2 ** 100` is an exact whole number.
6. **`type(x)`** shows a value's type, like JS `typeof`.
7. **Naming:** `snake_case` for variables and functions.

## Common mistakes
- Adding a string and a number with `+`.
- Writing `true` or `none` in lowercase.
- Expecting `/` to give a whole number.

## Cheat sheet
- Assign: `name = "Joel"`
- Check a type: `type(name)`
- Decimal division: `/`, whole-number division: `//`
- Power: `**`
- Mix text and numbers: `f"age: {age}"`

## Self-check
1. What happens when you run `"5" + 5`, and why?
2. What do `7 / 2` and `7 // 2` give?
3. Which single value covers JS `null` and `undefined`?