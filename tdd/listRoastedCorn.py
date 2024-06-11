import random
def create_list(element):
    random.seed(5)
    figures = []
    for number in range(10):
        numbers = random.randint(1, 50)
        figures.append(numbers)
    return figures


print(create_list(random.seed()))

def lengthoflist(element):
    count = 0
    for letter in range(10):
        count += 1
    return count


print(lengthoflist(f'{random.seed()}'))

def even_elements_in_list(element):
    random.seed(5)
    figure = []
    sumup = 0
    for number in range(10):
        numbers = random.randint(1, 50)
        if numbers % 2 == 0:
            figure.append(numbers)
    for addup in figure:
        sumup += int(addup)
    return sumup


print(even_elements_in_list(f'{random.seed()}'))


def odd_elements_in_list(element):
    random.seed(5)
    figure = []
    total = 0
    for number in range(10):
        numbers = random.randint(1, 50)
        if numbers % 2 == 1:
            figure.append(numbers)
    for sumup in figure:
        total += int(sumup)
    return total


print(odd_elements_in_list(f'{random.seed()}'))


def multiply_elements_in_list(element):
    random.seed(5)
    figure = []
    for number in range(10):
        numbers = random.randint(1, 50)




def average_elements_in_list(elements):
    figure = []
    random.seed(5)
    average = 0
    for element in range(10):
        numbers = random.randint(1, 50)
        figure.append(numbers)
    for iteration in figure:
        average += int(iteration) / 10
    return average


print(average_elements_in_list(f'{random.seed()}'))


def largest_elements_in_list(elements):
    random.seed(5)
    figure = []
    largest = 0
    for number in range(10):
        ranges = random.randint(1, 50)
        figure.append(ranges)
        if ranges > largest:
            largest = ranges
    return largest


print(largest_elements_in_list(f'{random.seed()}'))

def smallest_elements_in_list(elements):
    random.seed(5)
    figure = []
    smallest = 0
    for number in range(10):
        ranges = random.randint(1, 50)
        figure.append(ranges)
        if ranges < smallest:
            ranges = smallest
    return smallest


print(smallest_elements_in_list(f'{random.seed()}'))

def create_tuple():
    new_tuple = ()


print(create_tuple())


def add_elements_to_tuple():
    new_tuple = ()
    for number in range(1, 21):
        lists = list(new_tuple)
        lists.append(number)
        new_tuple = tuple(lists)
    return new_tuple


print(add_elements_to_tuple())


def sum_elements_at_oddpositions_in_tuple():
    new_tuple = ()
    sums = 0
    for number in range(1, 21, 2):
        lists = list(new_tuple)
        lists.append(number)
        new_tuple = tuple(lists)
    for element in new_tuple:
        sums += int(element)
    return sums


print(sum_elements_at_oddpositions_in_tuple())


def sum_elements_at_evenpositions_in_tuple():
    new_tuple = ()
    sumup = 0
    for number in range(0, 21, 2):
        lists = list(new_tuple)
        lists.append(number)
        new_tuple = tuple(lists)
    for element in new_tuple:
        sumup += int(element)
    return sumup


print(sum_elements_at_evenpositions_in_tuple())


def sum_highest_and_smallest_elements_in_tuple():
    new_tuple = ()
    highest = 0
    smallest = 0
    for number in range(1, 21):
        lists = list(new_tuple)
        lists.append(number)
        new_tuple = tuple(lists)
    for iterable in new_tuple:
        if iterable > highest:
            highest = iterable
        if iterable < smallest:
            smallest = iterable
    return highest, smallest


print(sum_highest_and_smallest_elements_in_tuple())


def unpack_first_five_elements_in_tuple():
    new_tuple = ()
    for number in range(1, 21):
        lists = list(new_tuple)
        lists.append(number)
        new_tuple = tuple(lists)
    red, blue, pink, yellow, coy, *ink = new_tuple
    return red, blue, pink, yellow, coy


print(unpack_first_five_elements_in_tuple())


def create_dictionary():
    new_dictionary = {}


print(create_dictionary())

def populate_dictionary():
    student_list = {
        'Bola Ige': 15,
        'Esther Chukwu': 20,
        'Ade Badmus': 23,
        'Smart Uzor': 18,
        'David Adeleye': 22,
        'Alonge Stella': 21,
        'Bisola Mariam': 19,
        'Francis kennedy': 17,
        'Mba Chineye': 18,
        'Victor Ikpeba': 22,
    }
    for names in student_list:
        return student_list


print(populate_dictionary())


def sort_dictionary_by_key():
    student_list = {
        'Bola Ige': 15,
        'Esther Chukwu': 20,
        'Ade Badmus': 23,
        'Smart Uzor': 18,
        'David Adeleye': 24,
        'Alonge Stella': 21,
        'Bisola Mariam': 19,
        'Francis kennedy': 17,
        'Mba Chineye': 18,
        'Victor Ikpeba': 22,
    }
    for key, value in student_list.items():
        return key


print(sort_dictionary_by_key())


def sort_dictionary_by_value():
    student_list = {
        'Bola Ige': 15,
        'Esther Chukwu': 20,
        'Ade Badmus': 23,
        'Smart Uzor': 18,
        'David Adeleye': 22,
        'Alonge Stella': 21,
        'Bisola Mariam': 19,
        'Francis kennedy': 17,
        'Mba Chineye': 18,
        'Victor Nnneka': 22,
    }
    for key, value in student_list.items():
        print(value)


print(sort_dictionary_by_value())