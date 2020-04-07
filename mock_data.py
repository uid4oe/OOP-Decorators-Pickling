from datetime import datetime
from Classes.Animal import Animal
from Classes.FeedingRecord import FeedingRecord
from Classes.Food import get_food, Food
from Classes.ObservationRecord import ObservationRecord
from Classes.Staff import get_staff, Staff

date = datetime.now().date()
time = datetime.now().time()

s1 = Staff("Oguzhan", "Ergun", "A-111", 1234)
s2 = Staff("oe", "00", "A-222", 9876)
f1 = Food("Regular Sterilised 37", "Royal Canin")
f2 = Food("Regular Fit 32", "Royal Canin")
f3 = Food("Chicken in Jelly", "Whiskas")

sample_env = dict()
sample_env["relative_humidity"] = 20
sample_env["enclosure_size"] = 20
sample_env["temperature"] = 20
sample_env["hours_of_light_per_day"] = 10

a1 = Animal('M', date, "Black", sample_env)
a2 = Animal('F', date, "White", sample_env)

s = 0
for k in Staff.staff_list.keys():
    s = k
    break

fr1 = FeedingRecord(date, time, get_food("Regular Sterilised 37Royal Canin"), 100, get_staff(s))
a1.feeding_record.append(fr1)
fr1 = FeedingRecord(date, time, get_food("Regular Fit 32Royal Canin"), 150, get_staff(s))
a1.feeding_record.append(fr1)
fr1 = FeedingRecord(date, time, get_food("Chicken in JellyWhiskas"), 200, get_staff(s))
a1.feeding_record.append(fr1)

or1 = ObservationRecord(date, time, 10, 25, "Initial Observation", get_staff(s))
a1.observation_record.append(or1)
or1 = ObservationRecord(date, time, 10, 24, "Stable", get_staff(s))
a1.observation_record.append(or1)
or1 = ObservationRecord(date, time, 11, 26, "Weight Gain", get_staff(s))
a1.observation_record.append(or1)
