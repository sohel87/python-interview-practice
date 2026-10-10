# Python for Coding Interviews: Reference and Practice

## How to use this

Read a section when a problem needs it, not front to back. Each section ends with the mistake interviewers notice most.

- **Practice files:** `practice.py` holds 37 exercise stubs in the same order as this doc. Run `python3 practice.py` to see which pass; `python3 practice.py heap` runs only exercises whose name contains "heap". `checks.py` holds the tests; `solutions.py` holds worked answers.
- **Rule for the solutions file:** open it only after your version passes, or after 20 minutes stuck. Then close it and rewrite the solution from memory.
- **Python version:** everything here runs on Python 3.10 or later, which covers LeetCode, CoderPad and HackerRank today.
- **Cheat sheet:** when an exercise catches you out, add one line to your own sheet. Don't copy this doc into it.

## Numbers and maths

Python integers never overflow, and `//` floors towards negative infinity rather than towards zero. Both differ from JavaScript and Java.

```
7 // 2            # 3
-7 // 2           # -4   floors towards -infinity
int(-7 / 2)       # -3   truncates towards zero (C, Java, JS behaviour)
-7 % 3            # 2    result takes the sign of the divisor
q, r = divmod(17, 5)          # (3, 2)

2 ** 10                       # 1024
pow(2, 10, 1_000_000_007)     # modular power, fast
MOD = 10**9 + 7

float("inf"), float("-inf")   # sentinels for min/max tracking
10**20 + 1                    # fine: ints are arbitrary precision
round(2.5)                    # 2  (rounds half to even)

# Peel digits off a number
while n:
    n, d = divmod(n, 10)

# Ceiling division for positive ints, no floats
(a + b - 1) // b
-(-a // b)
```

**Gotcha:** "Evaluate Reverse Polish Notation" expects division that truncates towards zero, so use `int(a / b)`, not `a // b`. Problems like "Reverse Integer" ask you to emulate 32-bit overflow, so check `-2**31 <= x <= 2**31 - 1` yourself.

## Lists

A list is a dynamic array: cheap at the end, expensive at the front. It doubles as your stack.

```
nums = [0] * n
grid = [[0] * cols for _ in range(rows)]   # each row is a separate list

# Stack
stack = []
stack.append(x)
top = stack[-1]          # peek
stack.pop()              # O(1)
if stack: ...            # empty check

# Indexing and slicing (slices copy: O(k))
nums[-1], nums[i:j], nums[::-1], nums[::2]
copy = nums[:]           # or list(nums)

# Sorting
nums.sort()                          # in place, returns None
nums.sort(key=abs, reverse=True)
new = sorted(nums)                   # new list

# Front operations are O(n): use collections.deque instead
nums.insert(0, x)
nums.pop(0)

x in nums               # O(n)
nums.index(x)           # O(n), ValueError if missing
nums.extend(other)      # in place; nums + other builds a new list

# Comprehensions
squares = [x * x for x in nums if x > 0]
flat = [x for row in grid for x in row]
cols_ = list(zip(*grid))             # transpose (tuples)

# Iterating backwards
for i in range(len(nums) - 1, -1, -1): ...
for x in reversed(nums): ...
```

**Gotchas:**

- `[[0] * cols] * rows` makes every row the same list. Changing one cell changes the whole column.
- `x = nums.sort()` sets `x` to `None`.
- Passing `nums[1:]` into a recursive call copies the list each time, turning O(n) into O(n²). Pass indices instead.

## Strings

Strings are immutable. Build a list of pieces and `join` once at the end.

```
s[0], s[-1], s[1:3], s[::-1]
s[0] = "H"                   # TypeError: immutable

parts = []
for ch in s:
    parts.append(ch.upper())
result = "".join(parts)      # O(n) total

s.split()                    # splits on any whitespace, drops empties
s.split(",")                 # keeps empty strings between commas
" ".join(words)
s.strip(), s.lower(), s.upper()
ch.isalnum(), ch.isalpha(), ch.isdigit(), ch.isspace()

ord("a"), chr(97)            # 97, "a"
idx = ord(ch) - ord("a")      # 0..25, for 26-slot count arrays

s.find("lo")                 # index or -1
s.index("lo")                # index or ValueError
s.count("l"), s.startswith("he"), s.replace("l", "L")

"".join(sorted(s))           # sorted() returns a list of chars
list(s)                      # ["h", "e", ...]
int("42"), str(42), int("101", 2), bin(5)[2:]   # "101"

from string import ascii_lowercase, digits
```

**Gotcha:** `res += ch` inside a loop can be O(n²) in the worst case, and interviewers know it. For anagram keys, use `tuple(count)` of a 26-slot list (O(n)) or `"".join(sorted(s))` (O(n log n)), and be ready to say which you picked and why.

## Tuples

Tuples are immutable and hashable, so they work as dict keys and set members. They compare element by element, which is what makes heaps and multi-key sorts work.

```
p = (1, 2)
x, y = p
single = (5,)                # the comma makes it a tuple; (5) is just 5

seen = set()
seen.add((r, c))             # grid coordinates
dist = {}
dist[r, c] = 0               # parentheses optional inside []

(1, 2) < (1, 3) < (2, 0)     # True: compares first items, then the next

count = [0] * 26
key = tuple(count)           # list -> hashable key
```

**Gotcha:** lists can't be dict keys or set members (`TypeError: unhashable type: 'list'`). Convert with `tuple(...)` first.

## Sets

Use a set whenever the question is "have I seen this?". Membership is O(1) on average.

```
s = set()                    # {} is an empty DICT, not a set
s = {1, 2, 3}
s.add(x)
s.remove(x)                  # KeyError if missing
s.discard(x)                 # no error if missing
x in s

a | b, a & b, a - b, a ^ b   # union, intersection, difference, symmetric difference
a <= b                       # subset

len(set(nums)) != len(nums)  # contains a duplicate
frozenset(items)             # immutable, hashable set (usable as a dict key)
```

**Gotcha:** sets are unordered. If a test expects a list in a particular order, sort it before returning. Adding to or removing from a set while iterating over it raises `RuntimeError`.

## Dictionaries

The dict is the most-used structure in coding rounds: index maps, counts, groupings, memo tables. Lookup, insert and delete are O(1) on average, and iteration follows insertion order.

```
d = {}
d[k] = v
d.get(k)                     # None if missing
d.get(k, 0)                  # default if missing
d[k] = d.get(k, 0) + 1       # counting without imports
d.setdefault(k, []).append(v)   # grouping without imports

k in d                       # checks keys, O(1)
for k, v in d.items(): ...
for k in d: ...
d.keys(), d.values()

del d[k]                     # KeyError if missing
d.pop(k, None)               # safe removal

index = {v: i for i, v in enumerate(nums)}   # dict comprehension

max(d, key=d.get)            # key with the largest value
sorted(d.items(), key=lambda kv: kv[1], reverse=True)

# Two Sum shape: check before you insert
seen = {}
for i, x in enumerate(nums):
    if target - x in seen:
        return [seen[target - x], i]
    seen[x] = i
```

**Gotcha:** deleting keys while looping over the dict raises `RuntimeError: dictionary changed size during iteration`. Loop over `list(d)` instead.

## collections

`deque`, `defaultdict` and `Counter` appear in most rounds; `OrderedDict` is mainly for the LRU cache.

```
from collections import deque, defaultdict, Counter, OrderedDict
```

**deque: a queue with O(1) at both ends.** Use it for BFS and for sliding windows that drop from the front.

```
q = deque([start])
q.append(x)
q.popleft()                  # O(1); list.pop(0) is O(n)
q.appendleft(x)
q.pop()
q[0], q[-1]                  # peek either end, O(1)
window = deque(maxlen=k)     # oldest item drops off automatically

# BFS level by level
while q:
    for _ in range(len(q)):
        node = q.popleft()
        ...
```

**defaultdict: a dict that creates missing values.**

```
graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

count = defaultdict(int)
count[x] += 1

groups = defaultdict(list)
groups[key].append(word)
```

**Counter: a dict of counts.**

```
c = Counter("banana")        # Counter({'a': 3, 'n': 2, 'b': 1})
c["z"]                       # 0: no KeyError, and nothing inserted
c.most_common(2)             # [('a', 3), ('n', 2)]
Counter(s) == Counter(t)     # anagram check
c1 - c2                      # subtract, dropping zero and negative counts
c1 + c2
c.update("more")             # add counts from an iterable
c.total()                    # sum of counts (3.10+)
```

**OrderedDict: a dict that can move keys to either end.**

```
cache = OrderedDict()
cache[k] = v
cache.move_to_end(k)         # mark as most recently used
cache.popitem(last=False)    # evict the least recently used
```

**Gotchas:**

- Reading `graph[missing]` on a defaultdict inserts an empty list. Check with `if node in graph` when you don't want that.
- For LRU Cache, an interviewer may say "without OrderedDict". Be ready to build it from a dict plus a doubly linked list with dummy head and tail nodes.

## Heaps with heapq

`heapq` turns a plain list into a min-heap. Push and pop are O(log n), peeking is O(1), and `heapify` is O(n).

```
import heapq

h = []
heapq.heappush(h, x)
smallest = heapq.heappop(h)
h[0]                          # peek at the smallest, O(1)

heapq.heapify(nums)           # in place, O(n)
heapq.heappushpop(h, x)       # push, then pop the smallest (one sift)
heapq.heapreplace(h, x)       # pop the smallest, then push

heapq.nlargest(k, nums)
heapq.nsmallest(k, points, key=lambda p: p[0]**2 + p[1]**2)

# Max-heap: negate on the way in and out
heapq.heappush(h, -x)
largest = -heapq.heappop(h)

# Priority + payload: tuples compare left to right
heapq.heappush(h, (dist, node))

# Tiebreaker when payloads can't be compared (ListNode, dicts)
from itertools import count
tie = count()
heapq.heappush(h, (node.val, next(tie), node))

# Top k largest in O(n log k): keep a min-heap of size k
for x in nums:
    heapq.heappush(h, x)
    if len(h) > k:
        heapq.heappop(h)
kth_largest = h[0]
```

**Gotchas:**

- The list is heap-ordered, not sorted. `h[0]` is the minimum, but `h[1]` is not necessarily the second smallest.
- Two tuples with equal priorities compare their second items. If those are `ListNode` objects, you get `TypeError: '<' not supported`. Add the counter tiebreaker.
- Negation is the habit to build for max-heaps. Some newer Python versions add max-heap helpers, but interview platforms often run older versions.

## Binary search with bisect

`bisect` finds insertion points in a sorted list in O(log n). Use it for lookups; write the loop by hand when the condition isn't "compare with a value".

```
from bisect import bisect_left, bisect_right, insort

a = [1, 2, 2, 2, 5]
bisect_left(a, 2)             # 1: first index with a[i] >= 2
bisect_right(a, 2)            # 4: first index with a[i] > 2
bisect_right(a, 2) - bisect_left(a, 2)   # 3 copies of 2

i = bisect_left(a, x)
found = i < len(a) and a[i] == x

insort(a, 3)                  # insert keeping order: O(log n) search + O(n) shift
bisect_left(intervals, t, key=lambda iv: iv[0])   # key= needs 3.10+
```

**The one hand-written template to memorise.** Phrase the problem as "find the first index where `cond` becomes true", with `cond` false then true across the range.

```
lo, hi = 0, n                 # answer lies in [lo, hi]; hi = n means "none"
while lo < hi:
    mid = (lo + hi) // 2
    if cond(mid):
        hi = mid              # mid could be the answer
    else:
        lo = mid + 1          # mid is not the answer
return lo
```

The same loop solves "binary search on the answer" problems such as Koko Eating Bananas: search over speeds, with `cond(speed)` meaning "can finish in time".

**Gotcha:** most off-by-one bugs come from mixing `lo <= hi` with `hi = mid`. Pick this one template and use it everywhere.

## Sorting

Python's sort is O(n log n) and stable: equal items keep their original order. Almost every custom order is a `key` function returning a tuple.

```
sorted(words, key=len)
sorted(pairs, key=lambda p: (-p[1], p[0]))   # count descending, then name ascending
intervals.sort(key=lambda iv: iv[0])         # merge intervals starts here

from operator import itemgetter
rows.sort(key=itemgetter(1, 0))              # same as lambda r: (r[1], r[0])

# Descending on a string key: negation doesn't work, so use stability
rows.sort(key=lambda r: r[1])                # secondary key first
rows.sort(key=lambda r: r[0], reverse=True)  # primary key last

# Pairwise comparison when no key exists ("Largest Number")
from functools import cmp_to_key
def cmp(a, b):
    if a + b > b + a: return -1
    if a + b < b + a: return 1
    return 0
strs.sort(key=cmp_to_key(cmp))
```

**Beyond comparison sorts:** when values fall in a small range, bucket by count instead. "Top K Frequent Elements" in O(n) uses `buckets[freq].append(num)` and reads the buckets from the top.

**Gotcha:** a `cmp` function must return negative, zero or positive, not `True`/`False`.

## Functions, closures and recursion

Interview solutions usually put a helper (`dfs`, `backtrack`, `dp`) inside the main function so it can see the inputs without passing them around.

```
def num_islands(grid):
    rows, cols = len(grid), len(grid[0])
    seen = set()
    count = 0

    def dfs(r, c):
        if not (0 <= r < rows and 0 <= c < cols):
            return
        if grid[r][c] == "0" or (r, c) in seen:
            return
        seen.add((r, c))                 # mutating: no nonlocal needed
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            dfs(r + dr, c + dc)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in seen:
                dfs(r, c)
                count += 1
    return count
```

**`nonlocal`****:** you need it only when the inner function reassigns an outer variable (`best = max(best, x)`, `count += 1`). Calling methods on an outer object (`res.append`, `seen.add`) needs nothing. Forgetting it gives `UnboundLocalError`.

```
def diameter(root):
    best = 0
    def depth(node):
        nonlocal best
        if not node:
            return 0
        left, right = depth(node.left), depth(node.right)
        best = max(best, left + right)
        return 1 + max(left, right)
    depth(root)
    return best
```

**Memoised recursion:**

```
from functools import cache        # or lru_cache(maxsize=None)

@cache
def ways(i):
    if i <= 1:
        return 1
    return ways(i - 1) + ways(i - 2)

ways.cache_clear()                 # between test cases if it's module-level

import sys
sys.setrecursionlimit(10**5)       # default is about 1000 frames
```

**Other useful bits:**

```
first, *rest = nums               # starred unpacking
print(*grid, sep="\n")            # quick debugging
key = lambda x: (x[1], x[0])
```

**Gotchas:**

- `@cache` arguments must be hashable. Pass indices or tuples, never lists.
- `def f(x, memo={})` shares one dict across every call. Use `memo=None` and create it inside.
- Recursion deeper than about 1,000 frames fails. Raise the limit, or switch to an explicit stack or bottom-up DP and say why.

## Classes

You need classes for three things: the node types LeetCode gives you, design questions (Min Stack, LRU Cache, Trie), and making objects comparable inside a heap.

```
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Dummy head: removes the "is this the first node?" special case
dummy = ListNode()
tail = dummy
for v in values:
    tail.next = ListNode(v)
    tail = tail.next
return dummy.next

# Design question shape
class MinStack:
    def __init__(self):
        self.stack = []          # (value, min so far)

    def push(self, val):
        low = min(val, self.stack[-1][1]) if self.stack else val
        self.stack.append((val, low))

    def getMin(self):
        return self.stack[-1][1]

class TrieNode:
    def __init__(self):
        self.children = {}       # char -> TrieNode
        self.is_end = False

# Make an object usable in heapq
class Task:
    def __init__(self, priority, name):
        self.priority, self.name = priority, name
    def __lt__(self, other):
        return self.priority < other.priority
    def __repr__(self):          # readable when you print it
        return f"Task({self.priority}, {self.name!r})"
```

**Gotchas:**

- Test nodes with `if node is None` or `if not node`, but never `if not node.val`: a value of 0 is falsy.
- LeetCode wraps your answer in `class Solution` with `self` as the first parameter. Shared state can go on `self`, but a closure with `nonlocal` is usually cleaner.

## itertools and math

These save lines, but interviewers often want the underlying loop. Use them where the loop isn't the point of the question.

```
from itertools import (accumulate, combinations, permutations, product,
                       pairwise, groupby, chain, count, zip_longest)

list(accumulate([1, 2, 3]))             # [1, 3, 6]
pre = list(accumulate(nums, initial=0)) # [0, 1, 3, 6]: sum(nums[i:j]) == pre[j] - pre[i]
list(accumulate(nums, max))             # running maximum

list(combinations("abc", 2))            # [('a','b'), ('a','c'), ('b','c')]
list(permutations([1, 2, 3]))           # 6 orderings
list(product("ab", repeat=2))           # [('a','a'), ('a','b'), ('b','a'), ('b','b')]
list(pairwise([1, 2, 3]))               # [(1, 2), (2, 3)]   3.10+

[(k, len(list(g))) for k, g in groupby("aaabcc")]   # [('a',3), ('b',1), ('c',2)]
list(chain.from_iterable([[1], [2, 3]]))           # [1, 2, 3]
list(zip_longest("ab", "xyz", fillvalue=""))

import math
math.inf
math.gcd(12, 18), math.lcm(4, 6)        # 6, 12  (lcm: 3.9+)
math.comb(5, 2), math.perm(5, 2)        # 10, 20
math.isqrt(17)                          # 4, exact integer square root
math.ceil(7 / 2), math.floor(-3.5)      # 4, -4
math.log2(8)                            # 3.0

from functools import reduce
reduce(math.gcd, nums)                  # gcd of a whole list
```

**Gotchas:**

- `groupby` only groups *consecutive* equal items. Sort first if you need all equal items together.
- In a backtracking question (Subsets, Permutations), using `combinations` or `permutations` usually skips the thing being tested. Write the recursion, then mention the library alternative.

## Complexity cheat sheet

State these costs out loud when you choose a structure. "Average" for sets and dicts assumes reasonable hashing; the worst case is O(n).



## Common gotchas

These cause most Python-specific bugs in coding rounds. Check your solution against this list before saying "done".

- `[[0] * cols] * rows` shares one row object. Use a comprehension.
- `nums.sort()` returns `None`; `sorted(nums)` returns a new list.
- `-7 // 2 == -4`. Use `int(a / b)` when you need truncation towards zero.
- A mutable default argument (`def f(x, seen=set())`) persists between calls.
- Changing a list, dict or set while looping over it skips items or raises `RuntimeError`. Loop over a copy.
- `grid[:]` copies only the outer list. Use `[row[:] for row in grid]` for a 2-D copy.
- Reassigning an outer variable inside a nested function needs `nonlocal`, otherwise you get `UnboundLocalError`.
- Recursion depth defaults to about 1,000 frames. A 10⁴-node linked list or skewed tree will overflow.
- Heap tuples with equal priorities compare the next element; non-comparable payloads crash. Add a counter.
- `defaultdict[key]` inserts the key just by reading it.
- `{}` is an empty dict; `set()` is an empty set.
- `0`, `""`, `[]` and `None` are all falsy. Use `is None` when 0 is a valid value.
- Use `==` for values and `is` only for `None`. Small-integer caching makes `is` look right in testing and fail later.
- Naming a variable `max`, `min`, `sum`, `list`, `dict`, `str` or `id` breaks the built-in for the rest of the function.
- `range(a, b)` excludes `b`. Backwards to 0 is `range(n - 1, -1, -1)`.
- String concatenation in a loop and `nums[1:]` in recursion both hide an extra factor of n.

## Pattern templates

Each template below has been run and tested. They show the idioms in their natural setting; learn the shape when you reach that pattern in NeetCode, not now.

**Two pointers (sorted input)**

```
def pair_sum(nums, target):
    l, r = 0, len(nums) - 1
    while l < r:
        s = nums[l] + nums[r]
        if s == target:
            return [l, r]
        if s < target:
            l += 1
        else:
            r -= 1
    return []
```

**Sliding window (variable size)**

```
def longest_unique(s):
    last = {}                          # char -> last index seen
    best = left = 0
    for right, ch in enumerate(s):
        if ch in last and last[ch] >= left:
            left = last[ch] + 1
        last[ch] = right
        best = max(best, right - left + 1)
    return best
```

**Monotonic stack (next greater element)**

```
def next_greater(nums):
    res = [-1] * len(nums)
    stack = []                         # indices, values decreasing
    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:
            res[stack.pop()] = x
        stack.append(i)
    return res
```

**BFS shortest path on a grid**

```
from collections import deque

def shortest_path(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    q = deque([(start, 0)])
    seen = {start}                     # mark when enqueuing, not when popping
    while q:
        (r, c), d = q.popleft()
        if (r, c) == goal:
            return d
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols
                    and grid[nr][nc] == 0 and (nr, nc) not in seen):
                seen.add((nr, nc))
                q.append(((nr, nc), d + 1))
    return -1
```

**Topological sort (Kahn's algorithm)**

```
from collections import deque, defaultdict

def topo_order(n, edges):
    graph = defaultdict(list)
    indeg = [0] * n
    for u, v in edges:
        graph[u].append(v)
        indeg[v] += 1
    q = deque(i for i in range(n) if indeg[i] == 0)
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in graph[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order if len(order) == n else []   # [] means a cycle
```

**Dijkstra**

```
import heapq
from collections import defaultdict

def dijkstra(edges, src):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
    dist = {src: 0}
    h = [(0, src)]
    while h:
        d, u = heapq.heappop(h)
        if d > dist.get(u, float("inf")):
            continue                   # stale entry
        for v, w in graph[u]:
            nd = d + w
            if nd < dist.get(v, float("inf")):
                dist[v] = nd
                heapq.heappush(h, (nd, v))
    return dist
```

**Union-Find**

```
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]   # path halving
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False               # already connected: a cycle edge
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True
```

**Backtracking (subsets)**

```
def subsets(nums):
    res, path = [], []
    def backtrack(i):
        if i == len(nums):
            res.append(path[:])        # copy, or every entry is the same list
            return
        path.append(nums[i])
        backtrack(i + 1)
        path.pop()
        backtrack(i + 1)
    backtrack(0)
    return res
```

**Dynamic programming, top-down and bottom-up (coin change)**

```
from functools import cache

def coin_change(coins, amount):
    @cache
    def dp(a):
        if a == 0:
            return 0
        if a < 0:
            return float("inf")
        return 1 + min(dp(a - c) for c in coins)
    ans = dp(amount)
    return -1 if ans == float("inf") else ans

def coin_change_bottom_up(coins, amount):
    dp = [0] + [float("inf")] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return -1 if dp[amount] == float("inf") else dp[amount]
```

**Trie (nested dicts)**

```
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node["$"] = True               # end-of-word marker

    def search(self, word, prefix=False):
        node = self.root
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        return prefix or "$" in node
```

## Practice exercises

37 short exercises, each aimed at one tool. Put `practice.py`, `checks.py` and `solutions.py` in one folder and run `python3 practice.py`. Each exercise shows `ok`, `x` (wrong answer, with the failing check), `!` (crash) or `.` (not started).

Suggested order, matched to your roadmap: sections 1 to 6 this week alongside arrays and hashing; sections 7 to 9 when NeetCode reaches binary search and heaps; 10 to 12 any Saturday. Tick each one off when it passes without help.

**1. Numbers**

- `digit_sum`: sum of digits (divmod)
- `div_trunc`: division truncating towards zero, exact for huge ints
- `ceil_div`: ceiling division without floats

**2. Lists**

- `make_grid`: independent rows
- `rotate_right`: new list rotated by k (slicing, %)
- `transpose`: rows to columns (zip)

**3. Strings**

- `is_palindrome`: ignoring case and punctuation; follow-up with two pointers
- `caesar_shift`: ord/chr arithmetic with wrap-around
- `reverse_words`: split and join

**4. Tuples and sets**

- `group_anagrams`: tuple-of-counts keys
- `has_duplicate`: set size
- `common_to_all`: set intersection

**5. Dictionaries**

- `two_sum`: one-pass index map
- `most_frequent_word`: counting with `get`, tie-break with a tuple key
- `invert_dict`: `setdefault` grouping

**6. collections**

- `top_k_frequent`: Counter plus sort; follow-up with buckets
- `can_construct`: Counter subtraction
- `shortest_path_grid`: BFS with deque
- `window_max`: monotonic deque, O(n)
- `LRUCache`: OrderedDict; follow-up with a linked list

**7. heapq**

- `kth_largest`: size-k min-heap
- `merge_sorted_lists`: k-way merge with tuple entries
- `k_closest`: `nsmallest` with a key

**8. bisect**

- `count_in_range`: `bisect_right - bisect_left`
- `search_insert`: bisect, then by hand
- `first_true`: the hand-written template (checked to be O(log n))

**9. Sorting**

- `sort_by_frequency`: mixed ascending and descending tuple key
- `largest_number`: `cmp_to_key`
- `merge_intervals`: sort by start, merge into a stack

**10. Functions and recursion**

- `make_counter`: closure with `nonlocal`
- `count_islands`: nested DFS without changing the input
- `climb_stairs`: `@cache`, must handle n = 90

**11. Classes**

- `reverse_list`: three pointers on `ListNode`
- `MinStack`: (value, min) tuples

**12. itertools and math**

- `run_lengths`: `groupby`
- `range_sums`: prefix sums with `accumulate(..., initial=0)`
- `gcd_of_list`: `reduce` with `math.gcd`

**After each exercise:** say the time and space complexity out loud, then compare with `solutions.py`. If the idiom there is new to you, add one line to your cheat sheet.

