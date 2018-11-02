# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 23:49:14 2018

@author: Heller
"""
import copy
from backmain import intro, rules, module, wordbreak
from flask import Flask, render_template, request, jsonify
from PyDictionary import PyDictionary
import pyttsx3
from textblob import Word
app = Flask(__name__)
global a


@app.route('/')
def result_sentence():
    global a
    a=0
    return render_template('index.html')

    
@app.route('/get_meaning')
def get_meaning():
    j=0;
    reply="";
    user_dicint=request.args.get('message')
    dictionary=PyDictionary();
    meaning=dictionary.meaning(user_dicint)
    if meaning is None:
        reply=" Word not found in our dictionary "
    else:
        for i in meaning:
            reply=reply+i+" : "+str(meaning[i][0])+"<br> <br>"
            print (reply)
            if(j==1):
                break
            j=j+1
        if(reply==""):
            user_dicint="Word not found"
    return jsonify({'html': reply, 'user_int': user_dicint.upper()})
  
@app.route('/get_pronun')
def get_pronun():
    user_word=request.args.get('message')
    reply=wordbreak(user_word)
    return jsonify({'html': reply, 'user_int': user_word})
    
@app.route('/get_reply')
def get_reply():
    global a
    global b
    reply = "";
    user_int = request.args.get('message')
    if(user_int.lower()=="111"):
        a=1
        user_int="start"
    
    if(user_int.lower()=="222"):
        if(a==3):
            a=1
            user_int="start"
        if(a==4):
            a=2
            user_int=b
    if (user_int.lower() == "hi" and a == 0):
        reply = intro()
        a = 1;
    elif (user_int.lower() == "start" or a == 2):
        b=copy.copy(user_int)
        a, reply = rules(a, user_int)
    elif (a == 3):
        a, reply = module(a, user_int)
    return jsonify({'html': reply, 'user_int': user_int})
@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r
if __name__ == '__main__':
    app.debug = True
    app.run()
