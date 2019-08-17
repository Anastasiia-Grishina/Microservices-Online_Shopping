FROM python:3.7-stretch

WORKDIR /home/

RUN pip3 install flask flask-restful pymodm requests

COPY * ./tracking/

ENV FLASK_APP tracking

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]