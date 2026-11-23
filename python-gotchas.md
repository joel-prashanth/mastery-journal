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