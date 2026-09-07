# 1. Write a SandboxRequest class with __init__ storing cloud, resource, size and a summary() method returning a formatted string. Make one and print its summary.

class sandboxRequest:
    def __init__(self, cloud: str, resource: str, size: str):
        self.cloud = cloud
        self.resource = resource
        self.size = size       
        
    def summary(self) -> str:
        return f"SandboxRequest -> Cloud: {self.cloud.upper()} | Resource: {self.resource} | Size: {self.size}" 
     
# Instantiate and call summary()
req = sandboxRequest(cloud="aws", resource="database", size="large")
print(req.summary())




# 2. Rewrite it as a @dataclass. Notice how much boilerplate disappears.
from dataclasses import dataclass

@dataclass
class SandboxRequest:
    cloud: str
    resource: str
    size: str

    def summary(self) -> str:
        return f"SandboxRequest -> Cloud: {self.cloud.upper()} | Resource: {self.resource} | Size: {self.size}"
    
# Instantiate and call summary()
req = SandboxRequest(cloud="aws", resource="database", size="large")
print(req.summary())



# 3. Add to the dataclass:
# is_large() method returning True if size is "large"
# __repr__ so printing the object is readable
# A field count: int = 1 with validation that rejects values below 1
from dataclasses import dataclass

@dataclass
class SandboxRequest:
    cloud: str
    resource: str
    size: str
    count: int = 1  # Default value specified

    def __post_init__(self):
        # Defensive validation after dataclass auto-generates __init__
        if self.count < 1:
            raise ValueError(f"count must be at least 1, got {self.count}")

    def is_large(self) -> bool:
        return self.size.lower() == "large"

    def __repr__(self) -> str:
        return f"SandboxRequest(cloud='{self.cloud}', resource='{self.resource}', size='{self.size}', count={self.count})"


# 1. Normal usage
req = SandboxRequest(cloud="aws", resource="database", size="large", count=2)
print(req)             # Uses custom __repr__
print(req.is_large())  # Output: True

# 2. Validation check (raises ValueError)
try:
    invalid_req = SandboxRequest(cloud="gcp", resource="cache", size="small", count=0)
except ValueError as e:
    print(f"Validation Error: {e}")
    
    
    
    
# 4. Hard: add a class-level counter that increments each time a new instance is created. Print how many requests exist after making three instances.
from dataclasses import dataclass, field
from typing import ClassVar

@dataclass
class SandboxRequest:
    # Class-level counter (not an instance field)
    total_requests: ClassVar[int] = 0

    cloud: str
    resource: str
    size: str
    count: int = 1

    def __post_init__(self):
        # Defensive validation
        if self.count < 1:
            raise ValueError(f"count must be at least 1, got {self.count}")
        
        # Increment the class-level counter upon each successful instantiation
        SandboxRequest.total_requests += 1

    def is_large(self) -> bool:
        return self.size.lower() == "large"

    def __repr__(self) -> str:
        return f"SandboxRequest(cloud='{self.cloud}', resource='{self.resource}', size='{self.size}', count={self.count})"


# Create three instances
req1 = SandboxRequest("aws", "database", "large")
req2 = SandboxRequest("gcp", "cache", "small")
req3 = SandboxRequest("azure", "vm", "medium")

# Print class-level total
print(f"Total requests created: {SandboxRequest.total_requests}")