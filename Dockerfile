FROM python:3
RUN pip install flask
COPY .  C:\Users\l1313\Desktop\Devops\Project-3
CMD ["python","rest_app.py"]
