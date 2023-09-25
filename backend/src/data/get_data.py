"""
Программа: Парсинг комментариев
Версия: 1.0
"""

from googleapiclient.discovery import build
from ..data.save_data import save_comments


def get_all_comments(**kwargs):
    """
    Выгрузка комментариев
    """
    service = build("youtube", "v3", developerKey=kwargs["api_key"])

    all_comments, all_likes, comms_for_likes = list(), list(), list()

    # сбор комментариев и лайков по id каналов
    for i in kwargs["channels_id"]:
        args = {"allThreadsRelatedToChannelId": i, "part": "snippet", "maxResults": 100}

        comments, likes, comms_list = set(), list(), list()

        for _ in range(30):
            response = service.commentThreads().list(**args).execute()

            for item in response["items"]:
                snippet = item["snippet"]["topLevelComment"]["snippet"]
                comment = snippet["textDisplay"]
                # уникальные комменты
                comments.add(comment)
                # все комментарии
                comms_list.append(comment)
                # кол-во лайков
                like_count = snippet["likeCount"]
                likes.append(like_count)

            args["pageToken"] = response.get("nextPageToken")
            if not args["pageToken"]:
                break

        all_comments.append(list(comments))
        all_likes.extend(likes)
        comms_for_likes.extend(comms_list)

    # сохранение данных
    data = [all_comments, all_likes, comms_for_likes]
    path = ["all_comments", "all_likes", "comms_for_likes"]
    save_comments(path, data)
    return all_comments, all_likes, comms_for_likes
