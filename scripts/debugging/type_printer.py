from io import TextIOWrapper


def traverse(f:TextIOWrapper, obj, indent=0):
    """Recursively traverse a nested Python structure and print types."""
    prefix = "  " * indent
    f.write(f"{prefix}{type(obj).__name__}: {repr(obj) if not isinstance(obj, (dict, list, tuple, set)) else ''} \n")

    if isinstance(obj, dict):
        for k, v in obj.items():
            f.write(f"{prefix}  Key ({type(k).__name__}): {repr(k)}\n")
            traverse(f,v, indent + 2)
    elif isinstance(obj, (list, tuple, set)):
        for i, item in enumerate(obj):
            f.write(f"{prefix}  Index {i}:\n")
            traverse(f, item, indent + 2)