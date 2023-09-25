"""
Программа: Получение топиков
Версия: 1.0
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
import pandas as pd
from ..data.save_data import save_comments


def vectorize_text(data: list):
    """
    Получение матрицы кол-ва слов в комментариях
    :param data: список всех комментариев
    :return:
    """
    # Векторизация
    tfidf = TfidfVectorizer(max_df=0.8, min_df=0.001)
    matrix = tfidf.fit_transform(data).toarray()
    # Преобразование в датасет
    feat_names = tfidf.get_feature_names_out()
    x = pd.DataFrame(matrix, columns=feat_names)
    return x, feat_names


def get_nmf_topics(x, feat_names, **kwargs) -> pd.DataFrame:
    """

    :param x:
    :param feat_names:
    :return: датасет
    """
    # nmf факторизация
    nmf = NMF(kwargs["n_components"], init="nndsvda", max_iter=1000, tol=0.0005)
    # nmf_x = nmf.fit_transform(x)
    nmf.fit_transform(x)
    nmf_topics = nmf.components_

    word_dict = {}
    words_img = []
    for i in range(kwargs["n_components"]):
        # берем топ заданного кол-во слов по каждому топику
        words_ids = nmf_topics[i].argsort()[: -kwargs["n_top_words"] - 1: -1]
        words = [feat_names[key] for key in words_ids]
        word_dict["Topic_" + "{:02d}".format(i + 1)] = words
        words_img.append(words)
    # сохранение данных
    save_comments(["topics"], [word_dict])
    df = pd.DataFrame(word_dict)

    return df
