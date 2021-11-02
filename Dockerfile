FROM python:3.8
RUN pip install -r "Ashana_bot/requirements.txt"
RUN py "Ashana_bot/app.py"
