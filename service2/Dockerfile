FROM python:3.10
WORKDIR /serv1
COPY ./requirements.txt /serv1/requirements.txt
RUN python3 -m pip install pip --upgrade
RUN python3 -m pip install psycopg2-binary
RUN python3 -m pip install -r requirements.txt
COPY . /serv1/
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]