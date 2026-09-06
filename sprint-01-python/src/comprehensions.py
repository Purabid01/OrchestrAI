# 1. Rewrite this loop as a one-line comprehension:
result = []
for cloud in ["AWS", " Azure ", "GCP "]:
    result.append(cloud.strip().lower())

print(result)

# one line comprehension
print([cloud.strip().lower() for cloud in ["AWS", " Azure ", "GCP "]]) 



# 2. From [19.99, 4.50, 120.0, 8.0] — build a list of prices over 10 using a comprehension
prices = [19.99, 4.50, 120.0, 8.0]
print([p for p in prices if p > 10])


# 3. Build a dict comprehension mapping each cloud to its character count: {"aws": 3, "azure": 5, "gcp": 3}
print({c.strip().lower(): len(c.strip()) for c in ["AWS", " Azure ", "GCP "]})


# 4. Hard: given a list of request dicts, extract names where cloud is "aws":
requests = [
    {"name": "db1", "cloud": "aws"},
    {"name": "cache1", "cloud": "gcp"},
    {"name": "db2", "cloud": "aws"}
]

print([req["name"] for req in requests if req["cloud"] == "aws"])