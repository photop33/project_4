FROM python:3
COPY rest_app.py /
RUN pip install -r requirements.txt
CMD [ "python", "./rest_app.py" ]
