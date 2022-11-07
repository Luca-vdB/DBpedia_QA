FROM python:3.2

# expose
EXPOSE 8000
# set working directory
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /app

CMD python3 app/dbpedia/main.py "Who is Tom Cruise?"

