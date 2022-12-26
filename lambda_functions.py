# lambda

from functools import reduce


def area(width, length):
    return width * length


lambda_area = lambda width, length: width * length


print("normal area function:", area(4, 5))
print("lambda area function:", lambda_area(4, 5))


print("normal area function name: ", area.__name__)
print("lambda area function name: ", lambda_area.__name__)

# map(), filter(), reduce()
miles = [5, 7, 3, 8, 2, 9, 10]

# map()
kilometers = list(map(lambda mile: mile * 1.61, miles))
print("Miles to kilomteters using map(): ", kilometers)

# filter()
even_miles = list(filter(lambda mile: mile % 2 == 0, miles))
print("Even miles: ", even_miles)

# reduce()
maximum_mile = reduce(
    lambda mile_1, mile_2: mile_1 if mile_1 > mile_2 else mile_2, miles)
print("Maximum Mile: ", maximum_mile)
