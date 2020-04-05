from datetime import datetime
from Animal import Animal
from FeedingRecord import FeedingRecord
from Food import get_food, Food
from ObservationRecord import ObservationRecord
from Staff import get_staff, Staff

date = datetime.now().date()
time = datetime.now().time()

s1 = Staff("Oguzhan", "Ergun", "A-111", 1234)
s2 = Staff("Arslan", "Charyyev", "A-222", 9876)
f1 = Food("Big Joy", "Whiskas")
f2 = Food("Diet Time", "Royal Canin")

sample_env = dict()
sample_env["relative_humidity"] = 123
sample_env["enclosure_size"] = 67
sample_env["temperature"] = 2
sample_env["hours_of_light_per_day"] = 1

a1 = Animal('M', date, "Black", sample_env)
a2 = Animal('F', date, "White", sample_env)

s = 0
for k in Staff.staff_list.keys():
    s = k
    break

fr1 = FeedingRecord(date, time, get_food("Diet TimeRoyal Canin"), 100, get_staff(s))
or1 = ObservationRecord(date, time, 100, 60, "Ok", get_staff(s))

a1.observation_record.append(or1)
a1.feeding_record.append(fr1)
a1.feeding_record.append(fr1)