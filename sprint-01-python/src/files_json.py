# 1. Write a list of dicts to catalog.json using json.dump. Read it back with json.load and print it.
import json
import os

catalog = [
    {"name": "postgres", "cloud": "aws", "price": 49.99},
    {"name": "redis", "cloud": "azure", "price": 29.99},
    {"name": "mongodb", "cloud": "gcp", "price": 39.99}
]

# 1. Write the list of dicts to catalog.json
with open("catalog.json", "w") as f:
    json.dump(catalog, f, indent=4)
    
# 2. Read the data back from catalog.json
with open("catalog.json", "r") as f:
    loaded_catalog = json.load(f)
    
print(loaded_catalog)



# 2. Write save_request(req: dict) that appends a request to a JSON file — read existing list, append, write back.
def save_request(req: dict, filename: str = "requests.json"):
    # Defensive check: ensure input is a dictionary
    if not isinstance(req, dict):
        raise TypeError(f"Expected dict for req, got {type(req).__name__}")

    # Step 1: Read existing data safely
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            # Ensure the root structure is a list
            if not isinstance(data, list):
                data = []
    except (FileNotFoundError, json.JSONDecodeError):
        # Default to an empty list if file doesn't exist or is empty/corrupt
        data = []

    # Step 2: Append the new request
    data.append(req)

    # Step 3: Write the updated list back to disk
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
# Clean up before testing
if os.path.exists("requests.json"):
    os.remove("requests.json")
    
# --- Test Execution ---
new_req = {"endpoint": "/api/v1/deploy", "status": 200, "cloud": "aws"}
# Save first request
save_request(new_req)
# Save second request
save_request({"endpoint": "/api/v1/metrics", "status": 404, "cloud": "gcp"})
# Verify content by reading back
with open("requests.json", "r") as f:
    print(f.read())
    
    
    
# 3. Write load_catalog() that reads catalog.json and returns [] if the file doesn't exist — no crash.
def load_catalog(filename: str = "catalog.json") -> list:
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            # Ensure the returned structure is always a list
            return data if isinstance(data, list) else []
            
    except (FileNotFoundError, json.JSONDecodeError):
        # File doesn't exist, or is empty/corrupt -> return empty list safely
        return []


# --- Test Executions ---
# 1. Non-existent file (returns [] cleanly without crashing)
catalog = load_catalog("non_existent_file.json")
print("Missing file result:", catalog)
# Output: Missing file result: []
# 2. Existing file test
with open("catalog.json", "w") as f:
    json.dump([{"name": "postgres", "cloud": "aws"}], f)

catalog = load_catalog("catalog.json")
print("Existing file result:", catalog)



# 4. Hard: read a JSON file that contains deliberately broken JSON. Handle it gracefully with the correct exception — don't crash, return [] and print a warning.
def load_broken_json(filename: str = "broken_data.json") -> list:
    try:
        with open(filename, "r") as f:
            return json.load(f)
            
    except FileNotFoundError:
        print(f"Warning: File '{filename}' not found. Returning empty list.")
        return []
        
    except json.JSONDecodeError as e:
        # Catches syntax errors (missing commas, quotes, unclosed brackets, etc.)
        print(f"Warning: File '{filename}' contains invalid JSON syntax ({e.msg} at line {e.lineno}, column {e.colno}). Returning empty list.")
        return []


# --- Setup & Test ---

# 1. Create a file with deliberately broken JSON (missing closing bracket & invalid quote)
broken_content = """
[
    {"name": "postgres", "cloud": "aws"},
    {"name": "redis", "cloud": "azure"
]
"""

with open("broken_data.json", "w") as f:
    f.write(broken_content)

# 2. Execute function safely
data = load_broken_json("broken_data.json")

print("Returned data:", data)




