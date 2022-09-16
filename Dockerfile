FROM python:3.10-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt
  
COPY . /code

EXPOSE 80

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
