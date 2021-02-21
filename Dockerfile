FROM python:3.7-alpine
ADD . /
CMD ["python", "app.py"]
