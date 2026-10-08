"""Worked solutions. Open only after your own version passes, or after 20 minutes stuck.

Run:  python3 solutions.py
"""

import heapq
import math
from bisect import bisect_left, bisect_right
from collections import Counter, OrderedDict, defaultdict, deque
from functools import cache, cmp_to_key, reduce
from itertools import accumulate, groupby


# ---------------------------------------------------------------- 1. numbers

def digit_sum(n):
    total = 0
    while n:
        n, d = divmod(n, 10)
        total += d
    return total


def div_trunc(a, b):
    # int(a / b) also works here, but floats lose precision past 2**53.
    q = abs(a) // abs(b)
    return q if (a < 0) == (b < 0) else -q


def ceil_div(a, b):
    return -(-a // b)


# ---------------------------------------------------------------- 2. lists

def make_grid(rows, cols, fill):
    return [[fill] * cols for _ in range(rows)]


def rotate_right(nums, k):
    if not nums:
        return []
    k %= len(nums)
    return nums[-k:] + nums[:-k] if k else nums[:]


def transpose(matrix):
    return [list(col) for col in zip(*matrix)]


# ---------------------------------------------------------------- 3. strings

def is_palindrome(s):
    chars = [c.lower() for c in s if c.isalnum()]
    return chars == chars[::-1]
    # Interview follow-up: two pointers skipping non-alphanumerics, O(1) space.


def caesar_shift(s, k):
    out = []
    for c in s:
        if "a" <= c <= "z":
            out.append(chr((ord(c) - ord("a") + k) % 26 + ord("a")))
        else:
            out.append(c)
    return "".join(out)


def reverse_words(s):
    return " ".join(reversed(s.split()))


# ---------------------------------------------------------------- 4. tuples and sets

def group_anagrams(words):
    groups = defaultdict(list)
    for w in words:
        count_ = [0] * 26
        for c in w:
            count_[ord(c) - ord("a")] += 1
        groups[tuple(count_)].append(w)
    return list(groups.values())


def has_duplicate(nums):
    return len(set(nums)) != len(nums)


def common_to_all(lists):
    return sorted(set.intersection(*map(set, lists)))


# ---------------------------------------------------------------- 5. dictionaries

def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
    return []


def most_frequent_word(text):
    counts = {}
    for w in text.lower().split():
        counts[w] = counts.get(w, 0) + 1
    return min(counts, key=lambda w: (-counts[w], w))


def invert_dict(d):
    out = {}
    for k, v in d.items():
        out.setdefault(v, []).append(k)
    return {v: sorted(ks) for v, ks in out.items()}


# ---------------------------------------------------------------- 6. collections

def top_k_frequent(nums, k):
    counts = Counter(nums)
    return sorted(counts, key=lambda x: (-counts[x], x))[:k]
    # O(n) alternative: bucket sort by frequency.


def can_construct(ransom, magazine):
    return not (Counter(ransom) - Counter(magazine))


def shortest_path_grid(grid):
    rows, cols = len(grid), len(grid[0])
    if grid[0][0] or grid[rows - 1][cols - 1]:
        return -1
    q = deque([(0, 0, 0)])
    seen = {(0, 0)}
    while q:
        r, c, d = q.popleft()
        if (r, c) == (rows - 1, cols - 1):
            return d
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and not grid[nr][nc] and (nr, nc) not in seen:
                seen.add((nr, nc))
                q.append((nr, nc, d + 1))
    return -1


def window_max(nums, k):
    dq = deque()  # indices; their values are decreasing from front to back
    res = []
    for i, x in enumerate(nums):
        while dq and nums[dq[-1]] <= x:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:
            dq.popleft()
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = OrderedDict()

    def get(self, key):
        if key not in self.data:
            return -1
        self.data.move_to_end(key)
        return self.data[key]

    def put(self, key, value):
        self.data[key] = value
        self.data.move_to_end(key)
        if len(self.data) > self.capacity:
            self.data.popitem(last=False)


# ---------------------------------------------------------------- 7. heapq

def kth_largest(nums, k):
    h = []
    for x in nums:
        heapq.heappush(h, x)
        if len(h) > k:
            heapq.heappop(h)
    return h[0]


def merge_sorted_lists(lists):
    h = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(h)
    out = []
    while h:
        val, i, j = heapq.heappop(h)
        out.append(val)
        if j + 1 < len(lists[i]):
            heapq.heappush(h, (lists[i][j + 1], i, j + 1))
    return out


def k_closest(points, k):
    return heapq.nsmallest(k, points, key=lambda p: p[0] ** 2 + p[1] ** 2)


# ---------------------------------------------------------------- 8. bisect

def count_in_range(nums, lo, hi):
    return bisect_right(nums, hi) - bisect_left(nums, lo)


def search_insert(nums, target):
    return bisect_left(nums, target)


def first_true(n, cond):
    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi) // 2
        if cond(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


# ---------------------------------------------------------------- 9. sorting

def sort_by_frequency(nums):
    counts = Counter(nums)
    return sorted(nums, key=lambda x: (counts[x], -x))


def largest_number(nums):
    strs = list(map(str, nums))

    def cmp(a, b):
        if a + b > b + a:
            return -1
        if a + b < b + a:
            return 1
        return 0

    strs.sort(key=cmp_to_key(cmp))
    result = "".join(strs)
    return "0" if result[0] == "0" else result


def merge_intervals(intervals):
    merged = []
    for start, end in sorted(intervals, key=lambda iv: iv[0]):
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


# ---------------------------------------------------------------- 10. functions and recursion

def make_counter():
    n = 0

    def counter():
        nonlocal n
        n += 1
        return n

    return counter


def count_islands(grid):
    rows, cols = len(grid), len(grid[0])
    seen = set()

    def dfs(r, c):
        if not (0 <= r < rows and 0 <= c < cols):
            return
        if grid[r][c] != "1" or (r, c) in seen:
            return
        seen.add((r, c))
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            dfs(r + dr, c + dc)

    islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in seen:
                dfs(r, c)
                islands += 1
    return islands


def climb_stairs(n):
    @cache
    def ways(i):
        if i <= 2:
            return i
        return ways(i - 1) + ways(i - 2)

    return ways(n)
    # Bottom-up O(1) space: a, b = b, a + b in a loop.


# ---------------------------------------------------------------- 11. classes

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    prev = None
    while head:
        head.next, prev, head = prev, head, head.next
    return prev
    # Clearer in an interview:
    #   nxt = head.next; head.next = prev; prev = head; head = nxt


class MinStack:
    def __init__(self):
        self.stack = []  # (value, minimum so far)

    def push(self, val):
        low = min(val, self.stack[-1][1]) if self.stack else val
        self.stack.append((val, low))

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]


# ---------------------------------------------------------------- 12. itertools and math

def run_lengths(s):
    return [(ch, len(list(group))) for ch, group in groupby(s)]


def range_sums(nums, queries):
    pre = list(accumulate(nums, initial=0))
    return [pre[j + 1] - pre[i] for i, j in queries]


def gcd_of_list(nums):
    return reduce(math.gcd, nums)


if __name__ == "__main__":
    import sys
    import checks
    sys.exit(0 if checks.run(sys.modules[__name__]) else 1)
