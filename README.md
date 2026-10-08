# Python interview practice

37 short exercises for building fluency with the Python standard library in coding interviews: `collections`, `heapq`, `bisect`, `functools`, `itertools`, plus the built-in idioms. Each exercise targets one tool.

## Files

| File | What it is |
| --- | --- |
| `practice.py` | Exercise stubs. Replace each `raise NotImplementedError` with your solution. |
| `checks.py` | Tests and the runner. No need to edit. |
| `solutions.py` | Worked solutions. Open only after your version passes, or after 20 minutes stuck. |

## Running

Requires Python 3.10 or later.

```bash
python3 practice.py          # all exercises
python3 practice.py heap     # one section, or any part of an exercise name
python3 solutions.py         # check the reference solutions (all should pass)
```

Each exercise reports `ok`, `x` (wrong answer, with the failing check), `!` (crash) or `.` (not started).

## Sections

1. Numbers: `digit_sum`, `div_trunc`, `ceil_div`
2. Lists: `make_grid`, `rotate_right`, `transpose`
3. Strings: `is_palindrome`, `caesar_shift`, `reverse_words`
4. Tuples and sets: `group_anagrams`, `has_duplicate`, `common_to_all`
5. Dictionaries: `two_sum`, `most_frequent_word`, `invert_dict`
6. collections: `top_k_frequent`, `can_construct`, `shortest_path_grid`, `window_max`, `LRUCache`
7. heapq: `kth_largest`, `merge_sorted_lists`, `k_closest`
8. bisect: `count_in_range`, `search_insert`, `first_true`
9. Sorting: `sort_by_frequency`, `largest_number`, `merge_intervals`
10. Functions and recursion: `make_counter`, `count_islands`, `climb_stairs`
11. Classes: `reverse_list`, `MinStack`
12. itertools and math: `run_lengths`, `range_sums`, `gcd_of_list`

## How to use it

After each exercise, state the time and space complexity out loud, then compare with `solutions.py`. If an idiom there is new to you, add one line to your own cheat sheet.
