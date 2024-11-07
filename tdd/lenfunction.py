def checklength(name):
    count = 0
    for length in name:
        count += 1
        length = str(length)
    return count


print(checklength("Ayinlade"))


def length(items):
    if type(items) in [int, float]:
        raise TypeError("items is not iterable")
    count = 0
    for length in items:
        count += 1
