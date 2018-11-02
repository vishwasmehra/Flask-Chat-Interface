# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 15:28:15 2018

@author: Heller
"""

from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer 
from chatterbot.trainers import UbuntuCorpusTrainer 
import random
import sqlite3
import nltk
from functools import lru_cache
from itertools import product as iterprod
import pyttsx3
import os
from nltk.corpus import brown
from PyPDF2 import PdfFileReader
from nltk.sentiment.vader import SentimentIntensityAnalyzer 
import datetime
from textblob import Word
try:
    arpabet = nltk.corpus.cmudict.dict()
except LookupError:
    nltk.download('cmudict')
    arpabet = nltk.corpus.cmudict.dict()
currentTime = datetime.datetime.now()
# from docx import Document
def intro():
    greet=["Good Morning", "Good afternoon", "Good evening"]
    statement=["I am TutorBot . Here to make a master in English", "I am Tutorbot. Nice to meet you", "You just popped into my head and I thought I’d say Hi","Knock knock!!! I thought I heard a thud....just wanted to know if it was you! So Hi !!"]
    sel=" Start the course <br> Instruction to use <br> Type 111 to go the main menu <br> Type 222 to go back to previous menu"
    currentTime = datetime.datetime.now()  
    gret=""
    if currentTime.hour < 12 :
        gret=greet[0]
    elif currentTime.hour < 18 :
        gret=greet[1]
    else:
        gret=greet[2]
    reply=gret+" "+random.choice(statement)+"<br> Type 'Start' to "+sel
    return reply
def rules(a,user_int):
    level="What is your level :- <br>1- Beginner<br>2- Intermediate <br>3-Expert<br>"
    #user_in=int(user_int)
    if(a==1):
        return 2,level
    elif(a==2):
        if(user_int != "1" and user_int!="2" and user_int!="3"):
            return 2,"Please select a valid level"
        else:
            if(user_int=="1"):
                c=""
                counter=0
                for f in os.listdir("notes/"):
                    counter=counter+1
                    c=c+str(counter)+"----"+f[:-4]+"<br>"
                return 3,c
        choice=input()
        module(c,choice)
def module(c,inde):
    inde=int(inde)
    flag=0
    for f in os.listdir("notes/"):
        flag=flag+1
        if(flag==inde):
            file="notes/"+f
            with open(file) as fa:
                content = fa.readlines()
    content=[x.strip() for x in content] 
    rep=""
    for i in content:
        rep=rep+i+"<br>"
    return 4,rep
def wordbreak(s):
    s = s.lower()
    if s in arpabet:
        return arpabet[s]
    middle = len(s)/2
    partition = sorted(list(range(len(s))), key=lambda x: (x-middle)**2-x)
    for i in partition:
        pre, suf = (s[:i], s[i:])
        if pre in arpabet and wordbreak(suf) is not None:
            return [x+y for x,y in iterprod(arpabet[pre], wordbreak(suf))]
    return None