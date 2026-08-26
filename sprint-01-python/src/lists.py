# 1. Prove the aliasing trap — show it breaking, then show it fixed with one of your three methods
a = [1, 2, 3]
b = a
print(f"Memory address of a: {id(a)}")
print(f"Memory address of b: {id(b)}")
print(f"Are they the same object? {a is b}")  # returns true

#Modifying b affects a
b.append(4)
print(f"List 'a': {a}")
print(f"List 'b': {b}")

# Fixing it by addressing diff memory 
fix_b = a.copy()
print(f"Memory address of a: {id(a)}")
print(f"Memory address of fix_b {id(fix_b)}")
print(f"Are they the same object? {a is fix_b}")   # Returns false

fix_b.append(5)
print(f"List 'a': {a}")
print(f"List 'fix_b': {fix_b}")





# 2. Build a list of 5 cloud regions, append one, remove one, check membership with in
cloud_regions = ['us-east-1', 'us-west-2','eu-central-1', 'us-central1', 'eu-west-1']
cloud_regions.append('asia-east1')   # Append region  --> Adds 'asia-east1' to the end
cloud_regions.remove('eu-central-1')   # Remove region  --> Removes 'eu-central-1'

print(cloud_regions)

search_region = input("Enter region to search: ").strip().split()[0]    # Strip outer spaces and grab the first word typed
#check membership directly
if search_region in cloud_regions:
    print(f"{search_region}: Region Found.")
else:
    print(f"{search_region}: Region Not Found")


# 3. Slice the middle three items from a 5-item list
sliced_region = cloud_regions[1:4]    # Slice from index 1 up to (but not including) index 4 -> gets 1, 2, and 3..because in python lists, indices are zero based(0, 1, 2, 3, 4)
print(f"Sliced_regions: {sliced_region}")





# 4. This one is hard — given [19.99, 4.50, 120.0, 8.0], find the max without using max(). Then find the average. Loop only, no built-ins.
given_list = [19.99, 4.50, 120.0, 8.0]

# Initialize max with the first element of the list
curr_max = given_list[0]
count = 0
total_sum = 0

for item in given_list:
    count += 1
    total_sum += item
    
    if item > curr_max:
        curr_max = item

avg = total_sum/count

print(f"curr_max: {curr_max}")
print(f"avg: {avg}")
