FROM python:3.8
RUN pip install -r requirements.txt
RUN py app.py
