# MLOps project: Analysis of discussions in the comments of YouTube channels dedicated to Data Science 💻 💬

## UI Demo
![alt text](demo/example.gif?raw=true)

## Данная программа показывает что чаще всего обсуждают люди под комментариями популярных ютуб каналов, посвященных Data Science

___
## Запуск программы с помощью Docker Compose

- Сборка сервисов из образов внутри backend/frontend и запуск контейнеров в автономном режиме

`docker compose up -d`

___
## Folders
- `/backend` - Папка с проектом FastAPI
- `/frontend` - Папка с проектом Streamlit
- `/config` - Папка, содержащая конфигурационный файл
- `/data` - Папка, содержащая извлеченные данные и обработанные данные в формате pickle, а также полученные топики
- `/demo` - Папка, содержащая демо работы сервиса в Streamlit UI в формате gif
