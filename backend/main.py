"""
Программа: Модель для получения тематик под комментариями каналов про DS
Версия: 1.0
"""

import uvicorn
from fastapi import FastAPI

from src.pipeline.pipeline import pipeline_topics

import warnings
warnings.filterwarnings("ignore")


app = FastAPI()
CONFIG_PATH = "../config/params.yml"


@app.post("/topics")
def topics():
    """
    Получение тематик для выбранных каналов
    """
    df = pipeline_topics(config_path=CONFIG_PATH)

    return df


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=80)
