"""Python for coding interviews: 37 exercises.

Replace each `raise NotImplementedError` with your solution, then run:
    python3 practice.py            # all exercises
    python3 practice.py heap       # one section, or any part of an exercise name

Each docstring names the tool to practise. Aim for the idiomatic version first,
then say its time and space complexity out loud before moving on.
"""

# Add imports as you need them, as you would in an interview.


# ================================================================ 1. numbers

def digit_sum(n):
    """Sum of the decimal digits of a non-negative integer n.
    digit_sum(9045) -> 18.   Tool: divmod.
    """
    raise NotImplementedError


def div_trunc(a, b):
    """Integer division that truncates towards zero, like C or Java.
    div_trunc(-7, 2) -> -3 (whereas -7 // 2 == -4).   Tool: //, abs, signs.
    Bonus: make it exact for very large ints (no floats).
    """
    raise NotImplementedError


def ceil_div(a, b):
    """Ceiling of a / b for a >= 0, b > 0, without floats or math.ceil.
    ceil_div(7, 2) -> 4.   Tool: // with negation.
    """
    raise NotImplementedError


# ================================================================ 2. lists

def make_grid(rows, cols, fill):
    """A rows x cols grid where every row is an independent list.
    Tool: list comprehension (and why [[fill] * cols] * rows is wrong).
    """
    raise NotImplementedError


def rotate_right(nums, k):
    """Return a NEW list rotated right by k (k may exceed len(nums)).
    rotate_right([1,2,3,4,5], 2) -> [4,5,1,2,3].   Tool: slicing, %.
    """
    raise NotImplementedError


def transpose(matrix):
    """Rows become columns. [[1,2,3],[4,5,6]] -> [[1,4],[2,5],[3,6]].
    Return a list of lists.   Tool: zip(*matrix).
    """
    raise NotImplementedError


# ================================================================ 3. strings

def is_palindrome(s):
    """True if s reads the same forwards and backwards, ignoring case and
    non-alphanumeric characters.   Tool: str.isalnum, str.lower, slicing.
    Follow-up: do it with two pointers and O(1) extra space.
    """
    raise NotImplementedError


def caesar_shift(s, k):
    """Shift each lowercase letter k places, wrapping round; leave everything
    else unchanged. k may be negative or larger than 26.
    caesar_shift("xyz", 3) -> "abc".   Tool: ord, chr, %, "".join.
    """
    raise NotImplementedError


def reverse_words(s):
    """Reverse word order; collapse runs of spaces; no leading/trailing spaces.
    "  hello   world  " -> "world hello".   Tool: str.split(), " ".join.
    """
    raise NotImplementedError


# ================================================================ 4. tuples and sets

def group_anagrams(words):
    """Group words that are anagrams (lowercase a-z only). Any group order.
    Tool: defaultdict(list) keyed by tuple(26 counts). Avoid sorting each word.
    """
    raise NotImplementedError


def has_duplicate(nums):
    """True if any value appears at least twice.   Tool: set."""
    raise NotImplementedError


def common_to_all(lists):
    """Sorted list of values that appear in every list (no duplicates).
    Tool: set intersection (set.intersection(*...) or &).
    """
    raise NotImplementedError


# ================================================================ 5. dictionaries

def two_sum(nums, target):
    """Indices [i, j] with i < j and nums[i] + nums[j] == target, in one pass.
    Exactly one answer exists.   Tool: dict of value -> index, enumerate.
    """
    raise NotImplementedError


def most_frequent_word(text):
    """Most frequent word, case-insensitive; ties go to the alphabetically
    first word.   Tool: dict.get counting, min/max with a tuple key.
    Do it without Counter here.
    """
    raise NotImplementedError


def invert_dict(d):
    """Map each value to a SORTED list of the keys that had it.
    {"a": 1, "b": 2, "c": 1} -> {1: ["a", "c"], 2: ["b"]}.   Tool: setdefault.
    """
    raise NotImplementedError


# ================================================================ 6. collections

def top_k_frequent(nums, k):
    """The k most frequent values, most frequent first; ties: smaller value first.
    Tool: Counter, sorted with a tuple key.
    Follow-up: O(n) with bucket sort.
    """
    raise NotImplementedError


def can_construct(ransom, magazine):
    """True if ransom can be built from magazine's letters (each used once).
    Tool: Counter subtraction.
    """
    raise NotImplementedError


def shortest_path_grid(grid):
    """Fewest 4-directional steps from top-left to bottom-right through 0 cells
    (1 = wall). Return -1 if impossible. A 1x1 [[0]] grid is 0 steps.
    Tool: deque BFS, a seen set of (r, c) tuples.
    """
    raise NotImplementedError


def window_max(nums, k):
    """Maximum of every contiguous window of size k, in O(n).
    window_max([1,3,-1,-3,5,3,6,7], 3) -> [3,3,5,5,6,7].
    Tool: deque of indices kept in decreasing value order (monotonic deque).
    """
    raise NotImplementedError


class LRUCache:
    """Least-recently-used cache. get returns -1 for a missing key. put inserts
    or updates; when over capacity, evict the least recently used key.
    Both operations O(1).   Tool: OrderedDict (move_to_end, popitem(last=False)).
    Follow-up: rebuild it with a dict + doubly linked list.
    """

    def __init__(self, capacity):
        raise NotImplementedError

    def get(self, key):
        raise NotImplementedError

    def put(self, key, value):
        raise NotImplementedError


# ================================================================ 7. heapq

def kth_largest(nums, k):
    """The kth largest element (not kth distinct), in O(n log k).
    Tool: a min-heap capped at size k.
    """
    raise NotImplementedError


def merge_sorted_lists(lists):
    """Merge k sorted Python lists into one sorted list in O(N log k).
    Tool: heap of (value, list_index, element_index) tuples.
    Don't just concatenate and sort.
    """
    raise NotImplementedError


def k_closest(points, k):
    """The k points closest to the origin, as a list of [x, y]. Any order.
    Tool: heapq.nsmallest with key=, or a max-heap of size k via negation.
    """
    raise NotImplementedError


# ================================================================ 8. bisect

def count_in_range(nums, lo, hi):
    """How many values in sorted nums satisfy lo <= x <= hi, in O(log n).
    Tool: bisect_left and bisect_right.
    """
    raise NotImplementedError


def search_insert(nums, target):
    """Index of target in sorted distinct nums, or where it would be inserted.
    Tool: bisect. Then write it again by hand.
    """
    raise NotImplementedError


def first_true(n, cond):
    """cond(i) is False for i < answer and True from answer onwards, for i in
    range(n). Return the answer, or n if cond is never True. O(log n) calls.
    Tool: the hand-written lo/hi template from the reference doc.
    """
    raise NotImplementedError


# ================================================================ 9. sorting

def sort_by_frequency(nums):
    """Sort by frequency ascending; equal frequencies by value DESCENDING.
    [2,3,1,3,2] -> [1,3,3,2,2].   Tool: Counter + sorted with a tuple key.
    """
    raise NotImplementedError


def largest_number(nums):
    """Arrange non-negative ints to form the largest number, as a string.
    [3,30,34,5,9] -> "9534330"; [0,0] -> "0".   Tool: functools.cmp_to_key.
    """
    raise NotImplementedError


def merge_intervals(intervals):
    """Merge overlapping [start, end] intervals (touching ones merge too).
    Return them sorted by start.   Tool: sort with key, a result list as a stack.
    """
    raise NotImplementedError


# ================================================================ 10. functions and recursion

def make_counter():
    """Return a function that returns 1, 2, 3, ... on successive calls.
    Each counter keeps its own state.   Tool: closure + nonlocal.
    """
    raise NotImplementedError


def count_islands(grid):
    """Count groups of 4-directionally connected "1" cells in a grid of "0"/"1"
    strings. Don't modify the input.   Tool: nested dfs function, seen set.
    """
    raise NotImplementedError


def climb_stairs(n):
    """Ways to climb n steps taking 1 or 2 at a time. Must handle n = 90 fast.
    Tool: @functools.cache on a nested function.
    Follow-up: bottom-up with O(1) space.
    """
    raise NotImplementedError


# ================================================================ 11. classes

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    """Reverse a singly linked list iteratively; return the new head.
    Tool: three pointers (prev, curr, next). Handle head = None.
    """
    raise NotImplementedError


class MinStack:
    """Stack with push, pop, top and getMin, all O(1).
    Tool: store (value, current minimum) tuples.
    """

    def __init__(self):
        raise NotImplementedError

    def push(self, val):
        raise NotImplementedError

    def pop(self):
        raise NotImplementedError

    def top(self):
        raise NotImplementedError

    def getMin(self):
        raise NotImplementedError


# ================================================================ 12. itertools and math

def run_lengths(s):
    """Run-length encode as (char, count) tuples.
    "aaabcc" -> [("a", 3), ("b", 1), ("c", 2)].   Tool: itertools.groupby.
    """
    raise NotImplementedError


def range_sums(nums, queries):
    """For each (i, j) query, return sum(nums[i..j]) inclusive, each in O(1)
    after an O(n) setup.   Tool: itertools.accumulate(nums, initial=0).
    """
    raise NotImplementedError


def gcd_of_list(nums):
    """Greatest common divisor of a non-empty list.
    Tool: math.gcd with functools.reduce.
    """
    raise NotImplementedError


if __name__ == "__main__":
    import sys
    import checks
    checks.run(sys.modules[__name__])
