def traverse(obj, indent=0, file = None):
    """Recursively traverse a nested Python structure and print types."""

    prefix = "  " * indent
    print(f"{prefix}{type(obj).__name__}: {repr(obj) if not isinstance(obj, (dict, list, tuple, set)) else ''} \n", file=file)

    if isinstance(obj, dict):
        for k, v in obj.items():
            print(f"{prefix}  Key ({type(k).__name__}): {repr(k)}\n", file=file)
            traverse(v, indent + 2, file)
    elif isinstance(obj, (list, tuple, set)):
        for i, item in enumerate(obj):
            print(f"{prefix}  Index {i}:\n", file=file)
            traverse(item, indent + 2, file)




if __name__ == "__main__":
    myobject = {
        "123" : ["123", 12, print],
        45: {
            56: ["!23"]
        }
    }
    with open("test.log", "w") as f:
        traverse(myobject, file=f)