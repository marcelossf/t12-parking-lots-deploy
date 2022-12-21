FROM python:3.11

# não utiliza arquivos .pyc na construção da imagem/container (__pycache__)
ENV PYTHONDONTWRITEBYTECODE 1

# Os logs de erro não se perdem entre aplicação e container
ENV PYTHONUNBUFFERED 1

WORKDIR /django_app

# COPY . .
COPY . /django_app/

RUN pip install -U pip
RUN pip install -r requirements.txt
# RUN python manage.py migrate

# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]