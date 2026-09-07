# ==============================================================================
# EVOLUTIONARY ARCHITECTURE NOTES:
# 
# Exercise 1: Defined base SandboxRequest with typed fields and count default.
#   - description: str
#   - cloud: Literal["aws", "azure", "gcp"]
#   - size: str
#   - count: int = 1
#
# Exercise 2: Added Field boundary enforcement to prevent non-positive counts.
#   - count: int = Field(default=1, ge=1)
#
# Exercise 3: Added pre-validation normalization for raw input strings.
#   - @field_validator("cloud", mode="before") runs prior to Literal checking.
#
# Exercise 4: Added cross-field business logic validation.
#   - @model_validator(mode="after") enforces multi-field rule (large size <= 10).
# ==============================================================================

from typing import Literal
from pydantic import BaseModel, Field, ValidationError, field_validator, model_validator


# --- Unified Single Source of Truth ---
class SandboxRequest(BaseModel):
    # Exercise 1: Core fields & types
    description: str                              # String description of the sandbox
    cloud: Literal["aws", "azure", "gcp"]         # Restricts input to specific cloud providers
    size: str                                     # Size specification (e.g., 'small', 'medium', 'large')
    
    # Exercise 2: Field boundary enforcing count >= 1
    count: int = Field(default=1, ge=1)           # Number of sandboxes; defaults to 1, must be >= 1

    # Exercise 3: Input normalization field validator
    @field_validator("cloud", mode="before")
    @classmethod
    def normalize_cloud(cls, v: str) -> str:
        """Strips whitespace and converts cloud parameter to lowercase before Literal validation."""
        if isinstance(v, str):
            return v.strip().lower()              # Normalizes strings (e.g., '  AWS ' -> 'aws')
        return v

    # Exercise 4: Cross-field model validator
    @model_validator(mode="after")
    def check_large_limit(self) -> "SandboxRequest":
        """Rejects requests specifying 'large' size if count exceeds 10."""
        if self.size == "large" and self.count > 10:
            raise ValueError("large size cannot exceed count of 10")
        return self                               # Return the validated instance


# ==============================================================================
# COMPREHENSIVE TEST SUITE
# ==============================================================================

# --- Exercise 1 Tests: Base Functionality & Type Bounds ---
print("--- Exercise 1 Tests ---")
# Test 1.1: Valid input instantiation
valid_req = SandboxRequest(description="Dev Env", cloud="aws", size="medium", count=3)
print("Exercise 1 - Valid Input:", valid_req)

# Test 1.2: Invalid cloud provider ("oracle" is not in the Literal)
try:
    SandboxRequest(description="Dev Env", cloud="oracle", size="medium")
except ValidationError as e:
    print("\nExercise 1 - Invalid Cloud Caught:\n", e)

# Test 1.3: Invalid count type (non-numeric string)
try:
    SandboxRequest(description="Dev Env", cloud="aws", size="medium", count="three")
except ValidationError as e:
    print("\nExercise 1 - Invalid Count Type Caught:\n", e)


# --- Exercise 2 Tests: Field Boundary Constraints (ge=1) ---
print("\n--- Exercise 2 Tests ---")
# Test 2.1: Boundary count=1 (Valid)
pass_req = SandboxRequest(description="Test", cloud="gcp", size="small", count=1)
print("Exercise 2 - Boundary count=1 passed:", pass_req)

# Test 2.2: Boundary count=0 (Invalid)
try:
    SandboxRequest(description="Test", cloud="gcp", size="small", count=0)
except ValidationError as e:
    print("\nExercise 2 - Boundary count=0 failed as expected:\n", e)


# --- Exercise 3 Tests: Field Normalization (mode="before") ---
print("\n--- Exercise 3 Tests ---")
# Test 3.1: Uppercase input with leading/trailing whitespace
req1 = SandboxRequest(description="Test", cloud=" AWS ", size="small")
print("Exercise 3 - Normalized ' AWS ' ->", req1.cloud)

# Test 3.2: Mixed case with padding
req2 = SandboxRequest(description="Test", cloud=" Azure ", size="small")
print("Exercise 3 - Normalized ' Azure ' ->", req2.cloud)


# --- Exercise 4 Tests: Cross-Field Logic Enforcement ---
print("\n--- Exercise 4 Tests ---")
# Test 4.1: Valid large request (count <= 10)
valid_large = SandboxRequest(description="Big Cluster", cloud="aws", size="large", count=10)
print("Exercise 4 - Valid large request:", valid_large)

# Test 4.2: Invalid large request (count > 10)
try:
    SandboxRequest(description="Over-sized Cluster", cloud="aws", size="large", count=11)
except ValidationError as e:
    print("\nExercise 4 - Cross-field rule violation caught:\n", e)


# NOTE ON VALIDATOR SCOPE:
# @field_validator checks or transforms individual fields in isolation (e.g., string cleaning).
# @model_validator evaluates cross-field relationships across the whole model (e.g., size vs. count).