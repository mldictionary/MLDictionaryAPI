FROM python:3.10

RUN mkdir -p /opt/api

COPY requirements.txt /opt/api
WORKDIR /opt/api

RUN apt-get update
RUN pip3 install -r requirements.txt

EXPOSE 8088

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8088"]
CMD ["mldictionary_api.app:create_app()"]
