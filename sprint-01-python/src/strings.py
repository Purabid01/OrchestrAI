# 1. Given "  AWS , Azure ,GCP  " — produce ["aws", "azure", "gcp"]. Do it step by step, print after each step

# repr() shows surrounding quotes so we can see whitespace clearly
cloud = "  AWS , Azure ,GCP  "
print(f"Original: {repr(cloud)}")

# step 1: remove leading/trailing spaces from the whole string
step1 = cloud.strip()
print(f"Step 1 (strip): {repr(step1)}")

# Step 2: Convert the entire string to lowercase
step2 = step1.lower()
print(f"step 2 (lower): {repr(step2)}")

# Step 3: Split the string by comma ',' into a list
step3 = step2.split(',')
print(f"Step 3 (split_by_comma) {step3}")

# Step 4: Strip remaining spaces around each individual item using a list comprehension
step4 = [item.strip() for item in step3]
print(f"Step 4 (clean list): {step4}")


### one line solution
result = [item.strip().lower() for item in cloud.split(',')]
print(result)





# 2. Take a full name as input, print initials — "Ada Lovelace" → "A.L."
# step 1: take the user input
full_name = input("Type your name: ")

#step 2: Split the name into words
words = full_name.split()
print(f"After splitting the name into words: {words}")

#Step 3: Get the first letter of each word and convert into uppercase
initials_list = [word[0].upper() for word in words]
print(f"First upprr letter of each word {initials_list}")

#Step 4: Join the letters together with a dot
final_initials = ".".join(initials_list)
print(f"Initials: {final_initials}.")



#3. Reverse a string using slicing only — one line
name = input("Enter a string to reverse: ")
print(name[::-1])



