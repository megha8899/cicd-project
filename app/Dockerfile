FROM python:3.8

EXPOSE 8080
WORKDIR /cicd-project

COPY . /cicd-project/app

RUN pip install --no-cache-dir -r /cicd-project/app/requirements.txt

RUN python -m unittest discover -s /cicd-project/app

CMD ["python", "/cicd-project/app/app.py"]


