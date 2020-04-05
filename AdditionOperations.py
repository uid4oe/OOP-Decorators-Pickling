from re import search
from FeedingRecord import FeedingRecord
from ObservationRecord import ObservationRecord
from Staff import Staff
from Food import Food
from Animal import Animal
from Parsers import animal_parser,date_parser,staff_parser,time_parser,food_parser


class AdditionOperations:
    @staticmethod
    def add_staff():
        print("--Add staff--")
        office_check = tel_check = False
        first_name = input("Enter First Name:")
        last_name = input("Enter Last Name:")

        while not office_check:
            office = input("Enter Office [A-XXX]:")
            check_digits = search(r"\d+", office)
            if office.startswith("A-") and check_digits is not None and len(check_digits.group(0)) == 3:

                office_check = True
            else:
                print("Error: Wrong Office Format, It must have the format [A-XXX]")

        while not tel_check:
            tel = int(input("Enter Telephone [4 Digits]:"))
            if 999 < tel < 9999:
                tel_check = True
            else:
                print("Error: Wrong Tel Format, It must has 4 digits")

        Staff(first_name, last_name, office, tel)

    @staticmethod
    def add_animal():
        print("--Add animal--")
        gender = input("Enter Gender:")
        date = date_parser("Birthday")
        colour = input("Enter Colour:")
        print("--Environment Conditions--")
        ec = dict()
        ec["relative_humidity"] = int(input("Enter Relative Humidity:"))
        ec["enclosure_size"] = int(input("Enter Enclosure Size:"))
        ec["temperature"] = int(input("Enter Temperature:"))
        ec["hours_of_light_per_day"] = int(input("Enter Hours of Light per Day:"))

        Animal(gender, date, colour, ec)

    @staticmethod
    def add_food():
        print("--Add food--")
        name = input("Enter Food Name:")
        manufacturer = input("Enter Manufacturer:")

        Food(name, manufacturer)

    @staticmethod
    def add_feeding_record_given_animal():
        print("--Add feeding details of a given animal--")
        animal = animal_parser()
        d = date_parser()
        time = time_parser()
        food = food_parser()
        weight = int(input("Enter Weight:"))
        staff = staff_parser()

        if animal.details_between_dates(for_print=False, operation_type="feeding", start_date=d, end_date=d) < 2:
            animal.feeding_record.append(FeedingRecord(d, time, food, weight, staff))
        else:
            raise Exception(f"Animal NO:{animal.no} should not be fed more than two times in a day")

    @staticmethod
    def add_observation_record_given_animal():
        print("--Add observation details of a given animal--")
        animal = animal_parser()
        d = date_parser()
        time = time_parser()
        animal_weight = int(input("Enter Animal Weight:"))
        temperature = int(input("Enter Temperature:"))
        note = input("Enter Note:")
        staff = staff_parser()

        if animal.details_between_dates(for_print=False, operation_type="observation", start_date=d, end_date=d) < 3:
            animal.observation_record.append(ObservationRecord(d, time, animal_weight, temperature, note, staff))
        else:
            raise Exception(f"Animal NO:{animal.no} should not be observed more than three times in a day")
