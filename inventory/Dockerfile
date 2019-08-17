FROM python:3.7-stretch

WORKDIR /home/

RUN pip3 install flask flask-restful pymodm requests

COPY * ./inventory/

ENV FLASK_APP inventory

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]