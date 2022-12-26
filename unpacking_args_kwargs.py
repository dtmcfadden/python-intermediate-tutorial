# Unpacking, *args + **kwargs

movies = ["Shrek", "Home Alone", "The Lion King", "Toy Story"]

# movie_1 = movies[0] # Shrek
# movie_2 = movies[1]
# movie_3 = movies[2]
# movie_4 = movies[3] # Toy Story

# movie_1, movie_2, movie_3, movie_4 = movies
# movie_1, movie_2, *disney_movies = movies
# *a_bunch_of_movies, last_movie = movies
# first_movie, *a_bunch_of_movies, last_movie = movies
# first_movie, *_, last_movie = movies

# # print(movie_1)
# # print(movie_2)
# # print(disney_movies)
# # print(movie_3)
# print(first_movie)
# # print(a_bunch_of_movies)
# print(last_movie)


# def some_func(number_1, number_2):
#     print("number_1:", number_1)
#     print("number_2:", number_2)


# # Positional Argument
# some_func(1, 2)

# # Keyword Argument
# some_func(number_1=4, number_2=5)
# some_func(number_2=100, number_1=200)


def average(numbers):
    total = sum(numbers)

    return total / len(numbers)


numbers = [1, 2, 3, 4, 5]
print(average(numbers))


# *args
def new_average(*args):
    total = sum(args)
    print("type args is:", type(args))

    return total / len(args)


# print(new_average(1, 2, 3, 4, 5, 6, 7, 8))

def concatenate(word_1, word_2, word_3):
    print(f"{word_1} {word_2} {word_3}")


concatenate(word_2="Cat", word_1="Hello", word_3="ball")


def new_concatenate(**kwargs):
    # print(kwargs)
    # print(type(kwargs))
    sentence = ""
    for word in kwargs.values():
        sentence += word + " "
    print(sentence)


new_concatenate(word_1="Bob", word_2="says", word_3="hello")
