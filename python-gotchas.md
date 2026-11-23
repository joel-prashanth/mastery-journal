# Python gotchas

One entry per surprise: what I expected, what happened, the rule.

## 2026-11-23: a string method did not change my string
- **Expected:** `s.upper()` on its own line would make `s` uppercase.
- **Happened:** `print(s)` still showed `abc`.
- **Rule:** strings are immutable. Methods return a new string, so keep the result with `s = s.upper()`.