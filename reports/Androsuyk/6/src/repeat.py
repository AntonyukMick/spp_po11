def repeat(pattern, repeat):
    if pattern is None:
        raise TypeError("pattern cannot be None")
    if not isinstance(repeat, int):
        raise TypeError("repeat must be an integer")
    if repeat < 0:
        raise ValueError("repeat must be non-negative")
    return pattern * repeat
