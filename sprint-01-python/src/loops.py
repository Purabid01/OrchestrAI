# Day 8: Loops

# 1. FizzBuzz 1–20: print "Fizz" for multiples of 3, "Buzz" for multiples of 5, "FizzBuzz" for both

for i in range (1, 21):
    if (i%3 == 0) and (i%5==0):
        print(i , " --> FizzBuzz")    
    elif (i%3 == 0):
        print(i , " --> Fizz")
    elif (i % 5 == 0):
        print(i , " --> Buzz")
    else:
        print(f"the number itself --> {i}")
        
        
# 2. Sum numbers 1–100 using a loop. Then do it with sum(range(...)) in one line. Print both and confirm they match
my_sum = 0
for i in range(1, 101):
    my_sum += i
    
print(f"Sum is {my_sum}")

# one line using built-in func
print(sum(range(1, 101)))


# 3. Loop over ["aws", "azure", "gcp"] and print each with its index using enumerate
cloud = ["aws", "azure", "gcp"]
for i, v in enumerate(cloud):
    print(i, v)
    
# 4. Debug this - 
i = 0
while i < 5:
    print(i)
    i += 1
    
    
# 5.predict this and run
for i in range(2, 10, 3):
    print(i)
    