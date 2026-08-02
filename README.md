# 🐍 Python Learning Journal
![Status](https://img.shields.io/badge/status-actively%20learning-brightgreen)
![Language](https://img.shields.io/badge/language-Python-blue)
![Progress](https://img.shields.io/badge/type-learning%20journal-yellow)

> 🚧 **This is a learning journal, not a finished project.** Each folder was added on the day I actually learned that topic. Once my foundational learning is complete, I'll move on to building real, standalone projects — this repo exists to document the process honestly, step by step.

## 📌 About
I'm learning Python with the goal of eventually moving into AI/data-focused work. This repository holds my notes and hands-on exercises, organized by topic in the order I learned them. Every commit corresponds to a specific topic learned on that day — check the [commit history](../../commits/main) to see the full timeline.

## 📚 Contents
| # | Topic | What's Inside |
|---|---|---|
| 01 | [Variables & Data Types](01-variables-data-types) | int, float, str, list, dict, set, range |
| 02 | [String Basics](02-string-basics) | Indexing, slicing, concatenation, escape characters |
| 03 | [String Methods](03-string-methods) | upper/lower, strip, replace, split, title, f-strings |
| 04 | [Operators](04-operators) | Arithmetic, comparison, logical (`and`/`or`/`not`), identity (`is`) |
| 05 | [Conditional Statements](05-conditional-statements) | if / elif / else, short-hand if |
| 06 | [Lists](06-lists) | Access, slicing, append/insert/remove/pop/sort... |
| 07 | [While Loops](07-while-loops) | break, continue, while-else |
| 08 | [For Loops](08-for-loops) | range(), tuples, strings, for-else |
| 09 | [Nested Loops, enumerate() & zip()](09-nested-loops-enumerate-zip) | Nested iteration, paired iteration |
| 10 | [List Comprehension](10-list-comprehension) | Writing loops in a single line |
| 11 | [Random Module](11-random-module) | randint, choice, shuffle, sample |
| 12 | [Mini Projects](12-mini-projects) | Circle area, factorial, number guessing game, sorter |
| 13 | [Dictionaries](13-dictionaries) | Access, update, delete, reference vs. copy |
| 14 | [Functions](14-functions) | Parameters, return, defaults, *args, **kwargs |
| 15 | [Math Module](15-math-module) | Rounding, roots, logs, trig, factorial, GCD, distance |
| 16 | [Statistics Module](16-statistics-module) | Mean, median, mode, variance, stdev, quantiles |
| 17 | [Datetime Module](17-datetime-module) | Formatting, parsing, date arithmetic, age calculation |
| 18 | [Time Module](18-time-module) | Timestamps, measuring execution time, delays |

## ▶️ How to Run
```bash
python 01-variables-data-types/notes.py
```
Files inside `12-mini-projects` expect user input, so run them in a terminal rather than by pasting into an interpreter.

## 💡 Key Takeaways
- **Methods that mutate in place** (`append`, `remove`, `sort`, `update`...) return `None` — no need to wrap them in `print()`.
- **Methods that return a value** (`pop`, `index`, `count`, `copy`, `get`...) can be printed or stored in a variable.
- **Assigning a mutable object** (`list`, `dict`, `set`) with `=` does not copy it — it shares a reference. Use `.copy()` for an independent copy.

## 🎯 What's Next
- NumPy & Pandas
- Object-Oriented Programming (classes, inheritance)
- Building small end-to-end projects

---
📎 Also see: [SQL Learning Journal](https://github.com/busesrkya/sql-learning-journal) — the same journal-style approach applied to SQL.