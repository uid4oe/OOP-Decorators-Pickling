from datetime import time, date

from Classes.Food import Food
from Classes.Staff import Staff


# input and type verifier decorator for Feeding Record class
def input_verifier(*types):
    def wrapper(f):
        def verify(*values):
            # checks the total number of inputs
            if len(values) < 6:
                raise Exception("You must enter Date, Time, Food, Weight and Staff for new Feeding Record"
                                "instantiation")

            if not (type(values[1]) is types[1] and type(values[2]) is types[2] and type(values[3]) is
                    types[3] and type(values[4]) is types[4] and type(values[5]) is types[5]):
                raise Exception("Wrong input format for Feeding Record class!")

            if values[1] is None:
                raise Exception("Wrong Date Format, retry.")

            # creates dictionary with the forced types
            mock = dict()
            mock["date"] = values[1]
            mock["time"] = values[2]
            mock["food"] = values[3]
            mock["weight"] = values[4]
            mock["staff"] = values[5]

            return f(values[0], mock)

        return verify

    return wrapper


class FeedingRecord:
    __slots__ = ["date", "time", "food", "weight", "staff"]

    @input_verifier(object, date, time, Food, int, Staff)
    def __init__(self, verified_input):
        self.date = verified_input["date"]
        self.time = verified_input["time"]
        self.food = verified_input["food"]
        self.weight = verified_input["weight"]
        self.staff = verified_input["staff"]

    def __str__(self):
        return f"Date: {self.date} - Time: {self.time} - Food Name: {self.food.name} " \
               f"- Manufacturer: {self.food.manufacturer} - Weight: {self.weight} - " \
               f"Staff: {self.staff.first_name + ' ' + self.staff.last_name}"
