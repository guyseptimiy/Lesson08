#  Продолжить работу над первым заданием.
#  Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
#  Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
#  можно использовать любую подходящую структуру (например, словарь).

from Lesson_08_Task_04 import Warehouse


class ExtetedWarehouse(Warehouse):

    def add(self, equip, amount):

        equip_name = equip.__class__.__name__

        value = self.goods.get(equip_name)

        if value is None:
            self.goods.update({equip_name: amount})
        else:
            self.goods.update({equip_name: amount + value})
        print(f'Позиция {equip_name} оприходованна')

        print(self.goods)

    def move(self, equip, amount):
        equip_name = equip.__class__.__name__

        value = self.goods.get(equip_name)

        if value is None:
            print(f'Позиция {equip_name} отсутствует на складе')
        elif value - amount < 0:
            print(f'Позиция {equip_name} нехватает {value - amount}')
        else:
            print(f'Позиция {equip_name} перемещена')
            self.goods.update({equip_name: value - amount})

        print(self.goods)
