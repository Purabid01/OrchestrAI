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


## Day 5 - [17-08-2026]
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