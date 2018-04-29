FROM python:2.7

COPY requirements.txt .

RUN pip install click

COPY . .

RUN python tests.py

CMD python run.py
