# input and type verifier decorative for Food class
def input_verifier(*types):
    def wrapper(f):
        def verify(*values):
            # checks the total number of inputs
            if len(values) < 3:
                raise Exception("You must enter Name and Manufacturer for new Food instantiation")

            # checks input types
            if not (type(values[1]) is types[1] and type(values[2]) is types[2]):
                raise Exception("Wrong input format for Food class!")

            # creates dictionary with the forced types
            mock = dict()
            mock["name"] = values[1]
            mock["manufacturer"] = values[2]

            return f(values[0], mock)

        return verify

    return wrapper


class Food:
    food_list = dict()

    __slots__ = ["name", "manufacturer"]

    @input_verifier(object, str, str)
    def __init__(self, verified_input):
        self.name = verified_input["name"]
        self.manufacturer = verified_input["manufacturer"]
        Food.food_list[self.name + self.manufacturer] = self

    def __str__(self):
        return f"Food Name: {self.name} - Manufacturer: {self.manufacturer}"


def get_food(value):
    value = str(value)
    if value not in Food.food_list:
        raise Exception("Food not found, check input")
    return Food.food_list[value]
