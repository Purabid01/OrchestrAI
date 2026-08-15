## Day 1 — 13-08-2026
**Branch:** day-01/toolchain-setup
**Commit:** b4fe472
**What I did: Today I setup my local env like install all the dependencies like puthon, git, uv and then and create and write readme and log.md file for summary**
**What broke or confused me:**
 I installed python latest version(3.14.4) but for this project with langraph kinda techstack python3.14.4 is too new.so I installed 3.12 alongside it 
**What I still don't understand:**
RESOLVED — venv isolates each project's packages so they don't 
conflict with each other or break system Python. Each project 
gets its own clean environment.





## Day 2 — 14-08-2026
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
