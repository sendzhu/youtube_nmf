"""
Программа: Сохранение и получение данных
Версия: 1.0
"""

import pickle
import yaml


def save_comments(path: list, data: list) -> None:
    """
    Сохранение данных
    :param path: название(-я) папок для вводимых данных
    :param data: данные, которые нужно сохранить
    :return: None
    """
    config_path = "../config/params.yml"
    with open(config_path) as file:
        config = yaml.load(file, Loader=yaml.FullLoader)

    # преобразование в список кортежей [(key, val), ..]
    data_path = list(zip(path, data))

    for i in data_path:
        key = i[0]
        values = i[1]
        with open(f'{config["save_data"][key]}.pkl', "wb") as file:
            pickle.dump(values, file)


def load_comments(path: list) -> list:
    """
    Получение данных из файла
    :param : название(-я) папок для выводимых данных
    :return: данные
    """
    config_path = "../config/params.yml"
    with open(config_path) as file:
        config = yaml.load(file, Loader=yaml.FullLoader)

    lst_data = []
    for x in path:
        with open(f'{config["save_data"][x]}.pkl', "rb") as file:
            data = pickle.load(file)
        lst_data.append(data)

    return lst_data
