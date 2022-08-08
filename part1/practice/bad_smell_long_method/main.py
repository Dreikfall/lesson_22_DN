# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def get_users_list():
    data = _read(csv)
    data_sort = _sort(data)
    data_filt = _filter(data_sort)
    return data_filt


# чтение из csv
def _read(csv_file):
    read_list = [i.split(';') for i in csv_file.split('\n')]
    return read_list


# Сортировка по возрасту по возрастанию
def _sort(data: list):
    data.sort(key=lambda x: int(x[1]))
    return data


# Фильтрация
def _filter(data):
    list_filt = [i for i in data if int(i[1]) > 10]
    return list_filt


if __name__ == '__main__':
    print(get_users_list())
