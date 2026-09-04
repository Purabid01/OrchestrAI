# 1. Build a dict mapping cloud → default region. Look one up safely with .get() — no crash if missing
# Dict mapping cloud providers to default regions
cloud_regions = {
    "aws": "us-east-1",
    "azure": "eastus",
    "gcp": "us-central1"
}

# 1. Looking up an existing key safely
aws_region = cloud_regions.get("aws", "region-unknown")
print(f"AWS Region: {aws_region}")
# Output: AWS Region: us-east-1

# 2. Looking up a missing key safely (returns fallback, no KeyError/crash)
oracle_region = cloud_regions.get("oracle", "region-unknown")
print(f"Oracle Region: {oracle_region}")
# Output: Oracle Region: region-unknown


# 2. Given ["aws", "gcp", "aws", "azure", "gcp"], count occurrences of each cloud into a dict using a loop — no Counter, no imports
clouds = ["aws", "gcp", "aws", "azure", "gcp"]
counts = {}

for cloud in clouds:
    counts[cloud] = counts.get(cloud, 0) + 1
    
print(counts)


# 3. Invert a dict — swap keys and values. Given {"aws": "us-east-1", "gcp": "us-central1"}, produce {"us-east-1": "aws", "us-central1": "gcp"}
original = {"aws": "us-east-1", "gcp": "us-central1"}

# Swap value (v) to key, and key (k) to value
inverted = {}

for cloud, region in original.items():
    inverted[region] = cloud
    
print(inverted)




# 4. Loop over a dict with .items() and print "cloud -> region" for each pair
cloud_regions = {
    "aws": "us-east-1",
    "azure": "eastus",
    "gcp": "us-central1"
}

for cloud, region in cloud_regions.items():
    print(f"{cloud} -> {region}")