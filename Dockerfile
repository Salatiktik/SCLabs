FROM python:3.10
WORKDIR /app sudo docker run --name lab1 --rm -it lab1: latest
COPY . /app 
CMD ["python", "main.py"]