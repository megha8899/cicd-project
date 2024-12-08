FROM python:3.8

EXPOSE 8080
WORKDIR /cicd-project

COPY ./app /cicd-project/app

RUN python -m ensurepip --upgrade 
RUN pip install --no-cache-dir -r /cicd-project/app/requirements.txt

ENTRYPOINT ["python", "-m", "unittest", "discover", "-s", "/cicd-project/app"]
CMD []


