def merge(*lists):
    return sorted([item for sublist in lists for item in sublist])