from datetime import datetime, time, date
from Staff import Staff


# input and type verifier decorative for Observation Record class
def input_verifier(*types):
    def wrapper(f):
        def verify(*values):
            # checks the total number of inputs
            if len(values) < 7:
                raise Exception("You must enter Date, Time, Animal Weight, Temperature, Note and Staff "
                                "for new Observation Record instantiation")

            if not (type(values[1]) is types[1] and type(values[2]) is types[2] and type(values[3]) is
                    types[3] and type(values[4]) is types[4] and type(values[5]) is types[5]
                    and type(values[6]) is types[6]):
                raise Exception("Wrong input format for Observation Record class!")

            if values[1] is None:
                raise Exception("Wrong Date Format, retry.")

            # creates dictionary with the forced types
            mock = dict()
            mock["date"] = values[1]
            mock["time"] = values[2]
            mock["animal_weight"] = values[3]
            mock["temperature"] = values[4]
            mock["note"] = values[5]
            mock["staff"] = values[6]

            return f(values[0], mock)

        return verify

    return wrapper


class ObservationRecord:
    __slots__ = ["date", "time", "animal_weight", "temperature", "note", "staff"]

    @input_verifier(object, date, time, int, int, str, Staff)
    def __init__(self, verified_input):
        self.date = verified_input["date"]
        self.time = verified_input["time"]
        self.animal_weight = verified_input["animal_weight"]
        self.temperature = verified_input["temperature"]
        self.note = verified_input["note"]
        self.staff = verified_input["staff"]

    def __str__(self):
        return f"Date: {self.date} - Time: {self.time} - Animal Weight: {self.animal_weight} " \
               f"- Temperature: {self.temperature} - Note: {self.note} - " \
               f"Staff: {self.staff.first_name + ' ' + self.staff.last_name}"
