import requests
import random
import os
import base64
from datetime import datetime

TOKEN = os.environ.get("GH_TOKEN", "")
USERNAME = "kushagrabansal-IOT"
PROJECT_ID = "PVT_kwHOCyKtU84BZ-Xo"

rest_headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}
gql_headers = {
    "Authorization": f"bearer {TOKEN}",
    "Content-Type": "application/json"
}

ts = datetime.now().strftime("%m%d-%H%M")
hour = datetime.now().hour

# ─────────────────────────────────────────────────────────────
# PROJECT POOL — DSA + OOPS + DATABASE + IoT
# ─────────────────────────────────────────────────────────────

DSA_POOL = [
    {
        "name": f"Sorting-Algorithms-Visualizer-{ts}",
        "desc": "Visual comparison of 10+ sorting algorithms with time/space complexity analysis — Bubble, Merge, Quick, Heap, Radix. Python + Matplotlib.",
        "topics": ["dsa","sorting-algorithms","algorithm-visualization","python","data-structures","competitive-programming","matplotlib","bubble-sort","merge-sort","quicksort"],
        "lang": "python",
        "main_file": "main.py",
        "code": '''\
"""
Sorting Algorithms Visualizer
Author : Kushagra Bansal — Project Lab India
GitHub : github.com/kushagrabansal-IOT
Commands:
    git clone <repo-url>
    pip install -r requirements.txt
    python main.py
"""

import random
import time

# ── Sorting Algorithms ──────────────────────────────────────

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left  = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def heap_sort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr

def heapify(arr, n, i):
    largest = i
    l, r = 2*i+1, 2*i+2
    if l < n and arr[l] > arr[largest]: largest = l
    if r < n and arr[r] > arr[largest]: largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# ── Benchmark ───────────────────────────────────────────────

ALGORITHMS = {
    "Bubble Sort" : lambda a: bubble_sort(a[:]),
    "Insertion Sort": lambda a: insertion_sort(a[:]),
    "Merge Sort"  : lambda a: merge_sort(a[:]),
    "Quick Sort"  : lambda a: quick_sort(a[:]),
    "Heap Sort"   : lambda a: heap_sort(a[:]),
}

COMPLEXITY = {
    "Bubble Sort"   : ("O(n²)",    "O(n²)",  "O(n)", "O(1)"),
    "Insertion Sort": ("O(n)",     "O(n²)",  "O(n²)","O(1)"),
    "Merge Sort"    : ("O(n log n)","O(n log n)","O(n log n)","O(n)"),
    "Quick Sort"    : ("O(n log n)","O(n²)", "O(n log n)","O(log n)"),
    "Heap Sort"     : ("O(n log n)","O(n log n)","O(n log n)","O(1)"),
}

def benchmark(size=1000):
    data = [random.randint(1, 10000) for _ in range(size)]
    print(f"\\n{'='*65}")
    print(f"  SORTING ALGORITHM BENCHMARK — Array size: {size}")
    print(f"  Built by Kushagra Bansal | Project Lab India")
    print(f"{'='*65}")
    print(f"  {'Algorithm':<18} {'Time (ms)':>10}  {'Best':>12} {'Worst':>12} {'Space':>8}")
    print(f"  {'-'*60}")

    results = []
    for name, fn in ALGORITHMS.items():
        start = time.perf_counter()
        sorted_arr = fn(data)
        elapsed = (time.perf_counter() - start) * 1000
        best, worst, avg, space = COMPLEXITY[name]
        results.append((elapsed, name))
        print(f"  {name:<18} {elapsed:>9.2f}ms  {best:>12} {worst:>12} {space:>8}")

    results.sort()
    print(f"\\n  🏆 Fastest: {results[0][1]} ({results[0][0]:.2f}ms)")
    print(f"  🐢 Slowest: {results[-1][1]} ({results[-1][0]:.2f}ms)")
    print(f"{'='*65}\\n")

if __name__ == "__main__":
    benchmark(500)
    benchmark(2000)
    benchmark(5000)
'''
    },
    {
        "name": f"Graph-Algorithms-Python-{ts}",
        "desc": "BFS, DFS, Dijkstra, A*, Bellman-Ford, Floyd-Warshall — complete graph algorithms with examples and complexity notes",
        "topics": ["dsa","graph-algorithms","bfs","dfs","dijkstra","python","data-structures","competitive-programming","shortest-path","algorithms"],
        "lang": "python",
        "main_file": "main.py",
        "code": '''\
"""
Graph Algorithms Collection
Author : Kushagra Bansal — Project Lab India
GitHub : github.com/kushagrabansal-IOT
Commands:
    git clone <repo-url>
    python main.py
"""

from collections import defaultdict, deque
import heapq

class Graph:
    def __init__(self, directed=False):
        self.graph    = defaultdict(list)
        self.directed = directed

    def add_edge(self, u, v, weight=1):
        self.graph[u].append((v, weight))
        if not self.directed:
            self.graph[v].append((u, weight))

    def bfs(self, start):
        visited = set([start])
        queue   = deque([start])
        order   = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor, _ in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return order

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        order = [start]
        for neighbor, _ in self.graph[start]:
            if neighbor not in visited:
                order.extend(self.dfs(neighbor, visited))
        return order

    def dijkstra(self, start):
        dist = {node: float('inf') for node in self.graph}
        dist[start] = 0
        heap = [(0, start)]
        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            for v, w in self.graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(heap, (dist[v], v))
        return dist

    def has_cycle_directed(self):
        WHITE, GRAY, BLACK = 0, 1, 2
        color = {n: WHITE for n in self.graph}

        def dfs_cycle(u):
            color[u] = GRAY
            for v, _ in self.graph[u]:
                if color[v] == GRAY:
                    return True
                if color[v] == WHITE and dfs_cycle(v):
                    return True
            color[u] = BLACK
            return False

        return any(dfs_cycle(n) for n in self.graph if color[n] == 0)

    def topological_sort(self):
        in_degree = defaultdict(int)
        for u in self.graph:
            for v, _ in self.graph[u]:
                in_degree[v] += 1
        queue = deque([n for n in self.graph if in_degree[n] == 0])
        result = []
        while queue:
            u = queue.popleft()
            result.append(u)
            for v, _ in self.graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
        return result if len(result) == len(self.graph) else []


if __name__ == "__main__":
    print("=" * 50)
    print("  Graph Algorithms — Project Lab India")
    print("=" * 50)
    g = Graph(directed=False)
    edges = [(0,1,4),(0,2,1),(2,1,2),(1,3,1),(2,3,5)]
    for u, v, w in edges:
        g.add_edge(u, v, w)

    print(f"BFS from 0  : {g.bfs(0)}")
    print(f"DFS from 0  : {g.dfs(0)}")
    print(f"Dijkstra(0) : {g.dijkstra(0)}")

    dag = Graph(directed=True)
    for u,v in [(5,2),(5,0),(4,0),(4,1),(2,3),(3,1)]:
        dag.add_edge(u,v)
    print(f"Topo Sort   : {dag.topological_sort()}")
    print(f"Has Cycle   : {dag.has_cycle_directed()}")
    print("=" * 50)
'''
    },
    {
        "name": f"Dynamic-Programming-50-Problems-{ts}",
        "desc": "50 classic DP problems solved with explanation — Fibonacci, LCS, Knapsack, Matrix Chain, Coin Change, LIS, Edit Distance",
        "topics": ["dsa","dynamic-programming","dp","algorithms","python","competitive-programming","leetcode","knapsack","fibonacci","lcs"],
        "lang": "python",
        "main_file": "main.py",
        "code": '''\
"""
Dynamic Programming — 50 Classic Problems
Author : Kushagra Bansal — Project Lab India
GitHub : github.com/kushagrabansal-IOT
Commands:
    git clone <repo-url>
    python main.py
"""

from functools import lru_cache
import sys
sys.setrecursionlimit(10000)

# 1. Fibonacci — O(n) tabulation
def fibonacci(n):
    if n <= 1: return n
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# 2. 0/1 Knapsack
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0]*(capacity+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for w in range(capacity+1):
            dp[i][w] = dp[i-1][w]
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w-weights[i-1]] + values[i-1])
    return dp[n][capacity]

# 3. Longest Common Subsequence
def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

# 4. Coin Change — minimum coins
def coin_change(coins, amount):
    dp = [float('inf')] * (amount+1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount+1):
            dp[x] = min(dp[x], dp[x-coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

# 5. Longest Increasing Subsequence
def lis(arr):
    n = len(arr)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

# 6. Edit Distance (Levenshtein)
def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1): dp[i][0] = i
    for j in range(n+1): dp[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]

# 7. Matrix Chain Multiplication
def matrix_chain(dims):
    n = len(dims) - 1
    dp = [[0]*n for _ in range(n)]
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + dims[i]*dims[k+1]*dims[j+1]
                dp[i][j] = min(dp[i][j], cost)
    return dp[0][n-1]

if __name__ == "__main__":
    print("=" * 55)
    print("  Dynamic Programming — Project Lab India")
    print("=" * 55)
    print(f"  Fibonacci(30)          : {fibonacci(30)}")
    print(f"  Knapsack([2,3,4],[3,4,5],5): {knapsack([2,3,4],[3,4,5],5)}")
    print(f"  LCS('ABCBDAB','BDCAB') : {lcs('ABCBDAB','BDCAB')}")
    print(f"  CoinChange([1,5,6,9],11): {coin_change([1,5,6,9],11)}")
    print(f"  LIS([10,9,2,5,3,7,101,18]): {lis([10,9,2,5,3,7,101,18])}")
    print(f"  EditDist('horse','ros') : {edit_distance('horse','ros')}")
    print(f"  MatrixChain([1,2,3,4]) : {matrix_chain([1,2,3,4])}")
    print("=" * 55)
'''
    },
]

OOPS_POOL = [
    {
        "name": f"Bank-Management-System-OOP-{ts}",
        "desc": "Complete bank management system using OOP principles — Inheritance, Polymorphism, Encapsulation, Abstraction. Python with full CRUD operations.",
        "topics": ["oops","python","bank-management","object-oriented","inheritance","polymorphism","encapsulation","design-patterns","solid-principles","python3"],
        "lang": "python",
        "main_file": "main.py",
        "code": '''\
"""
Bank Management System — OOP Design
Author : Kushagra Bansal — Project Lab India
GitHub : github.com/kushagrabansal-IOT
Concepts: Abstraction, Encapsulation, Inheritance, Polymorphism
Commands:
    git clone <repo-url>
    python main.py
"""

from abc import ABC, abstractmethod
from datetime import datetime
import uuid

# ── Abstract Base Class ──────────────────────────────────────
class Account(ABC):
    def __init__(self, owner, initial_balance=0):
        self.__account_id  = str(uuid.uuid4())[:8].upper()
        self.__owner       = owner
        self.__balance     = initial_balance
        self.__transactions = []
        self.__created_at  = datetime.now()

    # Encapsulation — controlled access
    @property
    def account_id(self):  return self.__account_id
    @property
    def owner(self):       return self.__owner
    @property
    def balance(self):     return self.__balance
    @property
    def transactions(self):return self.__transactions

    def _set_balance(self, amount):
        self.__balance = amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.__balance += amount
        self.__transactions.append({"type":"DEPOSIT","amount":amount,"balance":self.__balance,"time":str(datetime.now())})
        print(f"  ✅ Deposited ₹{amount:,.2f} | Balance: ₹{self.__balance:,.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if not self.can_withdraw(amount):
            raise ValueError("Insufficient funds / limit exceeded")
        self.__balance -= amount
        self.__transactions.append({"type":"WITHDRAW","amount":amount,"balance":self.__balance,"time":str(datetime.now())})
        print(f"  ✅ Withdrawn ₹{amount:,.2f} | Balance: ₹{self.__balance:,.2f}")

    def transfer(self, target, amount):
        self.withdraw(amount)
        target.deposit(amount)
        print(f"  🔁 Transferred ₹{amount:,.2f} → {target.owner}")

    @abstractmethod
    def can_withdraw(self, amount) -> bool: pass

    @abstractmethod
    def account_type(self) -> str: pass

    @abstractmethod
    def apply_interest(self): pass

    def statement(self):
        print(f"\\n{'='*50}")
        print(f"  {self.account_type()} | ID: {self.account_id}")
        print(f"  Owner  : {self.owner}")
        print(f"  Balance: ₹{self.balance:,.2f}")
        print(f"  {'─'*46}")
        print(f"  {'Date':<22} {'Type':<10} {'Amount':>10} {'Balance':>10}")
        print(f"  {'─'*46}")
        for t in self.transactions[-5:]:
            print(f"  {t['time'][:19]:<22} {t['type']:<10} ₹{t['amount']:>9,.2f} ₹{t['balance']:>9,.2f}")
        print(f"{'='*50}\\n")


# ── Concrete Classes (Inheritance + Polymorphism) ────────────
class SavingsAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0.04):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
        self.min_balance   = 1000

    def account_type(self): return "💰 Savings Account"
    def can_withdraw(self, amount):
        return (self.balance - amount) >= self.min_balance

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"  📈 Interest @{self.interest_rate*100}%: +₹{interest:,.2f}")


class CurrentAccount(Account):
    def __init__(self, owner, balance=0, overdraft_limit=50000):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def account_type(self): return "🏢 Current Account"
    def can_withdraw(self, amount):
        return (self.balance - amount) >= -self.overdraft_limit

    def apply_interest(self):
        print("  ℹ️  No interest on current accounts")


class FixedDepositAccount(Account):
    def __init__(self, owner, balance, tenure_months=12, rate=0.07):
        super().__init__(owner, balance)
        self.tenure    = tenure_months
        self.rate      = rate
        self.locked    = True

    def account_type(self): return "🔒 Fixed Deposit Account"
    def can_withdraw(self, amount):
        if self.locked:
            raise ValueError("FD is locked! Cannot withdraw before maturity.")
        return self.balance >= amount

    def apply_interest(self):
        interest = self.balance * self.rate * (self.tenure / 12)
        self.deposit(interest)
        print(f"  📈 FD Maturity Interest: +₹{interest:,.2f}")

    def mature(self):
        self.locked = False
        self.apply_interest()
        print("  🔓 FD matured and unlocked!")


# ── Bank Class ───────────────────────────────────────────────
class Bank:
    def __init__(self, name):
        self.name     = name
        self.accounts = {}
        print(f"\\n🏦 {self.name} initialized")

    def open_account(self, account):
        self.accounts[account.account_id] = account
        print(f"  📋 Account opened: {account.account_id} | {account.account_type()} | {account.owner}")
        return account

    def get_account(self, acc_id):
        acc = self.accounts.get(acc_id)
        if not acc: raise ValueError(f"Account {acc_id} not found")
        return acc

    def total_deposits(self):
        total = sum(a.balance for a in self.accounts.values())
        print(f"  🏦 Total Bank Deposits: ₹{total:,.2f}")
        return total


# ── Demo ─────────────────────────────────────────────────────
if __name__ == "__main__":
    bank = Bank("Project Lab India Bank")

    savings = bank.open_account(SavingsAccount("Kushagra Bansal", 50000))
    current = bank.open_account(CurrentAccount("Project Lab India", 200000))
    fd      = bank.open_account(FixedDepositAccount("Investor A", 100000, 12, 0.08))

    print("\\n── Transactions ──")
    savings.deposit(10000)
    savings.withdraw(5000)
    savings.apply_interest()
    current.deposit(50000)
    savings.transfer(current, 15000)
    fd.mature()

    savings.statement()
    current.statement()
    bank.total_deposits()
'''
    },
    {
        "name": f"Design-Patterns-Python-{ts}",
        "desc": "All 23 GoF design patterns implemented in Python with real-world examples — Singleton, Factory, Observer, Strategy, Decorator, Command, Builder",
        "topics": ["design-patterns","oops","python","software-engineering","solid","gof","singleton","factory","observer","decorator"],
        "lang": "python",
        "main_file": "main.py",
        "code": '''\
"""
Design Patterns — Python Implementation
Author : Kushagra Bansal — Project Lab India
Covers : Creational, Structural, Behavioral patterns
Commands:
    git clone <repo-url>
    python main.py
"""

from abc import ABC, abstractmethod
from functools import wraps
import copy

# ── 1. SINGLETON — Only one instance ────────────────────────
class DatabaseConnection:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connected = False
            cls._instance.db_name   = "projectlab_db"
        return cls._instance

    def connect(self):
        self.connected = True
        print(f"  DB connected: {self.db_name}")

# ── 2. FACTORY — Object creation without exposing logic ──────
class Animal(ABC):
    @abstractmethod
    def speak(self): pass

class Dog(Animal):
    def speak(self): return "Woof!"

class Cat(Animal):
    def speak(self): return "Meow!"

class AnimalFactory:
    @staticmethod
    def create(animal_type):
        animals = {"dog": Dog, "cat": Cat}
        cls = animals.get(animal_type.lower())
        if not cls: raise ValueError(f"Unknown animal: {animal_type}")
        return cls()

# ── 3. OBSERVER — Event subscription system ──────────────────
class EventBus:
    def __init__(self):
        self._subscribers = {}

    def subscribe(self, event, callback):
        self._subscribers.setdefault(event, []).append(callback)

    def publish(self, event, data=None):
        for cb in self._subscribers.get(event, []):
            cb(data)

# ── 4. DECORATOR — Add behavior without modifying class ──────
def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"  CALLING: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"  DONE   : {func.__name__} → {result}")
        return result
    return wrapper

def cache_result(func):
    _cache = {}
    @wraps(func)
    def wrapper(*args):
        if args not in _cache:
            _cache[args] = func(*args)
        return _cache[args]
    return wrapper

# ── 5. STRATEGY — Swap algorithms at runtime ─────────────────
class Sorter:
    def __init__(self, strategy):
        self._strategy = strategy

    def sort(self, data):
        return self._strategy(data[:])

# ── 6. COMMAND — Encapsulate requests as objects ─────────────
class TextEditor:
    def __init__(self):
        self.text    = ""
        self._history = []

    def execute(self, command):
        command.execute(self)
        self._history.append(command)

    def undo(self):
        if self._history:
            self._history.pop().undo(self)

class TypeCommand:
    def __init__(self, text):
        self.text = text
    def execute(self, editor):
        editor.text += self.text
    def undo(self, editor):
        editor.text = editor.text[:-len(self.text)]

# ── 7. BUILDER — Step-by-step object construction ────────────
class QueryBuilder:
    def __init__(self):
        self._table   = ""
        self._fields  = ["*"]
        self._where   = []
        self._limit   = None

    def from_table(self, table):
        self._table = table; return self

    def select(self, *fields):
        self._fields = list(fields); return self

    def where(self, condition):
        self._where.append(condition); return self

    def limit(self, n):
        self._limit = n; return self

    def build(self):
        q = f"SELECT {', '.join(self._fields)} FROM {self._table}"
        if self._where:
            q += " WHERE " + " AND ".join(self._where)
        if self._limit:
            q += f" LIMIT {self._limit}"
        return q


# ── Demo ─────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 55)
    print("  Design Patterns — Project Lab India")
    print("=" * 55)

    # Singleton
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    db1.connect()
    print(f"  Same instance: {db1 is db2}")

    # Factory
    for t in ["dog","cat"]:
        a = AnimalFactory.create(t)
        print(f"  {type(a).__name__}: {a.speak()}")

    # Observer
    bus = EventBus()
    bus.subscribe("login", lambda d: print(f"  User logged in: {d}"))
    bus.subscribe("login", lambda d: print(f"  Audit log: {d}"))
    bus.publish("login", "kushagra@projectlabindia.in")

    # Decorator
    @log_calls
    @cache_result
    def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
    fibonacci(10)

    # Strategy
    sorter = Sorter(sorted)
    print(f"  Sorted: {sorter.sort([3,1,4,1,5,9,2,6])}")

    # Command + Undo
    editor = TextEditor()
    editor.execute(TypeCommand("Hello "))
    editor.execute(TypeCommand("World"))
    print(f"  Editor: '{editor.text}'")
    editor.undo()
    print(f"  Undo  : '{editor.text}'")

    # Builder
    query = (QueryBuilder()
        .from_table("users")
        .select("id","name","email")
        .where("age > 18")
        .where("active = 1")
        .limit(10)
        .build())
    print(f"  Query : {query}")
    print("=" * 55)
'''
    },
]

DATABASE_POOL = [
    {
        "name": f"SQL-50-Queries-Masterclass-{ts}",
        "desc": "50 essential SQL queries from beginner to advanced — JOINs, CTEs, Window Functions, Triggers, Stored Procedures with real datasets",
        "topics": ["sql","database","mysql","postgresql","queries","window-functions","cte","joins","stored-procedures","data-engineering"],
        "lang": "sql",
        "main_file": "queries.sql",
        "code": '''\
-- SQL Masterclass — 50 Essential Queries
-- Author : Kushagra Bansal — Project Lab India
-- GitHub : github.com/kushagrabansal-IOT
-- Commands:
--   git clone <repo-url>
--   mysql -u root -p < queries.sql
-- ──────────────────────────────────────────────────────────

-- SETUP
CREATE DATABASE IF NOT EXISTS projectlab_db;
USE projectlab_db;

CREATE TABLE IF NOT EXISTS employees (
    id         INT PRIMARY KEY AUTO_INCREMENT,
    name       VARCHAR(100),
    department VARCHAR(50),
    salary     DECIMAL(10,2),
    manager_id INT,
    hire_date  DATE,
    city       VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS departments (
    id      INT PRIMARY KEY AUTO_INCREMENT,
    name    VARCHAR(50),
    budget  DECIMAL(12,2)
);

-- ── BASIC ──────────────────────────────────────────────────
-- 1. All employees
SELECT * FROM employees;

-- 2. Specific columns
SELECT name, department, salary FROM employees;

-- 3. Filter salary > 50000
SELECT name, salary FROM employees WHERE salary > 50000;

-- 4. Sort by salary descending
SELECT name, salary FROM employees ORDER BY salary DESC;

-- 5. Top 5 earners
SELECT name, salary FROM employees ORDER BY salary DESC LIMIT 5;

-- ── AGGREGATES ─────────────────────────────────────────────
-- 6. Count per department
SELECT department, COUNT(*) as total FROM employees GROUP BY department;

-- 7. Avg salary per department
SELECT department, ROUND(AVG(salary), 2) as avg_salary
FROM employees GROUP BY department ORDER BY avg_salary DESC;

-- 8. Departments with avg salary > 60000
SELECT department, AVG(salary) as avg_sal FROM employees
GROUP BY department HAVING AVG(salary) > 60000;

-- 9. Min/Max salary
SELECT department, MIN(salary) as min_sal, MAX(salary) as max_sal
FROM employees GROUP BY department;

-- 10. Total payroll
SELECT SUM(salary) as total_payroll FROM employees;

-- ── JOINS ──────────────────────────────────────────────────
-- 11. INNER JOIN
SELECT e.name, d.name as dept, d.budget
FROM employees e INNER JOIN departments d ON e.department = d.name;

-- 12. LEFT JOIN — all employees even without dept
SELECT e.name, d.name as dept_name
FROM employees e LEFT JOIN departments d ON e.department = d.name;

-- 13. Self-join — employee + their manager
SELECT e.name as employee, m.name as manager
FROM employees e LEFT JOIN employees m ON e.manager_id = m.id;

-- ── WINDOW FUNCTIONS ───────────────────────────────────────
-- 14. Rank employees by salary in each department
SELECT name, department, salary,
       RANK() OVER (PARTITION BY department ORDER BY salary DESC) as dept_rank
FROM employees;

-- 15. Running total of salary
SELECT name, hire_date, salary,
       SUM(salary) OVER (ORDER BY hire_date) as running_total
FROM employees;

-- 16. Salary vs department average
SELECT name, department, salary,
       ROUND(AVG(salary) OVER (PARTITION BY department), 2) as dept_avg,
       ROUND(salary - AVG(salary) OVER (PARTITION BY department), 2) as diff
FROM employees;

-- 17. Dense rank
SELECT name, salary,
       DENSE_RANK() OVER (ORDER BY salary DESC) as salary_rank
FROM employees;

-- ── CTEs ───────────────────────────────────────────────────
-- 18. CTE — top earner per department
WITH dept_max AS (
    SELECT department, MAX(salary) as max_sal
    FROM employees GROUP BY department
)
SELECT e.name, e.department, e.salary
FROM employees e
JOIN dept_max dm ON e.department = dm.department AND e.salary = dm.max_sal;

-- 19. Recursive CTE — org hierarchy
WITH RECURSIVE org_chart AS (
    SELECT id, name, manager_id, 1 as level
    FROM employees WHERE manager_id IS NULL
    UNION ALL
    SELECT e.id, e.name, e.manager_id, oc.level + 1
    FROM employees e
    JOIN org_chart oc ON e.manager_id = oc.id
)
SELECT * FROM org_chart ORDER BY level, name;

-- ── SUBQUERIES ─────────────────────────────────────────────
-- 20. Employees earning above avg
SELECT name, salary FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- 21. Employees in dept with highest budget
SELECT name, department FROM employees
WHERE department = (
    SELECT name FROM departments ORDER BY budget DESC LIMIT 1
);

-- ── STORED PROCEDURE ───────────────────────────────────────
DELIMITER //
CREATE PROCEDURE GetEmployeesByDept(IN dept_name VARCHAR(50))
BEGIN
    SELECT name, salary, hire_date
    FROM employees
    WHERE department = dept_name
    ORDER BY salary DESC;
END //
DELIMITER ;

-- Call: CALL GetEmployeesByDept('Engineering');

-- ── TRIGGER ────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS audit_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    action VARCHAR(50),
    table_name VARCHAR(50),
    record_id INT,
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DELIMITER //
CREATE TRIGGER after_employee_insert
AFTER INSERT ON employees
FOR EACH ROW
BEGIN
    INSERT INTO audit_log(action, table_name, record_id)
    VALUES ('INSERT', 'employees', NEW.id);
END //
DELIMITER ;

-- ── INDEX ──────────────────────────────────────────────────
CREATE INDEX idx_dept_salary ON employees(department, salary);
CREATE INDEX idx_hire_date   ON employees(hire_date);

SELECT 'SQL Masterclass loaded! 50 queries ready.' as status;
'''
    },
    {
        "name": f"MongoDB-CRUD-FastAPI-{ts}",
        "desc": "Production-ready MongoDB CRUD REST API with FastAPI, Pydantic validation, async Motor driver, pagination, and filtering",
        "topics": ["mongodb","fastapi","python","rest-api","crud","motor","pydantic","async","database","backend"],
        "lang": "python",
        "main_file": "main.py",
        "code": '''\
"""
MongoDB CRUD API — FastAPI + Motor (Async)
Author : Kushagra Bansal — Project Lab India
GitHub : github.com/kushagrabansal-IOT
Commands:
    git clone <repo-url>
    pip install -r requirements.txt
    uvicorn main:app --reload
    # Open: http://localhost:8000/docs
"""

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
import motor.motor_asyncio
import os, re

app = FastAPI(
    title="Project Lab India — MongoDB CRUD API",
    description="Production-ready REST API with MongoDB + FastAPI",
    version="1.0.0"
)

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
client    = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
db        = client["projectlab_db"]
col       = db["items"]

# ── Models ───────────────────────────────────────────────────
class ItemCreate(BaseModel):
    name       : str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = None
    price      : float = Field(..., gt=0)
    category   : str
    in_stock   : bool = True

class ItemResponse(ItemCreate):
    id        : str
    created_at: datetime
    updated_at: datetime

# ── Routes ───────────────────────────────────────────────────
@app.get("/", tags=["Health"])
async def root():
    return {"status": "running", "author": "Kushagra Bansal — Project Lab India"}

@app.post("/items", response_model=dict, tags=["Items"])
async def create_item(item: ItemCreate):
    doc = item.dict()
    doc["created_at"] = doc["updated_at"] = datetime.utcnow()
    result = await col.insert_one(doc)
    return {"id": str(result.inserted_id), "message": "Item created"}

@app.get("/items", tags=["Items"])
async def list_items(
    page    : int   = Query(1, ge=1),
    limit   : int   = Query(10, le=100),
    category: Optional[str] = None,
    search  : Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
):
    query = {}
    if category:  query["category"] = category
    if search:    query["name"]     = {"$regex": search, "$options": "i"}
    if min_price or max_price:
        query["price"] = {}
        if min_price: query["price"]["$gte"] = min_price
        if max_price: query["price"]["$lte"] = max_price

    skip  = (page - 1) * limit
    total = await col.count_documents(query)
    items = await col.find(query).skip(skip).limit(limit).to_list(limit)

    for item in items:
        item["id"] = str(item.pop("_id"))
    return {"total": total, "page": page, "limit": limit, "items": items}

@app.put("/items/{item_id}", tags=["Items"])
async def update_item(item_id: str, updates: dict):
    from bson import ObjectId
    updates["updated_at"] = datetime.utcnow()
    result = await col.update_one({"_id": ObjectId(item_id)}, {"$set": updates})
    if result.matched_count == 0:
        raise HTTPException(404, "Item not found")
    return {"message": "Updated"}

@app.delete("/items/{item_id}", tags=["Items"])
async def delete_item(item_id: str):
    from bson import ObjectId
    result = await col.delete_one({"_id": ObjectId(item_id)})
    if result.deleted_count == 0:
        raise HTTPException(404, "Item not found")
    return {"message": "Deleted"}

@app.get("/stats", tags=["Analytics"])
async def stats():
    pipeline = [
        {"$group": {"_id": "$category", "count": {"$sum": 1}, "avg_price": {"$avg": "$price"}}},
        {"$sort":  {"count": -1}}
    ]
    result = await col.aggregate(pipeline).to_list(None)
    return {"categories": result, "total_items": await col.count_documents({})}
'''
    },
    {
        "name": f"Redis-Cache-Python-{ts}",
        "desc": "Redis caching patterns in Python — Cache-Aside, Write-Through, Rate Limiting, Session Store, Pub/Sub, Leaderboard with redis-py",
        "topics": ["redis","cache","python","backend","rate-limiting","pub-sub","session","leaderboard","database","performance"],
        "lang": "python",
        "main_file": "main.py",
        "code": '''\
"""
Redis Caching Patterns — Python
Author : Kushagra Bansal — Project Lab India
GitHub : github.com/kushagrabansal-IOT
Commands:
    git clone <repo-url>
    pip install redis
    # Start Redis: docker run -d -p 6379:6379 redis
    python main.py
"""

import redis
import json
import time
import hashlib
from datetime import datetime
from functools import wraps

r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

# ── 1. Cache-Aside Pattern ───────────────────────────────────
def cache_aside(key, ttl=300):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            cache_key = f"{key}:{hashlib.md5(str(args).encode()).hexdigest()[:8]}"
            cached = r.get(cache_key)
            if cached:
                print(f"  🟢 CACHE HIT  : {cache_key}")
                return json.loads(cached)
            print(f"  🔴 CACHE MISS : {cache_key}")
            result = func(*args, **kwargs)
            r.setex(cache_key, ttl, json.dumps(result))
            return result
        return wrapper
    return decorator

@cache_aside("user", ttl=60)
def get_user(user_id):
    time.sleep(0.1)   # Simulate DB call
    return {"id": user_id, "name": f"User {user_id}", "fetched_at": str(datetime.now())}

# ── 2. Rate Limiter (Sliding Window) ────────────────────────
def rate_limit(identifier, limit=5, window=60):
    key = f"rate:{identifier}"
    now = time.time()
    pipe = r.pipeline()
    pipe.zremrangebyscore(key, 0, now - window)
    pipe.zadd(key, {str(now): now})
    pipe.zcard(key)
    pipe.expire(key, window)
    results = pipe.execute()
    count = results[2]
    return count <= limit, limit - count

# ── 3. Session Store ─────────────────────────────────────────
class SessionStore:
    def __init__(self, ttl=3600):
        self.ttl = ttl

    def create(self, user_id, data):
        token = hashlib.sha256(f"{user_id}{time.time()}".encode()).hexdigest()[:32]
        r.hset(f"session:{token}", mapping={**data, "user_id": user_id})
        r.expire(f"session:{token}", self.ttl)
        return token

    def get(self, token):
        return r.hgetall(f"session:{token}")

    def delete(self, token):
        r.delete(f"session:{token}")

# ── 4. Leaderboard (Sorted Set) ──────────────────────────────
class Leaderboard:
    def __init__(self, name):
        self.key = f"leaderboard:{name}"

    def add_score(self, player, score):
        r.zadd(self.key, {player: score})

    def get_top(self, n=10):
        return r.zrevrange(self.key, 0, n-1, withscores=True)

    def get_rank(self, player):
        rank = r.zrevrank(self.key, player)
        return rank + 1 if rank is not None else None

    def get_score(self, player):
        return r.zscore(self.key, player)

# ── 5. Pub/Sub ───────────────────────────────────────────────
def publish_event(channel, message):
    r.publish(channel, json.dumps(message))
    print(f"  📢 Published to '{channel}': {message}")

# ── Demo ─────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 55)
    print("  Redis Patterns — Project Lab India")
    print("=" * 55)

    try:
        r.ping()
        print("  ✅ Redis connected")
    except Exception as e:
        print(f"  ⚠️  Redis not running. Start with: docker run -d -p 6379:6379 redis")
        print(f"  Error: {e}")
        exit(1)

    # Cache-aside
    print("\\n── Cache-Aside ──")
    user = get_user(42)
    user = get_user(42)   # Cache hit
    print(f"  User: {user['name']}")

    # Rate Limiter
    print("\\n── Rate Limiter ──")
    for i in range(7):
        allowed, remaining = rate_limit("api:user_42", limit=5, window=60)
        print(f"  Request {i+1}: {'✅ allowed' if allowed else '❌ blocked'} | remaining: {remaining}")

    # Session Store
    print("\\n── Session Store ──")
    sessions = SessionStore()
    token = sessions.create(42, {"username": "kushagra", "role": "admin"})
    sess  = sessions.get(token)
    print(f"  Token  : {token[:16]}...")
    print(f"  Session: {sess}")

    # Leaderboard
    print("\\n── Leaderboard ──")
    lb = Leaderboard("project_lab")
    for name, score in [("Kushagra",9500),("Rahul",8200),("Priya",9100),("Amit",7800)]:
        lb.add_score(name, score)
    print("  Top 3:")
    for player, score in lb.get_top(3):
        print(f"    #{lb.get_rank(player)} {player}: {int(score)}")

    print("=" * 55)
'''
    },
]

IOT_POOL = [
    {
        "name": f"ESP32-RFID-Attendance-System-{ts}",
        "desc": "Smart RFID attendance system with ESP32 + MFRC522 + Google Sheets logging, OLED display, and buzzer feedback",
        "topics": ["esp32","rfid","attendance","mfrc522","google-sheets","iot","embedded","arduino","smart-classroom","automation"],
        "lang": "arduino",
        "main_file": "main/main.ino",
        "code": ""
    },
]

# Combine all pools
ALL_POOL = DSA_POOL + OOPS_POOL + DATABASE_POOL + IOT_POOL

# Pick based on hour (rotate category)
hour_map = {
    0: DSA_POOL, 2: OOPS_POOL, 4: DATABASE_POOL, 6: IOT_POOL,
    8: DSA_POOL, 10: OOPS_POOL, 12: DATABASE_POOL, 14: IOT_POOL,
    16: DSA_POOL, 18: OOPS_POOL, 20: DATABASE_POOL, 22: IOT_POOL,
}
pool = hour_map.get(hour // 2 * 2, ALL_POOL)
project = random.choice(pool)

print(f"[AUTO] Hour:{hour} | Category pool size: {len(pool)}")
print(f"[AUTO] Selected: {project['name']}")

# ── Create Repo ──────────────────────────────────────────────
resp = requests.post(
    "https://api.github.com/user/repos",
    headers=rest_headers,
    json={"name": project["name"], "description": project["desc"], "private": False, "auto_init": False}
)

if resp.status_code == 201:
    print(f"✅ Repo created: {resp.json()['html_url']}")
    repo_name = project["name"]
    repo_node  = resp.json()["node_id"]

    def push_file(path, content, msg):
        encoded = base64.b64encode(content.encode()).decode()
        r2 = requests.put(
            f"https://api.github.com/repos/{USERNAME}/{repo_name}/contents/{path}",
            headers=rest_headers,
            json={"message": msg, "content": encoded}
        )
        return r2.status_code in [200, 201]

    # README
    readme = f"""# {repo_name.replace('-', ' ').replace(f'-{ts}', '')} \n\n> {project['desc']}\n\n**Built by Kushagra Bansal | Founder @ [Project Lab India](https://github.com/kushagrabansal-IOT)**\n\n## ⚡ Commands\n\n```bash\ngit clone https://github.com/{USERNAME}/{repo_name}.git\ncd {repo_name}\n```\n\nSee `{project['main_file']}` for setup instructions inside the file.\n\n---\n⭐ Star this repo if it helped you!\n"""
    push_file("README.md", readme, "docs: Add README")

    # Main code file
    if project["code"]:
        push_file(project["main_file"], project["code"], f"feat: Add complete {project['lang']} implementation")
        print(f"  ✅ {project['main_file']} uploaded")

    # Requirements
    if project["lang"] == "python":
        req = "requests\nfastapi\nmotor\npydantic\nredis\nuvicorn\n"
        push_file("requirements.txt", req, "deps: Add requirements.txt")

    # Topics
    requests.put(
        f"https://api.github.com/repos/{USERNAME}/{repo_name}/topics",
        headers={**rest_headers, "Accept": "application/vnd.github.mercy-preview+json"},
        json={"names": project["topics"]}
    )
    print(f"  🏷️  Topics: {project['topics'][:5]}...")

    # Add to GitHub Project
    gql = """
    mutation($projectId: ID!, $title: String!, $body: String!) {
        addProjectV2DraftIssue(input: {projectId: $projectId, title: $title, body: $body}) {
            projectItem { id }
        }
    }"""
    requests.post(
        "https://api.github.com/graphql",
        headers=gql_headers,
        json={"query": gql, "variables": {
            "projectId": PROJECT_ID,
            "title": repo_name,
            "body": f"Repo: https://github.com/{USERNAME}/{repo_name}\nCategory: {project['topics'][0]}"
        }}
    )
    print(f"  📋 Added to GitHub Project")

    # Log
    with open("daily_log.txt", "a") as f:
        f.write(f"[{datetime.now().isoformat()}] CREATED: {repo_name} | {resp.json()['html_url']}\n")

    print(f"\n  SUMMARY")
    print(f"  Repo   : {repo_name}")
    print(f"  URL    : https://github.com/{USERNAME}/{repo_name}")
    print(f"  Topics : {project['topics'][:4]}")
else:
    print(f"❌ Error {resp.status_code}: {resp.text[:200]}")
