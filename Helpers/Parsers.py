from datetime import datetime
from Classes.Animal import Animal, get_animal
from Classes.Food import Food, get_food
from Classes.Staff import Staff, get_staff


def animal_parser():
    check = False
    print("Available Animal NOs in the system: ", end="")
    print([f"{a.no}" for a in Animal.animal_list.values()])
    while not check:
        try:
            a = input("Enter Animal NO:")
            a = get_animal(a)
            check = True
        except Exception as e:
            print(f"Error: {e}")
    return a


def date_parser(value=''):
    check = False
    while not check:
        try:
            d = input(f"Enter {value} [DD/MM/YYYY]:")
            d = datetime.strptime(d, "%d/%m/%Y").date()
            check = True
        except:
            print("Wrong Date Format, retry.")
    return d


def time_parser():
    check = False
    while not check:
        try:
            t = input(f"Enter Time [HH:MM:SS]:")
            t = datetime.strptime(t, "%X").time()
            check = True
        except:
            print("Wrong Time Format, retry.")
    return t


def staff_parser():
    check = False
    print("Available Staff IDs in the system: ", end="")
    print([f"{s.id}" for s in Staff.staff_list.values()])
    while not check:
        try:
            s = input("Enter Staff ID:")
            s = get_staff(s)
            check = True
        except Exception as e:
            print(f"Error: {e}")
    return s


def food_parser():
    check = False
    print("Available Foods in the system: ", end="")
    print([f"Name:{f.name} - Manufacturer:{f.manufacturer}" for f in Food.food_list.values()])
    while not check:
        try:
            a = input("Enter Food Name:")
            b = input("Enter Manufacturer:")
            f = get_food(a + b)
            check = True
        except Exception as e:
            print(f"Error: {e}")
    return f
