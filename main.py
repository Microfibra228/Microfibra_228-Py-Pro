# Добавление значения в конец

def add_end():
    num = int(input('Введите значение: '))

    list = [1, 2, 3]
    list.append(num)

    print('Вот список: ',  list)

# Добавление значения в начало


def add_start():
    num = int(input('Введите значение: '))

    list = [1, 2, 3]
    list.insert(0, num)

    print('Вот список: ', list)

# Добавление значения по индексу


def add_index():
    index = int(input('Введите значение, куда хотите добавить число: '))
    num = int(input('Введите значение: '))

    list = [1, 2, 3]
    list.insert(index, num)

    print('Вот список: ', list)

# Удаление из конца одного элемента


def del_end():
    list = [1, 2, 3]
    print('Список вначале: ', list)

    list_len = len(list) - 1
    list.pop(list_len)

    print('Список в конце: ', list)

# Удаление из начала одного элемента


def del_start():
    list = [1, 2, 3]
    list.pop(0)

    print('Вот список: ', list)


# Удаление по индексу одного элемента


def del_index():
    list = [1, 2, 3]
    index = int(input('Введите значение, откуда хотите удалить число: '))

    try:

        list.pop(index)
        print('Вот список: ', list)

    except IndexError:
        print('Что-то пошло не так. Индекс слишком большой!')








