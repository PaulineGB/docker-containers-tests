FROM python:latest

ARG TEST
ENV TEST=$TEST

WORKDIR /usr/src/app

COPY $TEST.py .

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD python3 $TEST.py
