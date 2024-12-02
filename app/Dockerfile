FROM python:3.8

EXPOSE 8080
WORKDIR /workspace

COPY . /workspace

RUN pip install -r requirements.txt

RUN source app/venv/bin/activate && python -m unittest discover -s appp

CMD ["python", "app/app.py"]

