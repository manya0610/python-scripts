"""
print supports writing to file, but sometimes we can't go and change all print statements.
this fixes it by using context manager
"""




import inspect
from functools import partial


class FilePrinter:
    def __init__(self, filename):
        self.filename = filename
    def __enter__(self):
        print("entered")
        self.old_print = inspect.builtins.print
        self.f = open(self.filename, "w")
        globals()["print"] = partial(inspect.builtins.print, file=self.f)
        print(print)
    
    def __exit__(self, *_):
        globals()["print"] = self.old_print
        self.f.close()
    

if __name__ == "__main__":
    with FilePrinter("test.log"):
        print("here we go, logged to file")

    print("this is not logged to file")