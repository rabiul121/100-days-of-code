# def add(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total
#
#
# print(add(1, 2, 3, 4, 5, 6, 7, 8, 9))
def calculate(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key, ":", value)
    # print(value)
    n = n + kwargs["a"] + kwargs["b"] + kwargs["c"]
    print(n)


calculate(2, a=1, b=2, c=3)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Ford", model="GT-9", color="Blue", seats=4)
print(my_car.make)
print(my_car.model)
print(my_car.color)
print(my_car.seats)
