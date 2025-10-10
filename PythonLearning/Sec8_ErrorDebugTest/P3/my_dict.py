class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__ == "__main__":
    my_dict = Dict(a=1,b=5)
    print(my_dict.a)
    print(my_dict['a'])

    dict_python = dict(a=1,b=2)
    print(dict_python.a)
    print(dict_python['a'])