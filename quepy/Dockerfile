FROM python:3.6

EXPOSE 8000

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt

RUN git clone https://github.com/DarFig/quepy

WORKDIR /app/quepy

RUN git checkout python3.6

RUN rm -r quepy

RUN mv quepy_python36 quepy

RUN python setup.py install

WORKDIR /app

COPY ./app /app

RUN python dbpedia/main.py "Who is Tom Cruise?"