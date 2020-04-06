from Classes.Animal import Animal
from Classes.Food import Food
from Classes.Staff import Staff
from Helpers.Parsers import animal_parser, date_parser

class ReportOperations:
    @staticmethod
    def staff_who_have_observed_a_given_animal():
        print("--Staff who have observed a given animal--")
        animal = animal_parser()
        animal.staff_who_observed()

    @staticmethod
    def observation_details_of_a_given_animal_between_specified_dates():
        print("--Observation details of a given animal between specified dates--")
        animal = animal_parser()
        sd = date_parser("Start Date")
        ed = date_parser("End Date")
        animal.details_between_dates(for_print=True, operation_type="observation", start_date=sd, end_date=ed)

    @staticmethod
    def feeding_details_of_a_given_animal_between_specified_dates():
        print("--Feeding details of a given animal between specified dates--")
        animal = animal_parser()
        sd = date_parser("Start Date")
        ed = date_parser("End Date")
        animal.details_between_dates(for_print=True, operation_type="feeding", start_date=sd, end_date=ed)

    @staticmethod
    def foods_that_have_been_fed_to_a_given_animal():
        print("--Foods that have been fed to a given animal--")
        animal = animal_parser()
        animal.foods_fed()

    @staticmethod
    def details_of_all_foods():
        print("--Details of all foods--")
        [print(f) for f in Food.food_list.values()]

    @staticmethod
    def details_of_all_animals():
        print("--Details of all animals--")
        [print(a) for a in Animal.animal_list.values()]

    @staticmethod
    def details_of_all_staff():
        print("--Details of all staff--")
        [print(s) for s in Staff.staff_list.values()]
