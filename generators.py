# Generators

def even_numbers(max_number):
    numbers = []
    for number in range(max_number):
        if number % 2 == 0:
            numbers.append(number)

    return numbers


numbers = even_numbers(8)
# numbers = even_numbers(10000000000)
print(numbers)


def generator_even_numbers(max_number):
    for number in range(max_number):
        if number % 2 == 0:
            yield number


numbers = generator_even_numbers(8)
# numbers = generator_even_numbers(100000000000000)
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))

# for number in numbers:
#     print(number)

numbers = [x for x in range(8) if x % 2 == 0]  # non generator
print(numbers)
numbers = (x for x in range(8) if x % 2 == 0)  # generator

for number in numbers:
    print(number)
