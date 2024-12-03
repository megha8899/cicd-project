FROM python:3.8

EXPOSE 8080
WORKDIR /cicd-project

COPY ./app /cicd-project/app

RUN pip install --no-cache-dir -r /cicd-project/app/requirements.txt

CMD ["python", "/cicd-project/app/app.py"]


