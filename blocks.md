# Block log

## M1 B2: Strings and f-strings (2026-11-23)
- Outcome: practice/m1_b2_strings.py cleans a syllabus line and prints `1.2 | process scheduling (18 chars)`.
- Quiz A 2/3, Quiz B 1/3, retake 1/2. Weak spot: string methods return new strings.
- Gotcha logged: `s.upper()` without `=` does not change `s`.
- Ship notes: Cost none. Scale none. Maintain none. Business none yet.
- In my words, what I will remember: Changed strings will only persist if they are re-assigned while changing.


## M1 B3: Lists and dicts (2026-11-23)
- Outcome: practice/m1_b3_collections.py stores topics in a list and marks in a dict and reads each mark back.
- Quiz A 3/3, Quiz B 1/3, retake 2/2. Weak spot: in-place (lists, dicts) versus new value (strings).
- Gotcha logged: storing the result of `append` gives `None`.
- Ship notes: Cost none. Scale none. Maintain none. Business none yet.
- In my words, what I will remember: 


## M1 B4: Control flow and loops (2026-11-26)
- Outcome: practice/m1_b4_loops.py loops over topics, looks up each mark and labels it weak, ok or strong.
- Quiz A 3/3, Quiz B 2/3. Missed: falsy values (empty dict and empty string are falsy).
- Gotcha logged: empty list or dict is falsy in Python, truthy in JS.
- Ship notes: Cost none. Scale none. Maintain none. Business none yet.
- In my words, what I will remember: Empty means false in Python. (Lists or Strings)


## M1 B5: Functions
- Quiz A 3/3, Quiz B 1/3, retake 1/2, then proof run (m1_b5_proof.py).
- Built: `clean_line(raw)` and `label_mark(mark)` in practice/m1_b5_functions.py.
- Missed: edit vs return (list changed in place, result is None), define before call.
- Ship notes:
  - Cost: no cost per user, plain Python.
  - Scale: nothing breaks at 10x, these functions are tiny.
  - Maintain: the 5 and 8 cut-offs are hard-coded, so changing the rule means editing the function.
  - Business: weak/ok/strong labels will drive which GATE topics Sarvantha tells a student to revise first.
- In my words: Don't call functions before defining them.

## M1 B6: Files, main guard, counting
- Quiz A 3/3, Quiz B 2/3 (missed the import and `__name__` question). Total 5/6.
- Built: projects/syllabus-cli, a uv project that reads syllabus.txt, cleans each line and prints topics per chapter.
- Ship notes:
  - Cost: no cost per user, plain file reading.
  - Scale: reading the whole file into memory is fine for a syllabus, but a huge file would need line-by-line reading.
  - Maintain: the file name and the "1.2 Title" line format are hard-coded, so a different syllabus layout breaks the chapter split.
  - Business: topics per chapter is the base for Sarvantha's study plan, because a student needs to see how much work each chapter holds.
- In my words: