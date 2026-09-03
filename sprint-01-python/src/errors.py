# 1. Exercise 1 — trigger each error deliberately, one snippet per error:
# For each one: write the code that causes it, run it, write in LOG the exact error name and one-sentence cause.
# NameError
# TypeError
# KeyError
# IndexError
# AttributeError
# ZeroDivisionError

# NameError
try:
    print(unsaid_var)
except NameError as e:
    Log = f"NameError: {e} - Tried to access a variable name that has not been defined in code."
    print(Log)
    
# 2. TypeError
try:
    result = "price: " + 100
except TypeError as e:
    LOG = f"TypeError: {e} - Attempted an operation (+ string and int) between incompatible data types."
    print(LOG)

# 3. KeyError
try:
    my_dict = {"cloud": "aws"}
    resource = my_dict["database"]
except KeyError as e:
    LOG = f"KeyError: {e} - Attempted to access a dictionary key that does not exist in the dictionary."
    print(LOG)

# 4. IndexError
try:
    clouds = ["aws", "azure"]
    third_cloud = clouds[5]
except IndexError as e:
    LOG = f"IndexError: {e} - Attempted to access a sequence or list position that is out of range."
    print(LOG)

# 5. AttributeError
try:
    number = 42
    number.lower()
except AttributeError as e:
    LOG = f"AttributeError: {e} - Attempted to call a method (.lower()) that does not exist on that object type (int)."
    print(LOG)

# 6. ZeroDivisionError
try:
    total = 100 / 0
except ZeroDivisionError as e:
    LOG = f"ZeroDivisionError: {e} - Attempted a division or modulo operation where the divisor was zero."
    print(LOG)
  
    
    
# 2. Exercise 2 — fix tip_calculator
# Copy your tip_calculator.py logic into this file and wrap the float(input(...)) calls in proper try/except ValueError so bad input prints a friendly message instead of crashing. Test with abc as input.

# 1. Take inputs from the user and convert strings to numbers
try:
    # 1. Prompt for inputs and convert to float
    bill_amount = float(input("Enter the total bill amount: $"))
    tip_percentage = float(input("Enter tip percentage (e.g., 15, 18, 20): "))

    # 2. Calculate tip and total amounts
    tip_amount = bill_amount * (tip_percentage / 100)
    total_bill = bill_amount + tip_amount

    # 3. Print the results (formatted to 2 decimal places)
    print("\n--- Summary ---")
    print(f"Tip Amount:      ${tip_amount:.2f}")
    print(f"Total Amount:    ${total_bill:.2f}")
except ValueError:
    print("\nInvalid input! Please enter valid numeric values for the bill and tip.") 
    
    

# 3. Exercise 3 — fix the empty input crash from lists.py
# Write a function safe_search(regions, query) that wraps the search in try/except and returns "no input provided" if query is empty.
def safe_search(regions, query):
    try:
        #check if query is empty or just whitespace
        if not query or not query.strip():
            return "no input provided"
        
        # Clean query and search list
        query_clean = query.lower().strip()
        
        for region in regions:
            if query_clean in region.lower():
                return f"Found: {region}"
        return "Region not found"
    
    except (AttributeError, TypeError):
        # Catches cases where query or regions are not strings/lists (e.g. None or int)
        return "no input provided"
    
# --- Test Cases ---
regions_list = ["us-east-1", "us-west-2", "eu-central-1", "ap-south-1"]

# 1. Empty string test
print(f"Empty input test:    {safe_search(regions_list, '')}")

# 2. Spaces-only input test
print(f"Spaces input test:   {safe_search(regions_list, '   ')}")

# 3. None value input test
print(f"None input test:     {safe_search(regions_list, None)}")

# 4. Valid search test
print(f"Valid search test:   {safe_search(regions_list, 'us-east')}")

# 5. Not found test
print(f"Not found test:      {safe_search(regions_list, 'sa-east-1')}")



# 4. Write validate_cloud(name) that raises ValueError("unknown cloud: {name}") if the name is not in ["aws", "azure", "gcp"]. Call it with a valid and invalid name. Catch the invalid one cleanly.
valid_clouds = ["aws", "azure", "gcp"]
def validate_cloud(name):
    # Guard against non-string inputs or None
    if not isinstance(name, str):
        raise ValueError(f"unknown cloud: {name}")
    
    normalized_name = name.lower().strip()
    
    if normalized_name not in valid_clouds:
        raise ValueError(f"unknown cloud: {name}")
    
    return normalized_name

# --- Test Executions ---

# 1. Calling with a valid name
try:
    valid_result = validate_cloud("AWS")
    print(f"Success: Validated '{valid_result}' successfully.")
except ValueError as e:
    print(f"Error: {e}")

# 2. Calling with an invalid name and catching it cleanly
try:
    invalid_result = validate_cloud("oracle")
    print(f"Success: Validated '{invalid_result}' successfully.")
except ValueError as e:
    print(f"Caught expected error cleanly -> {e}")
    
