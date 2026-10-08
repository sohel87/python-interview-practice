"""Tests for practice.py and solutions.py. You shouldn't need to edit this file.

Run from the same folder:
    python3 practice.py            # every exercise
    python3 practice.py heap       # only exercises whose section or name contains "heap"
"""

import sys
import traceback

CHECKS = []  # (section, name, check_function)


def check(section, name):
    def register(fn):
        CHECKS.append((section, name, fn))
        return fn
    return register


# ---------------------------------------------------------------- 1. numbers

@check("numbers", "digit_sum")
def _(m):
    assert m.digit_sum(0) == 0
    assert m.digit_sum(7) == 7
    assert m.digit_sum(9045) == 18
    assert m.digit_sum(10**30) == 1


@check("numbers", "div_trunc")
def _(m):
    assert m.div_trunc(7, 2) == 3
    assert m.div_trunc(-7, 2) == -3
    assert m.div_trunc(7, -2) == -3
    assert m.div_trunc(-7, -2) == 3
    assert m.div_trunc(6, 3) == 2


@check("numbers", "ceil_div")
def _(m):
    assert m.ceil_div(7, 2) == 4
    assert m.ceil_div(8, 2) == 4
    assert m.ceil_div(1, 5) == 1
    assert m.ceil_div(0, 5) == 0
    assert m.ceil_div(10**18 + 1, 10**9) == 10**9 + 1


# ---------------------------------------------------------------- 2. lists

@check("lists", "make_grid")
def _(m):
    g = m.make_grid(3, 2, 0)
    assert g == [[0, 0], [0, 0], [0, 0]]
    g[0][0] = 9
    assert g == [[9, 0], [0, 0], [0, 0]], "rows must be independent lists"
    assert m.make_grid(0, 5, ".") == []


@check("lists", "rotate_right")
def _(m):
    nums = [1, 2, 3, 4, 5]
    assert m.rotate_right(nums, 2) == [4, 5, 1, 2, 3]
    assert nums == [1, 2, 3, 4, 5], "don't modify the input"
    assert m.rotate_right(nums, 7) == [4, 5, 1, 2, 3]
    assert m.rotate_right(nums, 0) == [1, 2, 3, 4, 5]
    assert m.rotate_right([], 3) == []


@check("lists", "transpose")
def _(m):
    assert m.transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
    assert m.transpose([[1]]) == [[1]]


# ---------------------------------------------------------------- 3. strings

@check("strings", "is_palindrome")
def _(m):
    assert m.is_palindrome("A man, a plan, a canal: Panama")
    assert not m.is_palindrome("race a car")
    assert m.is_palindrome(" ")
    assert not m.is_palindrome("0P")


@check("strings", "caesar_shift")
def _(m):
    assert m.caesar_shift("abc", 1) == "bcd"
    assert m.caesar_shift("xyz", 3) == "abc"
    assert m.caesar_shift("hello, world!", 13) == "uryyb, jbeyq!"
    assert m.caesar_shift("abc", -1) == "zab"
    assert m.caesar_shift("abc", 52) == "abc"


@check("strings", "reverse_words")
def _(m):
    assert m.reverse_words("the sky is blue") == "blue is sky the"
    assert m.reverse_words("  hello   world  ") == "world hello"
    assert m.reverse_words("a") == "a"


# ---------------------------------------------------------------- 4. tuples and sets

@check("sets", "group_anagrams")
def _(m):
    got = m.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    norm = sorted(sorted(g) for g in got)
    assert norm == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
    assert m.group_anagrams([]) == []


@check("sets", "has_duplicate")
def _(m):
    assert m.has_duplicate([1, 2, 3, 1])
    assert not m.has_duplicate([1, 2, 3, 4])
    assert not m.has_duplicate([])


@check("sets", "common_to_all")
def _(m):
    assert m.common_to_all([[1, 2, 3, 4], [2, 4, 6], [4, 2, 2, 9]]) == [2, 4]
    assert m.common_to_all([[1], [2]]) == []
    assert m.common_to_all([[3, 1, 3]]) == [1, 3]


# ---------------------------------------------------------------- 5. dictionaries

@check("dicts", "two_sum")
def _(m):
    assert m.two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert m.two_sum([3, 2, 4], 6) == [1, 2]
    assert m.two_sum([3, 3], 6) == [0, 1]


@check("dicts", "most_frequent_word")
def _(m):
    assert m.most_frequent_word("the cat and the hat") == "the"
    assert m.most_frequent_word("b a c a b") == "a", "ties go to the alphabetically first word"
    assert m.most_frequent_word("Dog dog DOG cat") == "dog"


@check("dicts", "invert_dict")
def _(m):
    assert m.invert_dict({"a": 1, "b": 2, "c": 1}) == {1: ["a", "c"], 2: ["b"]}
    assert m.invert_dict({}) == {}


# ---------------------------------------------------------------- 6. collections

@check("collections", "top_k_frequent")
def _(m):
    assert m.top_k_frequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert m.top_k_frequent([4, 4, 5, 5, 6], 2) == [4, 5], "ties: smaller value first"
    assert m.top_k_frequent([7], 1) == [7]


@check("collections", "can_construct")
def _(m):
    assert not m.can_construct("a", "b")
    assert not m.can_construct("aa", "ab")
    assert m.can_construct("aa", "aab")
    assert m.can_construct("", "xyz")


@check("collections", "shortest_path_grid")
def _(m):
    assert m.shortest_path_grid([[0, 1], [0, 0]]) == 2
    assert m.shortest_path_grid([[0, 0, 0], [1, 1, 0], [0, 0, 0]]) == 4
    assert m.shortest_path_grid([[0, 1], [1, 0]]) == -1
    assert m.shortest_path_grid([[0]]) == 0
    assert m.shortest_path_grid([[1, 0], [0, 0]]) == -1


@check("collections", "window_max")
def _(m):
    assert m.window_max([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert m.window_max([1], 1) == [1]
    assert m.window_max([9, 8, 7, 6], 2) == [9, 8, 7]
    big = list(range(100_000))
    assert m.window_max(big, 50_000)[-1] == 99_999


@check("collections", "LRUCache")
def _(m):
    c = m.LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    assert c.get(1) == 1
    c.put(3, 3)            # evicts 2 (1 was used more recently)
    assert c.get(2) == -1
    c.put(4, 4)            # evicts 1
    assert c.get(1) == -1
    assert c.get(3) == 3
    assert c.get(4) == 4
    c.put(3, 30)           # update moves 3 to most recent
    c.put(5, 5)            # evicts 4
    assert c.get(4) == -1
    assert c.get(3) == 30


# ---------------------------------------------------------------- 7. heapq

@check("heap", "kth_largest")
def _(m):
    assert m.kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
    assert m.kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert m.kth_largest([1], 1) == 1


@check("heap", "merge_sorted_lists")
def _(m):
    assert m.merge_sorted_lists([[1, 4, 5], [1, 3, 4], [2, 6]]) == [1, 1, 2, 3, 4, 4, 5, 6]
    assert m.merge_sorted_lists([]) == []
    assert m.merge_sorted_lists([[], [0]]) == [0]


@check("heap", "k_closest")
def _(m):
    assert m.k_closest([[1, 3], [-2, 2]], 1) == [[-2, 2]]
    assert sorted(m.k_closest([[3, 3], [5, -1], [-2, 4]], 2)) == [[-2, 4], [3, 3]]


# ---------------------------------------------------------------- 8. bisect

@check("bisect", "count_in_range")
def _(m):
    a = [1, 2, 2, 3, 5, 8, 8, 8, 13]
    assert m.count_in_range(a, 2, 8) == 7
    assert m.count_in_range(a, 4, 4) == 0
    assert m.count_in_range(a, 0, 100) == 9
    assert m.count_in_range([], 1, 2) == 0


@check("bisect", "search_insert")
def _(m):
    assert m.search_insert([1, 3, 5, 6], 5) == 2
    assert m.search_insert([1, 3, 5, 6], 2) == 1
    assert m.search_insert([1, 3, 5, 6], 7) == 4
    assert m.search_insert([1, 3, 5, 6], 0) == 0


@check("bisect", "first_true")
def _(m):
    assert m.first_true(10, lambda i: i >= 7) == 7
    assert m.first_true(10, lambda i: True) == 0
    assert m.first_true(10, lambda i: False) == 10
    calls = []
    def cond(i):
        calls.append(i)
        return i >= 123_456
    assert m.first_true(10**9, cond) == 123_456
    assert len(calls) < 40, "should be O(log n) calls, not a linear scan"


# ---------------------------------------------------------------- 9. sorting

@check("sorting", "sort_by_frequency")
def _(m):
    assert m.sort_by_frequency([1, 1, 2, 2, 2, 3]) == [3, 1, 1, 2, 2, 2]
    assert m.sort_by_frequency([2, 3, 1, 3, 2]) == [1, 3, 3, 2, 2]
    assert m.sort_by_frequency([-1, 1, -6, 4, 5, -6, 1, 4, 1]) == [5, -1, 4, 4, -6, -6, 1, 1, 1]


@check("sorting", "largest_number")
def _(m):
    assert m.largest_number([10, 2]) == "210"
    assert m.largest_number([3, 30, 34, 5, 9]) == "9534330"
    assert m.largest_number([0, 0]) == "0"


@check("sorting", "merge_intervals")
def _(m):
    assert m.merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert m.merge_intervals([[1, 4], [4, 5]]) == [[1, 5]]
    assert m.merge_intervals([[4, 7], [1, 4]]) == [[1, 7]]
    assert m.merge_intervals([[1, 10], [2, 3]]) == [[1, 10]]


# ---------------------------------------------------------------- 10. functions and recursion

@check("functions", "make_counter")
def _(m):
    a = m.make_counter()
    b = m.make_counter()
    assert a() == 1
    assert a() == 2
    assert b() == 1, "each counter keeps its own state"
    assert a() == 3


@check("functions", "count_islands")
def _(m):
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    snapshot = [row[:] for row in grid]
    assert m.count_islands(grid) == 3
    assert grid == snapshot, "don't modify the input grid"
    assert m.count_islands([["0"]]) == 0
    assert m.count_islands([["1", "0", "1"]]) == 2


@check("functions", "climb_stairs")
def _(m):
    assert m.climb_stairs(1) == 1
    assert m.climb_stairs(2) == 2
    assert m.climb_stairs(5) == 8
    assert m.climb_stairs(90) == 4660046610375530309


# ---------------------------------------------------------------- 11. classes

@check("classes", "reverse_list")
def _(m):
    def build(vals):
        dummy = m.ListNode()
        tail = dummy
        for v in vals:
            tail.next = m.ListNode(v)
            tail = tail.next
        return dummy.next

    def to_list(node):
        out = []
        while node:
            out.append(node.val)
            node = node.next
        return out

    assert to_list(m.reverse_list(build([1, 2, 3, 4]))) == [4, 3, 2, 1]
    assert to_list(m.reverse_list(build([0]))) == [0]
    assert m.reverse_list(None) is None


@check("classes", "MinStack")
def _(m):
    s = m.MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    assert s.getMin() == -3
    s.pop()
    assert s.top() == 0
    assert s.getMin() == -2
    s.push(-2)
    s.pop()
    assert s.getMin() == -2, "duplicates of the minimum must be handled"


# ---------------------------------------------------------------- 12. itertools and math

@check("itertools", "run_lengths")
def _(m):
    assert m.run_lengths("aaabccdddd") == [("a", 3), ("b", 1), ("c", 2), ("d", 4)]
    assert m.run_lengths("") == []
    assert m.run_lengths("abab") == [("a", 1), ("b", 1), ("a", 1), ("b", 1)]


@check("itertools", "range_sums")
def _(m):
    nums = [3, -1, 4, 1, 5]
    assert m.range_sums(nums, [(0, 4), (1, 3), (2, 2)]) == [12, 4, 4]
    assert m.range_sums([], []) == []


@check("itertools", "gcd_of_list")
def _(m):
    assert m.gcd_of_list([12, 18, 24]) == 6
    assert m.gcd_of_list([7]) == 7
    assert m.gcd_of_list([5, 10, 3]) == 1


# ---------------------------------------------------------------- runner

def run(module, argv=None):
    argv = sys.argv[1:] if argv is None else argv
    flt = argv[0].lower() if argv else ""
    passed = failed = todo = 0
    section = None
    for sec, name, fn in CHECKS:
        if flt and flt not in sec.lower() and flt not in name.lower():
            continue
        if sec != section:
            print(f"\n[{sec}]")
            section = sec
        if not hasattr(module, name):
            print(f"  ?  {name}: not defined")
            failed += 1
            continue
        try:
            fn(module)
        except NotImplementedError:
            print(f"  .  {name}: todo")
            todo += 1
        except AssertionError as e:
            frame = traceback.extract_tb(e.__traceback__)[-1]
            detail = f" ({e})" if str(e) else ""
            print(f"  x  {name}: failed at checks.py line {frame.lineno}: {frame.line}{detail}")
            failed += 1
        except Exception as e:  # noqa: BLE001 - report any crash in the learner's code
            frame = traceback.extract_tb(e.__traceback__)[-1]
            print(f"  !  {name}: {type(e).__name__}: {e} (line {frame.lineno})")
            failed += 1
        else:
            print(f"  ok {name}")
            passed += 1
    total = passed + failed + todo
    print(f"\n{passed}/{total} passing, {failed} failing, {todo} todo")
    return failed == 0 and todo == 0
