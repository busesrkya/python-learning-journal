# Python Learning Journal

Notes and exercises from my Python learning journey, organized by topic.

## Contents

| Folder | Topic |
|---|---|
| `01-variables-data-types` | Variables, data types (int, float, str, list, dict, set, range) |
| `02-string-basics` | String indexing, slicing, concatenation, escape characters |
| `03-string-methods` | upper/lower, strip, replace, split, title, format(), f-string |
| `04-operators` | Arithmetic, comparison, logical (and/or/not), identity (is/is not) operators |
| `05-conditional-statements` | if / elif / else, short hand if |
| `06-lists` | List access, methods (append, insert, remove, pop, extend, sort...) |
| `07-while-loops` | while, break, continue, while-else |
| `08-for-loops` | for, range(), usage with tuples/strings, for-else |
| `09-nested-loops-enumerate-zip` | Nested loops, enumerate(), zip() |
| `10-list-comprehension` | Creating lists in a single line |
| `11-random-module` | random.randint, random.choice, shuffle, sample |
| `12-mini-projects` | Circle area calculator, factorial, number guessing game, number sorter |
| `13-dictionaries` | dict access/update/delete, reference vs copy (copy()) |
| `14-functions` | Function definition, parameters, default values, return, *args, **kwargs |

## How to Run

```bash
python 01-variables-data-types/notes.py
```

Files inside `12-mini-projects` ask for user input (`input()`), so they should be run in a terminal.

## Key Takeaways

- **Methods that mutate in place (append, remove, sort, update, etc.):** modify the list/dict directly and return `None` — no need to wrap them in `print()`.
- **Methods that return a value (pop, index, count, copy, get, etc.):** return a value that can be printed or stored in a variable.
- **Assignment (`=`) with mutable types (list, dict, set):** does not create a copy, it shares a reference to the same object. Use `.copy()` for an independent copy.
