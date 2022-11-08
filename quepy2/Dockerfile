FROM python:2.7.18

WORKDIR /app

COPY ./nltk-2.0.5-https-distribute.tar.gz /app/nltk-2.0.5-https-distribute.tar.gz
RUN pip install nltk-2.0.5-https-distribute.tar.gz

COPY ./requirements.txt /app/requirements.txt

#COPY ./nltk_download.py /app/./nltk_download.py

RUN pip install -r requirements.txt && \
    quepy --version && \
    git clone https://github.com/machinalis/quepy

#RUN python nltk_download.py
#CMD python -m nltk.downloader

COPY ./wordnet /usr/local/share/nltk_data/corpora/wordnet

COPY ./maxent_treebank_pos_tagger /usr/local/share/nltk_data/taggers/maxent_treebank_pos_tagger

RUN python quepy/examples/dbpedia/main.py "Who is Tom Cruise?" 
