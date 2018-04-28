FROM python:2.7

COPY requirements.txt .

RUN pip install click

COPY . .

CMD python run.py /data/input.txt
