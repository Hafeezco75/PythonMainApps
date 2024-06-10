import random

def createlist():
    figures = []
    for number in range(random.randint(1, 50)):
        figures.append(number)
        return figures

print(createlist())

def lengthoflist(elements):
    count = 0
    for letter in elements:
        count += 1
    return count


print(lengthoflist("Sabinus"))

def even_elements_in_list():
    sumup = 0
    figure = []
    for number in figure:
        if figure[number] % 2 == 0:
            figure.append(number)
            sumup += figure[number]
            return figure


print(even_elements_in_list())


def odd_elements_in_list():
    total = 0
    figures = []
    for number in figures:
        if figures[number] % 2 == 1:
            figures.append(number)
            total += figures[number]
            return figures


print(odd_elements_in_list())

def average_elements_in_list():
    listing = []
    for number in listing:
        listing.append(number)
        average = listing[number] / 10
        return average


print(average_elements_in_list())






