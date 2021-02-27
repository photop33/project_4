FROM python:3
COPY rest_app.py /
RUN pip install requests
RUN pip install flask
RUN pip install pymysql
CMD [ "python", "./rest_app.py" ]
