FROM python:3.3

# expose
EXPOSE 8000
# set working directory
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /app

RUN rm -r /usr/local/lib/python3.3/site-packages/quepy/

COPY ./quepy /usr/local/lib/python3.3/site-packages/quepy/

#RUN cat /usr/local/lib/python3.2/site-packages/quepy/quepyapp.py

RUN quepy --version

RUN python app/dbpedia/main.py "Who is Tom Cruise?"