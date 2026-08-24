# Day 7: booleans, control flow, and the or-string bug

# --- Bool warmup: truthiness in Python ---
print(bool(""))    # False - empty string is falsy
print(bool("0"))   # True  - non-empty string is truthy
print(bool([]))    # False - empty list is falsy
print(bool([0]))   # True  - non-empty list is truthy even if contains 0
print(bool(None))  # False - None is always falsy


# size_check.py — read a number of GB, print "small" under 10, "medium" 10–100, "large" over 100
infra_size = float(input("Type the infra size (in GB): "))

if infra_size < 10:
    print("Small")
elif infra_size <= 100:
    print("Medium")
else:
    print("Large")
    
    
# 2. Fix this bug before running it — tell me what's wrong first:
cloud = "gcp"
# if there is no else condition
if cloud in ("aws", "gcp"): 
    print("Matched")
# if there is else condition - use a single-line ternary expression (X if condition else Y)
print("Matched" if cloud in ("aws", "gcp") else "Mismatched")
