FROM python:3
COPY rest_app.py
RUN pip install flask
RUN pip install mysql
CMD [ "python", "./rest_app.py" ]
