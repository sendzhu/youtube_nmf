"""
Программа: Сборный конвейер для получения топиков
Версия: 1.0
"""

import yaml
from ..model.model import vectorize_text, get_nmf_topics
from ..data.get_data import get_all_comments
from ..transform.transform import pipeline_preprocess


def pipeline_topics(config_path) -> dict:
    """
    Полный цикл парсинга данных, предобработки и вывода топиков
    :param config_path: путь до файла с конфигурациями
    :return: датасет
    """
    # get params
    with open(config_path) as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    data_config = config["get_data"]
    model_config = config["model"]

    # parsing
    all_comments, lst2, lst3 = get_all_comments(**data_config)

    # preprocess
    comments_clean = pipeline_preprocess(all_comments)

    # model
    x, feat_names = vectorize_text(comments_clean)
    df = get_nmf_topics(x, feat_names, **model_config)

    return df
