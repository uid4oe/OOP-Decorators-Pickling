from datetime import date
from random import randint


# input and type verifier decorator for Animal class
def input_verifier(*types):
    def wrapper(f):
        def verify(*values):
            # checks the total number of inputs
            if len(values) < 5:
                raise Exception("You must enter Gender, Birthday, Colour and Environment Conditions for new Animal"
                                "instantiation")

            if not (type(values[1]) is types[1] and type(values[2]) is types[2] and type(values[3]) is types[3]):
                raise Exception("Wrong input format for Animal class!")

            if values[2] is None:
                raise Exception("Wrong Date Format, retry.")

            # creates dictionary with the forced types
            mock = dict()
            mock["gender"] = values[1]
            mock["birth_day"] = values[2]
            mock["colour"] = values[3]

            if len(dict(values[4]).values()) < 4:
                raise Exception(
                    "You must enter Relative Humidity, Enclosure Size (m2), Temperature and Hours of light per day"
                    "for Environment Conditions")

            if not (type(values[4]["relative_humidity"]) is types[4][0] and type(values[4]["enclosure_size"]) is
                    types[4][
                        1] and type(
                        values[4]["temperature"]) is types[4][2] and type(values[4]["hours_of_light_per_day"]) is
                    types[4][
                        3]):
                raise Exception("Wrong input format for Environment Conditions in Animal class!")

            mock["environment_conditions"] = dict()
            mock["environment_conditions"]["relative_humidity"] = values[4]["relative_humidity"]
            mock["environment_conditions"]["enclosure_size"] = values[4]["enclosure_size"]
            mock["environment_conditions"]["temperature"] = values[4]["temperature"]
            mock["environment_conditions"]["hours_of_light_per_day"] = values[4]["hours_of_light_per_day"]

            return f(values[0], mock)

        return verify

    return wrapper


class Animal:
    animal_list = dict()

    __slots__ = ["no", "gender", "birth_day", "colour", "environment_conditions", "feeding_record",
                 "observation_record"]

    @input_verifier(object, str, date, str, [int, int, int, int])
    def __init__(self, verified_input):
        animal_no = randint(1000, 9999)
        while animal_no in Animal.animal_list:
            animal_no = randint(1000, 9999)

        self.no = animal_no
        self.gender = verified_input["gender"]
        self.birth_day = verified_input["birth_day"]
        self.colour = verified_input["colour"]
        self.environment_conditions = verified_input["environment_conditions"]
        self.feeding_record = list()
        self.observation_record = list()

        Animal.animal_list[self.no] = self

    def __str__(self):
        return f"No: {self.no} - Gender: {self.gender} - Birthday: {self.birth_day} - Colour: {self.colour}"

    def details_between_dates(self, for_print, operation_type, start_date, end_date):
        if operation_type == "observation":
            list_type = self.observation_record
        elif operation_type == "feeding":
            list_type = self.feeding_record
        else:
            raise Exception("Wrong Operation Type!")

        result = [item for item in list_type if start_date <= item.date <= end_date]
        if for_print:
            [print(item) for item in result]
        else:
            return len(result)

    def foods_fed(self):
        unique_foods = set()
        [unique_foods.add(record.food) for record in self.feeding_record]
        [print(food) for food in unique_foods]

    def staff_who_observed(self):
        unique_staff = set()
        [unique_staff.add(record.staff) for record in self.observation_record]
        [print(staff) for staff in unique_staff]


def get_animal(value):
    value = int(value)
    if value not in Animal.animal_list.keys():
        raise Exception("Animal NO not found, check input")
    return Animal.animal_list[value]
