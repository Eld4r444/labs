def greet(name):
    print(f"Здравствуйте, {name}!")


def square(number):
    return number ** 2


def max_of_two(a, b):
    if a > b:
        return a
    return b


greet("Иван")
greet("Мария")
print(square(5))
print(square(-3))
print(max_of_two(7, 12))
print(max_of_two(9.5, 3.2))
