From python:3.9

Run mkdir -p /opt/api

Copy . /opt/api
Workdir /opt/api

Run apt-get update
Run pip3 install -r requirements.txt

Expose 8088

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8088"]
CMD ["api_dictionary.app:create_app()"]