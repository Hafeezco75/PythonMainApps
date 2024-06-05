tuples = (1, 3, "ojo", [])
tuples[3].extend([1, 3, "kent"])
tupless = tuples + (1, 6)
tupless += (1, 6)

print(tuples)

print((tuples[1]))

print(tupless)

names = ["afeez", "eniola", "janet"]
names += tuples
names = tuple(names)

print(names)

print(names.count(1))
print(names.index("afeez", 0,4))
