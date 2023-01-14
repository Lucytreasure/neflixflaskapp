from datetime import *
import time
import sys
import json
import requests
import os
# First we set our credentials

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
app = Flask(__name__)

@app.route('/Video/<video>')
def video_page(video):
    print (video)

    url = 'http://35.233.125.61/myflix/videos?filter={"video.file":"'+video+'"}'
    headers = {}
    payload = json.dumps({ })
    print (request.endpoint)
    response = requests.get(url)
    print (url)
    if response.status_code != 200:
      print("Unexpected response: {0}. Status: {1}. Message: {2}".format(response.reason, jResp['http status code'], jResp['message']))
      return "Unexpected response: {0}. Status: {1}. Message: {2}".format(response.reason, jResp['http status code'], jResp['message'])
    jResp = response.json()
    print (type(jResp))
    print (jResp)
    for index in jResp:
        for key in index:
           if (key !="_id"):
              print (index[key])
              for key2 in index[key]:
                  print (key2,index[key][key2])
                  if (key2=="Name"):
                      video=index[key][key2]
                  if (key2=="file"):
                      videofile=index[key][key2]
                  if (key2=="thumb"):
                      thumb=index[key][key2]
    return render_template('video.html', name=video,file=videofile,thumb=thumb)

@app.route('/')
def cat_page():
    url = "http://35.233.125.61/myflix/videos"
    headers = {}
    payload = json.dumps({ })

    response = requests.get(url)
    #print (response)
    # exit if status code is not ok
    print (response)
    print (response.status_code)
    if response.status_code != 200:
      print("Unexpected response: {0}. Status: {1}. Message: {2}".format(response.reason, jResp['http status code'], jResp['message']))
      return "Unexpected response: {0}. Status: {1}. Message: {2}".format(response.reason, jResp['http status code'], jResp['message'])
    jResp = response.json()
    print (type(jResp))
    html="<h2> Your Videos</h2>"
    for index in jResp:
       #print (json.dumps(index))
       print ("----------------")
       for key in index:

           if (key !="_id"):
              print (index[key])
              for key2 in index[key]:
                  print (key2,index[key][key2])
                  if (key2=="Name"):
                      name=index[key][key2]
                  if (key2=="file"):
                      file=index[key][key2]
                  if (key2=="thumb"):
                      thumb=index[key][key2]
                  if (key2=="uuid"):
                      uuid=index[key][key2]  
              html=html+'<h3>'+name+'</h3>'
              ServerIP=request.host.split(':')[0]
              html=html+'<a href="http://'+ServerIP+'/Video/'+file+'">'
              html=html+'<img src="https://storage.googleapis.com/flix-bucket/myflixpictures/'+thumb+'" width="320" height="240">'
              html=html+"</a>"        
              print("=======================")

    return html


if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')