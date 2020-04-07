from Classes.Animal import Animal
from Classes.Food import Food
from Classes.Staff import Staff
from Helpers.Parsers import animal_parser, date_parser


class ReportOperations:

    # given filename data and header, writes to file
    @staticmethod
    def write_report(report_name, data, header):
        file = open(report_name, 'w')
        if not type(data) is str:
            data_string = "\n".join([str(d) for d in data])
            file.write(header + data_string)
        else:
            file.write(header+data)
        file.close()

    # given animal no, prints unique staff who fed it
    @staticmethod
    def staff_who_have_observed_a_given_animal():
        print("--Staff who have observed a given animal--")
        header = f"ID\tFirst Name\tLast Name\tOffice\tTel\n"
        animal = animal_parser()
        result_set = {record.staff for record in animal.observation_record}

        if len(result_set) == 0:
            print("No result.")
            ReportOperations.write_report("staff_who_have_observed_a_given_animal.txt", "No result.", header)
        else:
            print(header, end="")
            [print(s) for s in result_set]
            ReportOperations.write_report("staff_who_have_observed_a_given_animal.txt", result_set, header)

    # given start and end date, prints observation details
    @staticmethod
    def observation_details_of_a_given_animal_between_specified_dates():
        print("--Observation details of a given animal between specified dates--")
        header = f"Date\tTime\tAnimal Weight\tTemperature\tNote\tStaff\n"
        animal = animal_parser()
        start_date = date_parser("Start Date")
        end_date = date_parser("End Date")
        result = [i for i in animal.observation_record if start_date <= i.date <= end_date]

        if len(result) == 0:
            print("No result.")
            ReportOperations.write_report("observation_details_of_a_given_animal_between_specified_dates.txt",
                                          "No result.",
                                          header)

        else:
            print(header, end="")
            [print(i) for i in result]
            ReportOperations.write_report("observation_details_of_a_given_animal_between_specified_dates.txt",
                                          result,
                                          header)

    # given start and end date, prints feeding details
    @staticmethod
    def feeding_details_of_a_given_animal_between_specified_dates():
        print("--Feeding details of a given animal between specified dates--")
        header = f"Date\tTime\tFood Name\tManufacturer\tWeight\tStaff\n"
        animal = animal_parser()
        start_date = date_parser("Start Date")
        end_date = date_parser("End Date")
        result = [i for i in animal.feeding_record if start_date <= i.date <= end_date]

        if len(result) == 0:
            print("No result.")
            ReportOperations.write_report("feeding_details_of_a_given_animal_between_specified_dates.txt", "No result.",
                                          header)
        else:
            print(header, end="")
            [print(i) for i in result]
            ReportOperations.write_report("feeding_details_of_a_given_animal_between_specified_dates.txt", result,
                                          header)

    # given animal no, prints unique food that is given to animal
    @staticmethod
    def foods_that_have_been_fed_to_a_given_animal():
        print("--Foods that have been fed to a given animal--")
        header = f"Food Name\tManufacturer\n"
        animal = animal_parser()
        result_set = {record.food for record in animal.feeding_record}

        if len(result_set) == 0:
            print("No result.")
            ReportOperations.write_report("foods_that_have_been_fed_to_a_given_animal.txt", "No result.", header)
        else:
            print(header, end="")
            [print(f) for f in result_set]
            ReportOperations.write_report("foods_that_have_been_fed_to_a_given_animal.txt", result_set, header)

    # prints details of foods
    @staticmethod
    def details_of_all_foods():
        print("--Details of all foods--")
        header = f"Food Name\tManufacturer\n"
        result = [f for f in Food.food_list.values()]
        if len(result) == 0:
            print("No result.")
            ReportOperations.write_report("details_of_all_foods.txt", "No result.", header)
        else:
            print(header, end="")
            [print(f) for f in result]
            ReportOperations.write_report("details_of_all_foods.txt", result, header)

    # prints details of animals
    @staticmethod
    def details_of_all_animals():
        print("--Details of all animals--")
        header = f"No\tGender\tBirthday\tColour\tRelative Humidity\tEnclosure Size\tTemperature\tHours of light per day\n"
        result = [a for a in Animal.animal_list.values()]

        if len(result) == 0:
            print("No result.")
            ReportOperations.write_report("details_of_all_animals.txt", "No result.", header)
        else:
            print(header, end="")
            [print(a) for a in result]
            ReportOperations.write_report("details_of_all_animals.txt", result, header)

    # prints details of staff
    @staticmethod
    def details_of_all_staff():
        print("--Details of all staff--")
        header = f"ID\tFirst Name\tLast Name\tOffice\tTel\n"
        result = [s for s in Staff.staff_list.values()]
        if len(result) == 0:
            print("No result.")
            ReportOperations.write_report("details_of_all_staff.txt", "No result.", header)
        else:
            print(header, end="")
            [print(s) for s in result]
            ReportOperations.write_report("details_of_all_staff.txt", result, header)
