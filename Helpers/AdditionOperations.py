from re import match
from Classes.FeedingRecord import FeedingRecord
from Classes.ObservationRecord import ObservationRecord
from Classes.Staff import Staff
from Classes.Food import Food
from Classes.Animal import Animal
from Helpers.Parsers import animal_parser, date_parser, staff_parser, time_parser, food_parser


class AdditionOperations:
    @staticmethod
    def add_staff():
        print("--Add staff--")
        office_check = tel_check = False
        first_name = input("Enter First Name:")
        last_name = input("Enter Last Name:")

        while not office_check:
            office = input("Enter Office [A-XXX]:")
            if match(r"^A-\d{3}$", office) is None:
                 print("Error: Wrong Office Format, It must have the format [A-XXX]")
            else:
                office_check = True

        while not tel_check:
            tel = input("Enter Telephone [4 Digits]:")
            if match(r"^\d{4}$", tel) is None:
                print("Error: Wrong Tel Format, It must has only 4 digits")
            else:
                tel_check = True    

        Staff(first_name, last_name, office, tel)
        print("Record added.")

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
        print("Record added.")

    @staticmethod
    def add_food():
        print("--Add food--")
        name = input("Enter Food Name:")
        manufacturer = input("Enter Manufacturer:")
        Food(name, manufacturer)
        print("Record added.")

    @staticmethod
    def add_feeding_record_given_animal():
        print("--Add feeding details of a given animal--")
        animal = animal_parser()
        date = date_parser("Date")

        if len([item for item in animal.feeding_record if item.date == date]) < 2:
            time = time_parser()
            food = food_parser()
            weight = int(input("Enter Weight:"))
            staff = staff_parser()
            animal.feeding_record.append(FeedingRecord(date, time, food, weight, staff))
            print("Record added.")
        else:
            raise Exception(f"Animal NO:{animal.no} should not be fed more than two times in a day")

    @staticmethod
    def add_observation_record_given_animal():
        print("--Add observation details of a given animal--")
        animal = animal_parser()
        date = date_parser("Date")

        if len([item for item in animal.observation_record if item.date == date]) < 3:
            time = time_parser()
            animal_weight = int(input("Enter Animal Weight:"))
            temperature = int(input("Enter Temperature:"))
            note = input("Enter Note:")
            staff = staff_parser()
            animal.observation_record.append(ObservationRecord(date, time, animal_weight, temperature, note, staff))
            print("Record added.")
        else:
            raise Exception(f"Animal NO:{animal.no} should not be observed more than three times in a day")
