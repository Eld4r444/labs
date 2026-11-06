def calculate_rectangle(width, height):
    return width * height


def calculate_perimeter(width, height):
    return 2 * (width + height)


def describe_rectangle(width, height, unit="см"):
    print(f"Прямоугольник {width} x {height} {unit}")


print(calculate_rectangle(5, 3))
print(calculate_perimeter(5, 3))
describe_rectangle(5, 3)
describe_rectangle(5, 3, "м")
