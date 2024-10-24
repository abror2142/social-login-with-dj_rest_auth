FROM python:3

COPY ./requirements.txt /
RUN pip install --no-cache-dir --timeout=1000 -r /requirements.txt

COPY ./entrypoint.sh /

WORKDIR /home/app/backend
COPY . .

EXPOSE 8000
ENTRYPOINT [ "sh", "/entrypoint.sh" ]