from random import randint
from re import match


# input and type verifier decorator for Staff class
def input_verifier(*types):
    def wrapper(f):
        def verify(*values):
            # checks the total number of inputs
            if len(values) < 5:
                raise Exception("You must enter First Name, Last Name, Office and Tel for new Staff instantiation")

            # checks input types
            if not (type(values[1]) is types[1] and type(values[2]) is types[2] and type(values[3]) is types[3] and
                    type(values[4]) is types[4]):
                raise Exception("Wrong input format for Staff class!")

            # creates dictionary with the forced types
            mock = dict()
            mock["first_name"] = values[1]
            mock["last_name"] = values[2]
            mock["office"] = values[3]
            mock["tel"] = values[4]

            # verifies office input format, checks whether it starts with "A-" and followed by 3 digits
            if match(r"^A-\d{3}$", mock["office"]) is None:
                raise Exception("Wrong Office Format, It must have the format [A-XXX]")

            # verifies tel input format, checks whether it has only 4 digits
            if match(r"^\d{4}$", mock["tel"]) is None:
                raise Exception("Wrong Tel Format, It must has 4 digits")

            return f(values[0], mock)

        return verify

    return wrapper


class Staff:
    staff_list = dict()

    __slots__ = ["id", "first_name", "last_name", "office", "tel"]

    @input_verifier(object, str, str, str, str)
    def __init__(self, verified_input):
        staff_id = randint(100000, 999999)
        while staff_id in Staff.staff_list:
            staff_id = randint(100000, 999999)

        self.id = staff_id
        self.first_name = verified_input["first_name"]
        self.last_name = verified_input["last_name"]
        self.office = verified_input["office"]
        self.tel = verified_input["tel"]

        Staff.staff_list[self.id] = self

    def __str__(self):
        return f"{self.id}\t{self.first_name}\t{self.last_name}\t{self.office}\t{self.tel}"


def get_staff(value):
    value = int(value)
    if value not in Staff.staff_list.keys():
        raise Exception("Staff ID not found, check input")

    return Staff.staff_list[value]
