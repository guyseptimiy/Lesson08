# Реализовать класс «Дата»,
# функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:

    def __init__(self, format_string):
        self.data = format_string
        self.dd = 0
        self.mm = 0
        self.yy = 0

    @classmethod
    def reformat(cls, formstr):
        parts = formstr.split('-')
        print(parts)
        return parts

    @staticmethod
    def verify(parts):
        pairs = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        dd = int(parts[0])
        mm = int(parts[1])

        if mm > 12:
            print('Число месяц больше 12')
        else:
            if dd > pairs.get(mm):
                print('число дней в месяце больше разрешенного в месяце')


d = input('inupt data in dd-mm-yy format:')

data = Data(d)

print(data.data)
data.reformat(d)

data.verify(data.reformat(d))
