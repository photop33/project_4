FROM python:3
ADD . "C:\Users\l1313\PycharmProjects\3\"
RUN pip install flask
RUN pip install mysql
CMD [ "python", "./rest_app.py" ]
