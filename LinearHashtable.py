import math


class Entry(object):  # записываем ключ,значение св-во инициализации запрашивает эти 2 поля при запросе печатает Value
    def __str__(self):
        return str(self.value)

    def __init__(self, key=0, value=0):  # дефолтные значения
        self.key = key
        self.value = value


def AuxiliaryHash(key, size):  # часть линейного хэша, 1ая ступень вычислений
    A = 0.618  # шаг рассчитан из того что в массиве 32 элемента некий сдвиг
    return int(math.floor(size * ((key * A) % 1)))  # часть формулы без деления на размер массива


def LinearHash(key, i, size):  # рассчитывает позицию, ее вызывает hash осн функция
    return (AuxiliaryHash(key, size) + i) % size  # i - позиция в массиве и делим на размер массива

# главное правило хэша - чтобы не проходить миллион значений, а сразу попадать на нужный
class LinearHashtable(object):  # класс хранящий хэш-таблицу и делает с ней разное
    # self - приватный массив с данными в классе
    def get(self, key):  # получаем значение из методички должен быть поиск по значению
        i = 0  # кол-во попыток найти значение обычно достигает единицы
        entry = self.entries[self.hash(key, i)]  # обращаемся к массиву который иниц
    # в init фция хэш переводит в порядковый номер
        while entry is None or entry.key != key:  # пока entry пустое или ключи не совпадают
            # начинаем ходить, но обычно начинает с первого раза без коллизий
            i += 1
            if i == self.size:
                return None
            entry = self.entries[self.hash(key, i)]
        return entry.value

    def search(self, key):  # self - если функция внутри класса, должно быть в параметрах,
        # через self обращаемся ко всем функциям класса
        i = 0
        entry = self.entries[self.hash(key, i)]
        search_result = str(self.hash(key, i)) + " "  # выводит то, что похоже на наш ключ
        while entry is None or entry.key != key:
            i += 1
            if i == self.size:
                return search_result + "-1"
            entry = self.entries[self.hash(key, i)]
            search_result += str(self.hash(key, i)) + " "
        return search_result

    def put(self, key, value):  # Добавление хэша внутренняя
        i = 0
        entry = self.entries[self.hash(key, i)]
        while entry and entry.key != key:
            i += 1
            if i == self.size:
                # raise Exception("Table is Full!")
                return
            entry = self.entries[self.hash(key, i)]
        if entry is None:  # если такого значения нет, добавляем его на опр позицию по хэшу
            entry = Entry(key=key, value=value)
            self.entries[self.hash(key, i)] = entry
        else:  # если есть такое значение, то мы тупо переписываем Value
            entry.value = value

    def insert(self, value):  # чтобы не передавать 2 значения одинаковых
        self.put(value, value)

    def hash(self, key, i):  # высчитывает позицию на кот будет находиться значение
        return LinearHash(key, i, self.size)

    def __str__(self):  # если на этот класс вызываем печать
        # если классу передаем print то ищет str и он уже будет что-то делать
        lines = []  # объявление пустого массива и будем печатать содержимое функции, ее массива
        for i in range(len(self.entries)):  # len - опр размер массива
            if not self.entries[i]:
                lines.append("" + str(i) + "\t" + "-1")  # append - добавляет в конец массива
            else:
                lines.append("" + str(i) + "\t" + str(self.entries[i].value))
        return "\n".join(lines)  # join - функция склейки по новой строчке

    def __init__(self, size=32):  # инициализация всего класса, у каждого класса техницеские переменные
        # чтобы их не передавать огрмным списком аргументов кот нужны каждой функции
        self.i = 0
        self.size = size
        self.entries = [None] * self.size  # в массиве после перебора будет храниться 32 класса с key и value
        # создание пустой таблицы

        #когда объявляем класс идем в Init
