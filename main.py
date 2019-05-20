from LinearHashtable import LinearHashtable
import random


def main():
    size_line = random.randint(10, 20)  # генерируется случайно от 10 до 20 чисел
    insert_values = (random.randint(0, int(r_t+199/5)) for r_t in range(0, size_line))  # от 0 до 199/5
    hash_line = LinearHashtable(size_line)  # инициализирует класс hash_line
    for value in insert_values:  # кидает туда значения
        print(value, end=' ')
        hash_line.insert(value)
    print(hash_line)


if __name__ == '__main__':
    main()
