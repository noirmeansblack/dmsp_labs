
def flatten_tuples(iterable):
    return sum(iterable, ())

def all_unique(iterable):
    seen = set()
    return not any(x in seen or seen.add(x) for x in iterable)
