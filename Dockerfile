FROM python:3.9

WORKDIR /FastAPI_JWT

COPY ./requirements.txt /app
RUN pip3 install -r requirements.txt
COPY ./app /FastAPI_JWT/app
EXPOSE 8000
CMD ["uvicorn", "FastAPI_JWT.main:app", "--reload"]
