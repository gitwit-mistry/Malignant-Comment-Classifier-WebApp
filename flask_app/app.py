from flask import Flask,render_template, request
import dataprocessor
import joblib
import socket
import _pickle as cPickle
import bz2

priv_ip = socket.gethostbyname(socket.gethostname())

#model = joblib.load('malignant_mails_classification_model.pkl')

# Load any compressed pickle file
def decompress_pickle(file):
 data = bz2.BZ2File(file, 'rb')
 data = cPickle.load(data)
 return data

model = decompress_pickle('model.pbz2') 

vectorizer = joblib.load('tfidf.pkl')

app = Flask(__name__)

@app.route('/')
def hello():
  return render_template('index.html')


@app.route('/input')
def input():
  return render_template('input.html')


@app.route('/result', methods= ["GET","POST"])
def predict():

  data  = request.args.get("cmt") 

  cleaned_data = dataprocessor.data_processor(data)
  print(cleaned_data)
  vect_data = vectorizer.transform([cleaned_data])

  data_res = model.predict(vect_data)[0]

  class_list = ['malignant','higly_malignant','rude','threat','abuse','loathe']

  res_dict = dict(zip(class_list,data_res))
 
  return render_template("result.html",res_dict=res_dict)
  

if __name__=='__main__':
  app.run(host=priv_ip,port=8080)
