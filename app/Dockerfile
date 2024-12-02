FROM python:3.8

EXPOSE 8080
WORKDIR /workspace

COPY . /workspace

RUN pip install -r requirements.txt

RUN python -m unittest discover -s app

CMD ["python", "app/app.py"]

