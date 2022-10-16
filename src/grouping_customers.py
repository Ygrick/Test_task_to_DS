import sys


def groups_customers_1(n_customers, n_first_id=0) -> dict:
    # инициализация списка пользователей
    list_customers = list(
        range(n_first_id, n_customers)
    )
    # инициализация словаря для хранения групп
    dict_customers = dict()

    for item in list_customers:
        # вычисление суммы цифр
        str_item = map(int,
                       str(item)
                       )
        count_digit_item = sum(str_item)

        # если группа не создана -> создаём
        if count_digit_item not in dict_customers.keys():
            dict_customers[count_digit_item] = list()

        # помещаем пользователя в группу
        dict_customers[count_digit_item].append(item)

    # сортируем группы по порядку и возвращаем словарь
    return dict(sorted(dict_customers.items(), key=lambda item: item[1]))


if __name__ == "__main__":
    try:
        res = groups_customers_1(*list(map(int, sys.argv[1:])))
        print(res)
    except: 
        print('Введён неправильный аргумент.')

