FROM python:3.8

EXPOSE 8080
WORKDIR /workspace

COPY app /workspace/app

RUN pip install --no-cache-dir -r /workspace/app/requirements.txt

RUN python -m unittest discover -s /workspace/app

CMD ["python", "/workspace/app/app.py"]


