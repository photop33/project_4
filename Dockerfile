FROM python:3
COPY rest_app /app
RUN pip install flask
CMD python3 rest_app.py
