FROM python:3.8
WORKDIR "/src/Ashana_bot"
RUN pip install -r requirements.txt
RUN py Ashana_bot/app.py
