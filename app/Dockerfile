FROM python:3.8

EXPOSE 8080
WORKDIR /workspace

COPY . /workspace

RUN python -m venv /app/venv
RUN . /app/venv/bin/activate && pip install -r requirements.txt

RUN . /app/venv/bin/activate && python -m unittest discover -s appp

CMD ["python", "app/app.py"]

