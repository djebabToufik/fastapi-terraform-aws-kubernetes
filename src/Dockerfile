FROM python:latest

RUN pip install --upgrade pip
COPY . /src 
WORKDIR /src/
RUN pip install -r requirements.txt
CMD ["python","main.py"]