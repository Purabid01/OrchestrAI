# 1. Prove the mutable default trap — show it breaking, then fixed with None
def add_item(item, basket=[]):
    basket.append(item)
    return basket

print(add_item("a"))   
print(add_item("b"))

# fixed using None as default arg
def fixed_add_item(item, basket=None):
    if basket is None:
        basket = []   # Creates a brand new list everytime
    basket.append(item)
    return basket
print(fixed_add_item("aa"))
print(fixed_add_item("bb"))



# 2. Write normalize_cloud(name) — takes a cloud name, returns it lowercased and stripped
def normalize_cloud(name):
    return name.lower().strip()
print(normalize_cloud("AWS"))          
print(normalize_cloud("  GCP  "))      
print(normalize_cloud(" Azure \n"))   

# 3. Write price_total(prices, tax=0.0) — takes a list of prices and optional tax rate, returns total
def price_total(prices, tax=0.0):
    subtotal = sum(prices)
    total_with_tax = subtotal * (1 + tax)
    return total_with_tax

print(price_total([90, 10], 0.08))



# 4. Write parse_request(text) — takes a string like "I need a postgres db on aws", returns {"cloud": "aws", "resource": "postgres"} by searching for keywords. Crude string matching only — no LLM yet.
def parse_request(text):
    # Standardize inputs to lowercase for easy matching
    cloud = ['aws', 'azure', 'gcp']
    resources = ['postgres', 'sql']
    
    found_cloud = None
    found_resource = None
    
    # Standardize incoming text
    clean_text = text.lower()
    words = clean_text.split()
    
    # Search for cloud keywords
    for c in cloud:
        if c in words:
            found_cloud = c
            break
        
    # Search for resource keywords
    for r in resources:
        if r in words:
            found_resource = r
            break
        
    return {"cloud": found_cloud, "resource": found_resource}

print(parse_request("I need a postgres db on aws"))
print(parse_request("I need something on oracle"))
print(parse_request("I need mysql on aws"))
    
    