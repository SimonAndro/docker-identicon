FROM python:3.12

RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi
RUN pip install --upgrade pip
RUN pip install Flask gunicorn requests redis
WORKDIR /app
COPY app /app
COPY cmd.sh /

EXPOSE 9090
USER uwsgi

CMD ["/cmd.sh"]