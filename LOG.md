## Day 1 — [13-08-2026]
**Branch:** day-01/toolchain-setup
**Commit:** b4fe472
**What I did: Today I setup my local env like install all the dependencies like puthon, git, uv and then and create and write readme and log.md file for summary**
**What broke or confused me:**
 I installed python latest version(3.14.4) but for this project with langraph kinda techstack python3.14.4 is too new.so I installed 3.12 alongside it 
**What I still don't understand:**
RESOLVED — venv isolates each project's packages so they don't 
conflict with each other or break system Python. Each project 
gets its own clean environment.





## Day 2 — [14-08-2026]
**Branch:** day-02/terminal-and-git
**Warmup — from memory, no looking up:**
git commit vs git push: git commit save changes locally and git push uploads local changes remotely.
**What I will do today:**
Terminal navigation, file operations, git workflow practice
## Excercise:
1. ls -la ===> -l gives list of files with long format like permissions, owner, size, dates and -a is used for list all the hidden files
2. I ran myscript.py and the error i got because wrong filename/we are in wrong dir
3. git diff: it is used for tracking changes in my working directory that are not staged yet(like uncommited changes since my last save)



## Day 3 — [14-08-2026]
**Branch:** day-03/first-python
**Predictions before running:**
- type(5) → int
- type(5.0) → float
- type("5") → string
- type(True) → boolean
**acutal output:**
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>

# qs: 
why does Python use str and bool instead of string and boolean? ---> Python uses str and bool for consistency, matching its other shortened built-in types like int and dict to reduce repetitive typing


## Day 4 - [15-08-2026]
**Branch:** day-04/variables-and-types
**Predictions before running:**
# What does each line print?
a = "5"  
b = 3     
print(a + a)   ---> 55 
print(b + b)   ---> 6
print(a * 3)   ---> 555  = = str repeatation creates "5" repeated 3 times
print(b * 3)   ---> 9
# qs:
Why does a + a not give you 10?---> Because a is string var, in python using the (+) operator performs string concatenation(joining the text/string together) rather than numerical addition.
# type conversion
c = int(a)
print(c + b)
print(type(c))
# qs:
What does int(a) do?
--> it converts the string to int type
# qs:
What does c + b print?
--> 8
# qs:
What does type(c) print?
--> <class 'int'>
# qs: 
print this --> print(a + b)
what is the exact error name, and why does Python refuse to do this?
--> Exact error = TypeError: can only concatenate str (not "int") to str
because python blocks this because strings and integers are incompatible types, and python avoids guessing whether we want text concatenation ("53") or arithmetic addition(8)


## Day 5,6 - [17-08-2026]
**Branch:** day-05/tip-calculator
# Why do you need to convert input() before doing math?
Because python input() function always returns a string(str). Even if the user types numbers to perform arithmetic, Python needs the value to be numerical type like int or float.
# What happens if you don't?
Addition joins strings together("5"+"5" = "55"), or throws a TypeError if mixed with a number ("5"+5).
Subtraction & Division always throw a TypeError because math is not defined for strings
Multiplication repeats the string if multiplied by an integer("5"*3="555"), but throws a TypeError if multiplied by another string ("5" * "5").
# Sprint 0 Gate:
1. What does AUTH_DISABLED do and why does it exist in the reference app?
--> AUTH_DISABLED is an env var used or configuration flag used to turn off user authentication checks across the application.
--> when AUTH_DISABLED is set to true or 1, the app skips mandatory sign in pages, OAuth redirects and token checks.
--> Instead of validadting JWT token or session cookies, backend middleware typically assigns a static "mock" or "admin" user to all incoming API requests.
--> Routes guarded by authentication middleware treat every request as authorized.
It exists is referenced app because of fast local setup, easy E2E testing, simpler debugging. 
2. How many databases does the reference app use and what are they for?
--> Mainly two,  orchestrai_ops and orchestrai_config
orchestrai_ops: stores operational data (requests, workflow state, job history)
orchestrai_config: stores admin config (settings, policies, catalog)
3. What is the difference between // and / in Python?
--> / performs standard devision and always returns a floating point number. 
--> // performs floor devision. it divides the number and rounds down to the nearest whole integer.
4. What does f"{value:.2f}" do — break down each part?
--> f"..." = f string prefix. Tells python to evaluate variables and expressions insdie {}.
--> value = variable/expression. The numerical value(int/float) we want to format
--> : = format specifier seperator. seperates the   variable name from the formatting rules that follow.
--> .2 = Precision specifier. Controls rounding and forces 2 digits after the decimal point.
--> f = Presentation Type = Stands for "fixed-point" notation.

# WARMUP
1. what does "hello"[1:4] print and why?
--> it prints "ell". Because python follows zero-based indexing and this is string slicing that includes start and end. Here, start at index 1, which is 'e' and end at index 4 which stops before index 4(it includes 1, 2, 3).
so, [1:4] pulls char at index 1, 2, 3 and giving us "ell". 
2. What does [::-1] actually mean?
--> [start:stop:step]
here, start empty, stop also empty, step is -1 which tells python to step backward thorugh the string one index at a time. 


## Day 7 - [18-08-2026]
**Branch:** day-07/control-flow
# WARMUP
1. **Predictions before running:**
print(bool(""))   ---> False  --> an empty string containing zero char is considered falsy
print(bool("0"))  ---> True   --> any non empty evaluates to True, even if the text inside happens to be char "0"
print(bool([]))   ---> False --> any empty list conatains no elements and is falsy
print(bool([0]))  ---> True --> a non-empty list(even if it's only item is 0) evaluates to True
print(bool(None)) ---> False --> None represents the absence of a value and is always falsy. 


## Day 8 - [24-08-2026]
**Branch:** day-08/loops
# WARMUP
1. **Predictions before running:**
for i in range(2, 10, 3):
    print(i)
--> It means: start at 2, stop before 10, step by 3. So: 2, then 2+3=5, then 5+3=8, then 8+3=11 which exceeds 10 so stop.It prints: 2, 5, 8.



# Day 9 - [24-08-2026]
**Branch:** day-09/lists-and-tuples
# WARMUP
1. **Predictions before running:**
a = [1, 2, 3]
b = a
b.append(4) ---> creating a second name that points to the same list in memory
print(a) ---> [1, 2, 3, 4]
--> . Both a and b point to the same object — so appending via b changes what a sees too.
--> fix: make b an independent copy so appending to it doesn't affect a
1. option A:  b = a.copy()
2: option B: b = a[:]
3. Option c: b = list(a)
# Still Fuzzy
list exercises crash on empty input — need try/except



# Day 10 - [26-08-2026]
**Branch:** day-10/functions
# WARMUP
**Predictions before running:**
def add_item(item, basket=[]):
    basket.append(item)
    return basket

print(add_item("a"))   --> ['a'] ----> It appends a in basket list
print(add_item("b"))   --> ['a', 'b']   ---> It appens b in basket list along with a
Why does basket still contain "a" when you call add_item("b")?
--> Because, default arguments in python are created only once when defined. So, calls resue the exact same list in memory. It uses the shared list.
1. how do we make each call get its own fresh list?
Use None as the default argument, and instantiate a new empty list  inside the function whenever None is passed.
def add_item(item, basket=None):
    if basket is None:
        basket = []   # Creates a brand new list everytime
    basket.appened(item)
    return basket
print(add_item("a"))   # output: ['a']



# Day 11 - [03-09-2026]
**Branch:** day-11/errors-and-exceptions
# WARMUP
**Predictions before running:**
1. what is the diff? Why is Option B better than Option A?
**Option A**
try:
    result = int(input("Enter number: "))
except:
    print("bad input")

**Option B**  
try:
    result = int(input("Enter number: "))
except ValueError:
    print("bad input")
--> Option A uses a bare except that dangerously catches system signals like Ctrl+C and masks hidden bugs, whereas Option B specifically catches only ValueError for invalid inputs, making execution safe and easy to debug.Bare except swallows everything including KeyboardInterrupt and SystemExit — signals the OS sends that our program should never silently ignore. Always catch the specific exception we expect.




# Day 12 - [03-09-2026]
**Branch:** day-12/dictionaries
# WARMUP
**Predictions before running:**
**1. What happens and why? Does it print, or does it crash?**
counts = {}
for c in ["aws", "aws", "gcp"]:
    counts[c] += 1
print(counts)
--> it crashes. Iterating through a list and using those strings as dictionary keys is completely valid Python syntax.
--> It crashes with a KeyError on the very first loop iteration (c = "aws") when executing counts[c] += 1.
**--> Why It Crashes**
The expression counts[c] += 1 is shorthand for:
counts[c] = counts[c] + 1
To compute counts["aws"] + 1, Python must first read the current value of counts["aws"]. But because counts is completely empty ({}), the key "aws" does not exist yet, raising a KeyError: 'aws'.
**--> How to Fix It**
To increment counts in a dictionary, we have three primary options:
**Option 1: Initialize the key if missing (dict.get())**
counts = {}
for c in ["aws", "aws", "gcp"]:
    counts[c] = counts.get(c, 0) + 1  # Falls back to 0 if key doesn't exist

print(counts)  # Output: {'aws': 2, 'gcp': 1}
**Option 2: Defensive if/else check**
counts = {}
for c in ["aws", "aws", "gcp"]:
    if c not in counts:
        counts[c] = 0
    counts[c] += 1
**Option 3: Use collections.defaultdict**
from collections import defaultdict

counts = defaultdict(int)  # Automatically defaults missing keys to 0
for c in ["aws", "aws", "gcp"]:
    counts[c] += 1
--> counts.get(cloud, 0) + 1 looks up the key cloud to get its current count (returning 0 if the key doesn't exist yet) and adds 1 to it.
**second way-->**
The second way is using defaultdict from the collections module, which automatically initializes missing keys with a default value (like 0 for integers) whenever we access or modify them:
from collections import defaultdict

counts = defaultdict(int)  # Automatically defaults missing keys to 0

for cloud in ["aws", "gcp", "aws"]:
    counts[cloud] += 1  # No KeyError! Missing keys start at 0
2. One question on your inversion code:
python
for cloud, region in original.items():
    inverted[region] = cloud
What happens if two clouds map to the same region? Which one wins and why? Write the answer in LOG.
LOG: DICTIONARY INVERSION COLLISION ANALYSIS

[INPUT DATASET]
original = {
    "aws": "us-east-1",
    "azure": "us-east-1"  <-- Duplicate value collision on region key
}

[EXECUTION TRACE]
- Pass 1: cloud="aws", region="us-east-1"
  Execution: inverted["us-east-1"] = "aws"
  State: inverted = {"us-east-1": "aws"}

- Pass 2: cloud="azure", region="us-east-1"
  Execution: inverted["us-east-1"] = "azure"
  State: inverted = {"us-east-1": "azure"}

[COLLISION RESULT]
Winner: "azure" (The last processed key)

[MECHANISM & CAUSE]
1. Python dictionaries require every key to be strictly unique.
2. Direct key assignment (`dict[key] = value`) performs an in-place update if 
   the target key already exists.
3. Therefore, subsequent iterations overwrite previous assignments, causing 
   earlier keys ("aws") to be silently replaced by later ones ("azure").

[DEFENSIVE RESOLUTION]
To retain all values without loss, map each inverted key to a list:

  inverted = {}
  for cloud, region in original.items():
      inverted.setdefault(region, []).append(cloud)

  Result: {"us-east-1": ["aws", "azure"]}





# Day 12 - [03-09-2026]
**Branch:** day-12/files-and-json
# WARMUP
**Predictions before running:**
with open("data.txt", "w") as f:
    f.write("hello")
1. What does "w" mode do if the file already exists?
--> It overwrites (truncates) the file completely, erasing all existing content the moment the file is opened.
2. What does with give you that a bare open() doesn't?
--> with acts as a Context Manager that guarantees the file is automatically closed when the block finishes, even if an unhandled exception or crash occurs inside the block.
It eliminates the need to manually call f.close().
3. What happens to the file if your program crashes inside a bare open() without closing it?
--> Data Loss / Unflushed Buffers: Python buffers file writes in memory for performance. If the script crashes before f.close() or f.flush() runs, pending data inside the buffer may never write to disk, leaving the file empty or incomplete.
--> File Resource Locks: On operating systems like Windows, the file handle remains locked by the operating system until the process is completely terminated, preventing other applications or scripts from editing, renaming, or deleting it.
5. what exception does json.load raise on broken JSON?
--> json.load raises json.JSONDecodeError (which is a subclass of ValueError).




# Day 14 - [06-09-2026]
**Branch:** day-14/comprehensions
# WARMUP
**Predictions before running:**
1. What does each line produce?
print([x * 2 for x in range(3)])   ----> [0, 2, 4]  ---> multiplies each number in 0, 1, 2 by 2
print({c: len(c) for c in ["aws", "gcp"]}) --->  {'aws': 3, 'gcp': 3}  --> creates a dictionary mapping each string to its length.
print([x for x in range(10) if x % 2 == 0]) ---> [0, 2, 4, 6, 8]  --> filters numbers from 0 to 9, keeping only even numbers




# Day 15 - [06-09-2026]
**Branch:** day-15/comprehensions
# WARMUP
**Predictions before running:**
1. What happens and why? What's the fix?
class Box:
    def __init__(self, size):
        size = size

b = Box("large")
print(b.size)
--> what happens??? --> It raises an AttributeError: 'Box' object has no attribute 'size'.
--> why??? ---> Inside __init__, size = size creates a local variable named size and assigns the argument to itself. It never attaches size to the instance object (self). Once __init__ finishes executing, that local size variable is destroyed, leaving the Box instance b with no size attribute attached.
--> Fix: Prefix size with self. so Python attaches it as an attribute to the instance:
class Box:
    def __init__(self, size):
        self.size = size  # Fix: attach to 'self'

b = Box("large")
print(b.size)  # Output: large

2. what does @dataclass auto-generate for you that you'd otherwise write manually?
--> When we apply @dataclass, Python automatically writes standard boilerplate methods behind the scenes based on our type annotations.

Here is what @dataclass auto-generates for us:

__init__(): Generates the constructor, accepts arguments for every defined field, and assigns them to instance variables (self.field = field).

__repr__(): Generates a clean, developer-friendly string representation (e.g., SandboxRequest(cloud='aws', resource='db', size='large', count=1)).

__eq__(): Generates equality comparison logic. It compares objects attribute-by-attribute (obj1 == obj2) rather than comparing memory addresses.

__ne__(): Generates "not equal" logic (obj1 != obj2).

Optional Ordering Methods (order=True): Generates rich comparison methods (__lt__, __le__, __gt__, __ge__) so we can sort instances by their fields.

Optional Immutability (frozen=True): Generates assignment blocks that block changes to attributes after instantiation (making instances hashable/read-only).

Comparison: Manual Class vs. @dataclass
Manual Class Boilerplate
Python
class SandboxRequest:
    def __init__(self, cloud: str, resource: str, size: str):
        self.cloud = cloud
        self.resource = resource
        self.size = size

    def __repr__(self):
        return f"SandboxRequest(cloud={self.cloud!r}, resource={self.resource!r}, size={self.size!r})"

    def __eq__(self, other):
        if not isinstance(other, SandboxRequest):
            return False
        return (self.cloud, self.resource, self.size) == (other.cloud, other.resource, other.size)
Equivalent @dataclass
Python
from dataclasses import dataclass

@dataclass
class SandboxRequest:
    cloud: str
    resource: str
    size: str
Both versions behave identically, but the @dataclass eliminates around 80% of the repetitive setup code while maintaining static type safety.




# Day 16 - [07-09-2026]
**Branch:** day-16/type-hints
# WARMUP
**Predictions before running:**
1. Both run identically at runtime. So why bother with the first form? Give two reasons.
def process(cloud: str) -> dict:
    ...

def process(cloud):
    ...
---> Type hints enable early bug detection via static analysis (mypy) and provide IDE auto-completion with self-documenting code.
