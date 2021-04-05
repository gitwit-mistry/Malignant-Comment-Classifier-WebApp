FROM mistryprathamesh/flask-app:latest

EXPOSE 8080

COPY flask_app/ .

RUN python3 -m venv vpy
RUN . vpy/bin/activate
RUN pip3 install -r requirements.txt

RUN python3 -m nltk.downloader stopwords

ENTRYPOINT ["python3","app.py" ]
