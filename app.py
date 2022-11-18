# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 11:15:48 2020

@author: dcise
"""
#from matplotlib.pyplot import imshow
import numpy as np
#from PIL import Image

#%matplotlib inline
#pil_im = Image.open('data/empire.jpg', 'r')
#imshow(np.asarray(pil_im))
import os

CURRENT_DIRECTORY = os.path.abspath(os.path.join(os.path.dirname('app.py')))
from flask import Flask, render_template, request, url_for
from flask_material import Material 
from PIL import Image
import urllib
import requests
import json
import sys
import base64
from base64 import b64encode
from tensorflow.keras.models import load_model
import tensorflow as tf
import io

from io import BytesIO
from tensorflow.python.framework import ops
from urllib.parse import urljoin, quote
##from google_images_download import google_images_download
import wikipedia
#response = google_images_download.googleimagesdownload()

app = Flask(__name__, template_folder='templates')
Material(app)
def init():
   global model,graph
   model = load_model(CURRENT_DIRECTORY + '\mnist-flask\model\H5.h5')
   graph = ops.reset_default_graph()

   
@app.route('/')
def upload_file():
   return render_template('index2.html')

@app.route('/about/')
def about():
    return render_template('about.html')

def upload_image_file(img):
   #if request.method == 'POST':
      #img = np.asarray(Image.open(request.files['file'].stream).convert("RGB"))
      #img = tf.keras.preprocessing.image.load_img(request.files['file'].stream)
      image = tf.image.convert_image_dtype(img, tf.float32)
      image = tf.image.resize(image, [240,40])
      image = tf.expand_dims(image, 0)
      
      y = model.predict(image)
      top_k = y[0].argsort()[-5:][::-1]
      x = np.array(['Accipiter Gentilis', 'Accipiter Nisus', 'Acrocephalus Palustris',
 'Acrocephalus Schoenobaenus', 'Acrocephalus Scirpaceus',
 'Actitis Hypoleucos', 'Aix Galericulata', 'Aix Sponsa', 'Alca Torda',
 'Alcedo Atthis', 'Anas Acuta', 'Anas Clypeata', 'Anas Crecca',
 'Anas Platyrhynchos', 'Anser Anser', 'Apus Apus', 'Aquila Chrysaetos',
 'Asio Flammeus', 'Asio Otus', 'Athene Noctua', 'Aythya Ferina',
 'Bombycilla Garrulus', 'Botaurus Stellaris', 'Calidris Alpina',
 'Calidris Canutus', 'Caprimulgus Climacurus', 'Caprimulgus Europaeus',
 'Carduelis Cannabina', 'Carduelis Carduelis', 'Charadrius Dubius',
 'Chenonetta Jubata', 'Chloris Chloris', 'Circus Aeruginosus',
 'Circus Cyaneus' ,'Dendrocopos Major', 'Garrulus Glandarius',
 'Haematopus Ostralegus', 'Larus Canus' ,'Larus Crassirostris',
 'Larus Fuscus', 'Milvus Milvus', 'Phasianus Colchicus',
 'Phoenicopterus Roseus', 'Picus Viridis' ,'Pluvialis Squatarola',
 'Polyplectron Schleiermacheri' ,'Strix Aluco', 'Tetrao Urogallus',
 'Tringa Totanus', 'Tyto Alba'])
      zz = str(x[top_k[0]]) + str('   ') + str(  y[0][top_k][0])
      zr = str(x[top_k[0]]) #this is species name of top guess
      zq = str(y[0][top_k][0]) #this is % sure of the first guess
      percents = []
      wikis =[]
      jj = 0
      names = []
      url ='https://www.itis.gov/ITISWebService/jsonservice/getITISTerms?srchKey='
      names_list= []
      while jj < 3:
         
         
         zr = str(x[top_k[jj]])
         names_list.append(str(x[top_k[jj]]))
         name = wikipedia.page(str(x[top_k[jj]]))
         wikis.append(name.url)
         percents.append("{:.0%}".format(y[0][top_k][jj]))
         requestURL = url + quote(zr)
         r = urllib.request.urlopen(requestURL)
         data = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))
         common = data['itisTerms'][0]['commonNames']
         if len(common) > 1:
             names.append(common[1])
         else: 
             names.append(common[0])
         r.close
         jj = jj+1
         
      #return 'We\'re ' + str(zq) + '% sure that this feather is from a ' + str(zr)
      names_string = ','.join(names_list)
      #absolute_image_paths = response.download({"keywords":names_string,"limit":1,"no_directory":"1", "output_directory": r"C:\Users\dcise\Desktop\Birds\ai-examples-master\Pulled", "no_download":1, "aspect_ratio": "square", "format":"jpg"})
      
      image1 = CURRENT_DIRECTORY + r"\mnist-flask\static\birds" + '\\' + names_list[0] + '.jpg'  #absolute_image_paths[0][names_list[0]][0]
      image2 = CURRENT_DIRECTORY + r"\mnist-flask\static\birds" + '\\' + names_list[1] + '.jpg' #absolute_image_paths[0][names_list[1]][0]
      image3 = CURRENT_DIRECTORY + r"\mnist-flask\static\birds" + '\\' + names_list[2] + '.jpg' #absolute_image_paths[0][names_list[2]][0]
      image_list = [image1, image2, image3]
      jjj=1
      #for var in image_list:
        #pix = np.asarray(Image.open(r'C:\Users\dcise\Desktop\Birds\ai-examples-master\mnist-flask\static\example.jpg'))
        #img = Image.fromarray(pix.astype('uint8'))
        #encoded_string = base64.b64encode(image_bytes).decode()      
        #globals()["w" + str(jjj)] = base64.b64encode(img).decode() 
      globals()["w" + str(1)] = 'mnist-flask/static/birds/' + names_list[0] + '.jpg'
      globals()["w" + str(2)] = 'mnist-flask/static/birds/' + names_list[1] + '.jpg'
      globals()["w" + str(3)] = 'mnist-flask/static/birds/' + names_list[2] + '.jpg'
        #jjj = jjj + 1
          #image = np.asarray(Image.open(r'C:\Users\dcise\Desktop\Birds\ai-examples-master\mnist-flask\static\example.jpg'))
          #response_image1 = requests.get(var)
          #file_object = io.BytesIO()
          #img = Image.open(BytesIO(response_image1.content))
          #pix = np.array(img)
          #img= Image.fromarray(pix.astype('uint8'))
          #img.save(file_object, 'PNG')
          #base64img = "data:image/png;base64,"+b64encode(file_object.getvalue()).decode('ascii')
          #globals()["w" + str(jjj)] = base64img
          #jjj = jjj+1
          
          
      #response_image1 = requests.get(image1)
      #file_object = io.BytesIO()
      #img = Image.open(BytesIO(response_image1.content))
      #pix = numpy.array(img)
      #img= Image.fromarray(pix.astype('uint8'))
     # img.save(file_object, 'PNG')
     # base64img = "data:image/png;base64,"+b64encode(file_object.getvalue()).decode('ascii')
      
      
       
      
      #print(image1)
      return render_template("listy.html", len = len(x), x = x, top_k = top_k, y=y, names = names, w1=w1, w2=w2, w3=w3, wikis = wikis, percents = percents)
@app.route('/uploader', methods = ['POST'])  
def user_image():
  if request.method == 'POST':
      app.logger.warning('TESTworks')
      img = np.asarray(Image.open(request.files['file'].stream).convert("RGB")) 
      returned = upload_image_file(img)
      return returned
@app.route('/uploader2', methods = ['GET','POST'])  
def default_image():
    #if request.method == 'POST':
        app.logger.warning('TEST')
        image = np.asarray(Image.open(CURRENT_DIRECTORY + r'\mnist-flask\static\example.jpg'))
        returned = upload_image_file(image)
        return returned
    #else: 
    #    return ""
if __name__ == '__main__':
   print(("* Loading Keras model and Flask starting server..."
      "please wait until server has fully started"))
   init()
   app.run(host = '127.0.0.1', port = 5000, debug=True, use_reloader=False, threaded=False)