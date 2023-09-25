"""
Программа: Отрисовка графиков
Версия: 1.0
"""

import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
from nltk.probability import FreqDist
from heapq import nlargest
from nltk.tokenize import word_tokenize
import nltk


def top_comments(likes: list, comms: list) -> pd.DataFrame:
    """
    Выявление топа комментариев
    :param likes: лайки
    :param comms: комментарии
    :return: датасет
    """
    # наибольшего кол-во лайков
    top = nlargest(10, likes)
    # их id
    top_likes = [likes.index(x) for x in top]
    # очистка от лишних символов
    comms = [x.replace('<br>', ' ') for x in comms]
    comms = [x.replace('&quot;', ' ') for x in comms]
    # поиск по id топ 10 коммов
    top_comms = [comms[x] for x in top_likes]
    # для полного отражение текста в строке датасета
    # pd.set_option("display.max_colwidth", None)
    df_comm = pd.DataFrame(top_comms, columns=["Top_Comments"])

    return df_comm


def lenth_comms(all_comms: list) -> matplotlib.figure.Figure:
    """
    Анализ длины комментариев
    :param all_comms: комментарии
    :return: поле рисунка
    """
    comments = sum(all_comms, [])
    # длина каждого комментария
    sent_len = [len(w.split()) for w in comments]

    # Визуализация
    fig = plt.figure(figsize=(10, 5))
    sns.kdeplot(sent_len, color="b", shade=True)

    plt.xlabel("Распределение длины комментариев")
    plt.grid(True)

    return fig


def get_tokens(clean_comms: list) -> list:
    """
    :param clean_comms: очищенные комментарии
    :return: токены
    """
    words = " ".join(clean_comms)
    # разбиваем на токены очищенный текст
    nltk.download('punkt')
    txt_tokens = word_tokenize(words)
    return txt_tokens


def top_words(clean_comms: list) -> pd.DataFrame:
    """
    Анализ частности слов
    :param clean_comms: очищенные комментарии
    :return: датасет
    """
    tokens = get_tokens(clean_comms)
    # топ 10 слов
    fdist = FreqDist(tokens)
    fdist = fdist.most_common(10)
    df = pd.DataFrame(fdist, columns=["top_words", "count"])
    return df


def bigrams(clean_comms: list) -> matplotlib.figure.Figure:
    """
    Анализ частотности би-граммов
    :param clean_comms: очищенные комментарии
    :return: поле рисунка
    """
    tokens = get_tokens(clean_comms)

    # Создаем датасет самых частотных биграммов
    bigrams_series = (pd.Series(nltk.ngrams(tokens, 2)).value_counts())[:10]
    bigrams_top = pd.DataFrame(bigrams_series.sort_values(ascending=False))
    bigrams_top = bigrams_top.reset_index().rename(
        columns={"index": "bigrams", 0: "counts"}
    )

    # Визуализация биграммы
    plt.figure(figsize=(14, 10))
    sns.catplot(
        x="counts", y="bigrams", kind="bar", palette="vlag", data=bigrams_top, aspect=2
    )
    plt.title("TOP 10 pair of words which occurred the texts")
    return plt.show()
