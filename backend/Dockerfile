FROM python:3.8-slim-buster

WORKDIR /app/backend
COPY . .


RUN pip install --upgrade pip && \
    pip install -r requirements.txt


EXPOSE 8000
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" , "--reload"]
