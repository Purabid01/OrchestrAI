# size_check — read a number of GB, print "small" under 10, "medium" 10–100, "large" over 100

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
 