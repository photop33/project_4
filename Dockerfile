FROM python:3
WORKDIR /app
COPY rest_app /app
RUN pip install flask
EXPOSE 5000
CMD python3 rest_app.py
