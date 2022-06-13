# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка:
# постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

from Lesson_08_Task_05 import ExtetedWarehouse
from Lesson_08_Task_04 import Printer

class InvalidAmount(Exception):
    pass

class VerifiedWarehouse(ExtetedWarehouse):

    def add(self, equip, amount):

        try:
            if amount.isdigit():
                ExtetedWarehouse.add(equip, amount)
            else:
                raise InvalidAmount
        except InvalidAmount:
            print('Количество может быть только числом')


vwh = VerifiedWarehouse()
pr1 = Printer()
vwh.add(pr1, 'a10')