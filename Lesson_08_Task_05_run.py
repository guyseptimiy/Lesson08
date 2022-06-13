from Lesson_08_Task_05 import ExtetedWarehouse
from Lesson_08_Task_04 import Scaner
from Lesson_08_Task_04 import Printer
from Lesson_08_Task_04 import Xerox

wh = ExtetedWarehouse()
pr1 = Printer()
sc1 = Scaner()
xr1 = Xerox()

wh.add(equip=pr1, amount=10)
wh.add(equip=sc1, amount=10)
wh.add(equip=xr1, amount=10)

wh.move(pr1, 15)
wh.move(pr1, 10)
wh.move(pr1, 5)
