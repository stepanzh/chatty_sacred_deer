import random

class StopTalking(Exception):
    pass

def randcycle(iterable):
    """Returns randomized cycle generator.
    New element never equals to previous.
    """
    assert len(iterable) > 2, 'Length must be > 2, for 2-element iterable use itertools.cycle'

    iterable_closure = tuple(iterable)
    i = random.randint(0, len(iterable_closure)-1)
    yield iterable_closure[i]
    pi = i
    while True:
        i = random.randint(0, len(iterable_closure)-1)
        if i == pi:
            continue
        item = iterable_closure[i]
        pi = i
        yield item
