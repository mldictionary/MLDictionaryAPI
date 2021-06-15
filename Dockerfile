FROM python:3.9

RUN mkdir -p /opt/api

COPY requirements.txt /opt/api
WORKDIR /opt/api

RUN apt-get update
RUN pip3 install -r requirements.txt

EXPOSE 8088

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8088"]
CMD ["api_dictionary.app:create_app()"]
