from collections.abc import MutableSequence


class Mutable_String(MutableSequence):
    def __init__(self, initial_string=""):
        self.string = list(initial_string)

    def __getitem__(self, index):
        return self.string[index]

    def __setitem__(self, index, value):
        self.string[index] = value

    def __str__(self):
        return "".join(self.string)

    def __len__(self):
        return len(self.string)

    def __iter__(self):
        return iter(self.string)

    def __repr__(self):
        return repr("".join(self.string))

    def __add__(self, string):
        if not isinstance(string, str):
            raise TypeError("input data must be a string")
        return Mutable_String(self.string + string)

    def title(self):
        return Mutable_String(''.join(self.string).title())

    def capitalize(self):
        return Mutable_String(''.join(self.string).capitalize())

    def center(self, width, fill=None):
        return Mutable_String(''.join(self.string).center(width, fill))

    def upper(self):
        return Mutable_String(''.join(self.string).upper())

    def lower(self):
        return Mutable_String(''.join(self.string).lower())

    def startswith(self, string):
        return ''.join(self.string).startswith(string)

    def endswith(self, string):
        return ''.join(self.string).endswith(string)

    def find(self, string, start=None, end=None):
        return ''.join(self.string).find(string, start, end)

    def rfind(self, s, start=None, end=None):
        return ''.join(self.string).rfind(s, start, end)

    def index(self, string, start=None, end=None):
        return ''.join(self.string).index(string, start, end)

    def rindex(self, string, start=None, end=None):
        return ''.join(self.string).rindex(string, start, end)

    def split(self, symbol):
        return Mutable_String(''.join(self.string).split(symbol))

    def replace(self, old, new):
        return Mutable_String(''.join(self.string).replace(old, new))

    def rreplace(self, old, new):
        return Mutable_String(''.join(self.string).rreplace(old, new))

    def isdigit(self):
        return ''.join(self.string).isdigit()

    def isalpha(self):
        return ''.join(self.string).isalpha()

    def isalnum(self):
        return ''.join(self.string).isalnum()

    def islower(self):
        return ''.join(self.string).islower()

    def isupper(self):
        return ''.join(self.string).isupper()

    def isspace(self):
        return ''.join(self.string).isspace()

    def istitle(self):
        return ''.join(self.string).istitle()

    def join(self, array):
        return Mutable_String(''.join(self.string).join(array))

    def format(self, *args, **kwargs):
        return Mutable_String(''.join(self.string).format(*args, **kwargs))

    def ord(self, c):
        return ord(c)

    def chr(self, d):
        return chr(d)

    def count(self, string, start=None, end=None):
        return ''.join(self)