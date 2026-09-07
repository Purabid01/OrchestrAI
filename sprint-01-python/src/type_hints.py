# 1. Take your functions from previous days and add full type hints to all of them. Copy these signatures and add the hints:

# # 2. Use Optional and Literal where appropriate:
# cloud parameters should be Literal["aws", "azure", "gcp"]
# nullable returns should be str | None not just str

from typing import Callable, Literal, Optional

# Literal["aws", "azure", "gcp"]: Restricts valid strings to exactly those three choices. mypy and IDEs will raise an error if any other string (e.g., "digitalocean") is passed.
# Optional[CloudProvider] / str | None: Clearly communicates to callers that the function may return None, forcing defensive handling (if cloud is not None:) downstream.

# Reusable alias for strict cloud validation
CloudProvider = Literal["aws", "azure", "gcp"]


def normalize_cloud_optional(name: str) -> Optional[CloudProvider]:
    """Normalizes raw input strings into valid cloud providers or returns None."""
    cleaned = name.strip().lower()
    if cleaned in ("aws", "azure", "gcp"):
        return cleaned  # type: ignore[return-value] -- # mypy cannot narrow a dynamic string check ('in tuple') to Literal["aws", "azure", "gcp"]
    return None


def price_total(prices: list[float], tax: float) -> float:
    """Calculates total cost given price list and tax rate multiplier."""
    return sum(prices) * (1 + tax)


# dict[str, str | None]: Uses the union operator (|) to indicate that values in the dictionary can be either a string or None.
# -> None: Explicitly indicates that the function performs a side effect (like writing to a file) and does not return a value.
def parse_request(text: str) -> dict[str, str | None]:
    """Parses input string into key-value map with nullable values."""
    return {"cloud": text.strip().lower() if text else None}


def save_request(req: dict[str, str | None], filename: str) -> None:
    """Writes request configuration dictionary to disk."""
    with open(filename, "w") as f:
        f.write(str(req))


def load_catalog(filename: str) -> list[dict[str, str | float]]:
    """Loads resource catalog as a list of structured dictionaries."""
    return [{"resource": "database", "price": 100.0}]


def validate_cloud(name: str) -> CloudProvider:
    """Validates and narrows a raw string into a CloudProvider Literal type."""
    normalized = name.strip().lower()
    if normalized == "aws":
        return "aws"
    elif normalized == "azure":
        return "azure"
    elif normalized == "gcp":
        return "gcp"
    raise ValueError(
        f"Invalid cloud provider: '{name}'. Must be 'aws', 'azure', or 'gcp'."
    )


# 4. Hard: type a function that takes a callable as a parameter:
# from typing import Callable

# def apply_to_clouds(
#     clouds: list[str],
#     func: Callable[[str], str]
# ) -> list[str]:
#     return [func(c) for c in clouds]
# Call it with normalize_cloud as the argument. This is a higher-order function — a function that takes another function as input. You'll see this pattern in LangGraph nodes.


def normalize_cloud(name: str) -> str:
    """Normalizes cloud provider strings."""
    return name.strip().lower()


def apply_to_clouds(
    clouds: list[str], func: Callable[[str], str]
) -> list[str]:
    """Higher-order function that applies a string transformation to every cloud name."""
    return [func(c) for c in clouds]


# Execute the higher-order function passing 'normalize_cloud' as a callable argument
raw_clouds = ["  AWS ", " GCP", "AZURE  "]
cleaned_clouds = apply_to_clouds(raw_clouds, normalize_cloud)

print(cleaned_clouds)


# NOTE: Callable[[str], str] Syntax:
# The first argument inside brackets [str] defines the input parameter types expected by func.
# The second argument str defines the expected return type of func.
# Higher-Order Function Pattern: Because functions in Python are first-class objects, passing functions into other functions (func: Callable[...]) enables flexible execution patterns—the exact mechanism framework nodes (like LangGraph chains or processing pipelines) use to route and transform data dynamically.