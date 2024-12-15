#Python does not directly work with Union as C++ does

from typing import Union

# Define a function that accepts a union type
def process_value(value: Union[int, str, float]) -> str:
    """Processes a value that can be of multiple types."""
    if isinstance(value, int):
        return f"Integer processed: {value * 2}"
    elif isinstance(value, str):
        return f"String processed: {value.upper()}"
    elif isinstance(value, float):
        return f"Float processed: {value + 0.5}"
    else:
        raise ValueError(f"Unsupported type: {type(value)}")

# Example usage
values = [42, "hello", 3.14]

for val in values:
    print(process_value(val))
