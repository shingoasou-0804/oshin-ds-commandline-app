FROM library/python:3.11
COPY requirements.txt requirements.lock ./
RUN pip install -r requirements.txt -c requirements.lock
