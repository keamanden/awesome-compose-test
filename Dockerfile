FROM python:3.10-alpine
WORKDIR /code
RUN pip install flask redis
COPY . .
CMD ["python", "app.py"]
