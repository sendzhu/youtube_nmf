"""
Программа: Frontend часть проекта
Версия: 1.0
"""

import streamlit as st
from src.plotting.charts import *
from src.data.save_data import load_comments

# from src.data.save_data import load_comments
# sys.path.insert(1, "/Users/pc/PycharmProjects/youtubeProject/backend/src/data")


def main_page():
    """
    Страница с описанием проекта
    """
    st.image(
        "https://www.computerra.ru/wp-content/uploads/2019/08/data_science_5.png",
        width=600
    )

    st.markdown("# Описание проекта")
    st.title(
        "MLOps project: Analysis of discussions in the comments of YouTube channels dedicated to Data Science 💻 💬"
    )
    st.write(
        """
        Данная программа показывает что чаще всего обсуждают люди 
        под комментариями популярных ютуб каналов, посвященных Data Science
        """
    )


def exploratory():
    """
    Exploratory data analysis
    """
    st.markdown("# Exploratory data analysis️")

    path = ["all_comments", "all_likes", "comms_for_likes", "clean_comms"]
    lst = load_comments(path)
    # load and write dataset
    all_comments, all_likes, comms_for_likes, clean_comms = (
        lst[0],
        lst[1],
        lst[2],
        lst[3],
    )

    # топ коммов
    st.markdown("## Топ 10 комментариев")
    st.write(top_comments(likes=all_likes, comms=comms_for_likes))
    # распределение длины всех комментов
    st.markdown("## Распределение длины всех комментариев")
    st.pyplot(lenth_comms(all_comms=all_comments))
    # топ слов
    st.markdown("## Топ 10 слов")
    st.write(top_words(clean_comms=clean_comms))
    # топ би-граммов
    st.markdown("## Топ 10 би-грамм")
    st.set_option("deprecation.showPyplotGlobalUse", False)
    st.pyplot(bigrams(clean_comms=clean_comms))


def result():
    """
    Результаты
    """
    topics = load_comments(["topics"])
    topics = topics[0]

    st.markdown("## Полученные тематики")
    st.write(pd.DataFrame(topics))


def main():
    """
    Сборка пайплайна в одном блоке
    """
    page_names_to_funcs = {
        "Описание проекта": main_page,
        "Разведочный анализ данных": exploratory,
        "Полученный результат": result,
    }
    selected_page = st.sidebar.selectbox("Выберите пункт", page_names_to_funcs.keys())
    page_names_to_funcs[selected_page]()


if __name__ == "__main__":
    main()
