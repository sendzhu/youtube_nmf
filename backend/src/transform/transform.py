"""
Программа: Предобработка данных
Версия: 1.0
"""

import re
from nltk.corpus import stopwords
from pymystem3 import Mystem
from ..data.save_data import save_comments
import nltk
nltk.download('stopwords')

def remove_links(text: str) -> str:
    """
    Удаление ссылок
    :param text: комментарии
    :return: комментарии без ссылок
    """
    for x in ["http\S+", "bit.ly/\S+", "www\S+"]:
        text = re.sub(x, "", text)
    return text


def clean_text(text: str) -> str:
    """
    Очистка текста от лишних символов
    :param text: комментарии
    :return: очищенные комментарии
    """
    # приводим текст к нижнему регистру
    text = text.lower()
    # очистка текста от символов
    text = re.sub(r"[^а-яё‽]+", " ", str(text))
    # возвращаем очищенные данные
    return text


def pipeline_preprocess(comments: list) -> list:
    """
    Препроцессинг текста, очистка, лемматизация, удаление стоп-слов
    :param comments: спарсенные комменты
    :return: очищенные комменты
    """
    # дополнение списка стоп-слов
    list_words = [
        "вообще",
        "буквально",
        "прямо",
        "говорится",
        "далее",
        "скажем",
        "короче",
        "видишь",
        "слышишь",
        "таким",
        "образом",
        "буквально",
        "типа",
        "самом",
        "деле",
        "общем",
        "некотором",
        "роде",
        "хрен",
        "принципе",
        "итак",
        "типо",
        "того",
        "только",
        "такое",
        "целом",
        "есть",
        "самое",
        "прикинь",
        "значит",
        "знаешь",
        "сказать",
        "понимаешь",
        "допустим",
        "слушай",
        "например",
        "просто",
        "конкретно",
        "ладно",
        "блин",
        "походу",
        "практически",
        "почти",
        "фактически",
        "себе",
        "твой",
        "свой",
        "достаточно",
        "который",
        "очень",
        "какой",
        "можешь",
        "свой",
        "такой",
        "почему"
    ]

    # загружаем стоп-слова для русского языка
    stop_words = stopwords.words("russian")
    stop_words.extend(list_words)

    clean_comms = []
    for text in comments:
        # объединяем комменты для быстрой лемматизации
        text = " ‽ ".join(text)
        # очистка текста от ссылок и лишних символов
        text = remove_links(text)
        text = clean_text(text)
        # лемматизация
        stem = Mystem()
        text = stem.lemmatize(text)
        # удаляем пробелы
        text = [token for token in text if token != " "]
        text = " ".join(text)
        # удаление стоп-слов
        text = " ".join([i for i in text.split() if i not in stop_words])
        text = text.strip()
        # обратно разъединяем комменты
        text = text.split(" ‽ ")
        # удаление слов короче 3 символов
        text = [x.split(' ') for x in text]
        text = [[i for i in j if len(i) > 3] for j in text]
        text = [' '.join(i) for i in text]
        clean_comms.extend(text)
        save_comments(["clean_comms"], [clean_comms])
    return clean_comms
