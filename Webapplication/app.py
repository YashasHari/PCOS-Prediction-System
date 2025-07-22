from flask_socketio import SocketIO, send, join_room
from flask import Flask, flash, redirect, render_template, request, session, abort,url_for
import os
#import StockPrice as SP
import re
import sqlite3
import pandas as pd
import numpy as np

from PIL import Image, ImageTk

import time 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

      
@app.route('/')
#loading login page or main chat page
def index():
        if not session.get('logged_in'):
                return render_template("index.html")
        else:
                return render_template('main.html')


        
@app.route('/loginpage')
def log_page():
    return render_template("login.html")
@app.route('/ahome')
def ahome_page():
    return render_template("main.html")
@app.route('/performance')
def performance_page():
    return render_template("performance.html")
@app.route('/loginaction', methods=['POST']) 
def log_action():
    uname=request.form['uname']
    passw=request.form['pass']
    if uname=="admin":
        if passw=="admin":
            session['uname']=uname
            session['logged_in']=True
            return redirect(url_for('index'))
        else:
            return render_template("index.html",msg="Incorret Password")
    else:
        return render_template("index.html",msg="Incorret User name")
@app.route("/predict",methods=['POST'])
def predict():
    age=request.form['age']
    weight=request.form['weight']
    hig=request.form['hig']
    bmi=request.form['bmi']
    bg=request.form['bg']
    pr=request.form['pr']
    rr=request.form['rr']
    hb=request.form['hb']
    cycle=request.form['cycle']
   
    cl=request.form['cl']
    ms=request.form['ms']
    prg=request.form['prg']
    abort=request.form['abort']
    ibhcg=request.form['ibhcg']
    iibhcg=request.form['iibhcg']
    fsh=request.form['fsh']
    lh=request.form['lh']
    FSHLH=request.form['FSHLH']
    hip=request.form['hip']
    Waist=request.form['Waist']
    
    whratio=request.form['whratio']
    tsh=request.form['tsh']
    amh=request.form['amh']
    prl=request.form['prl']
    vitd3=request.form['vitd3']
    pgr=request.form['pgr']
    rbs=request.form['rbs']
    wg=request.form['wg']
    hg=request.form['hg']
    sd=request.form['sd']
    hl=request.form['hl']
    pim=request.form['pim']
    ff=request.form['ff']
    rexe=request.form['re']
    sbp=request.form['sbp']
    dbp=request.form['dbp']
    fnol=request.form['fnol']
    fnor=request.form['fnor']
    afsl=request.form['afsl']
    afsr=request.form['afsr']
    endo=request.form['endo']
    
    data=pd.read_csv("data.csv")    
    X=data.drop(["PCOS (Y/N)","Sl. No","Patient File No."],axis = 1) #droping out index from features too
    y=data["PCOS (Y/N)"]


    #Splitting the data into test and training sets

    X_train,X_test, y_train, y_test = train_test_split(X,y, test_size=0.3)
    #Fitting the RandomForestClassifier to the training set

    rfc = RandomForestClassifier()
    rfc.fit(X_train, y_train)
    x_text=[float(age),float(weight),float(hig),float(bmi),float(bg),float(pr),float(rr),float(hb),float(cycle),float(cl),float(ms),float(prg),float(abort),float(ibhcg),float(iibhcg),float(fsh),float(lh),float(FSHLH),float(hip),float(Waist),float(whratio),float(tsh),float(amh),float(prl),float(vitd3),float(pgr),float(rbs),float(wg),float(hg),float(sd),float(hl),float(pim),float(ff),float(rexe),float(sbp),float(dbp),float(fnol),float(fnor),float(afsl),float(afsr),float(endo)]
    inputdata=x_text
    x_text=np.array(x_text)
    x_text=x_text.reshape(1, -1)
    res=rfc.predict(x_text)
    msg=""
    if res[0]==0:
        msg="No disease"
    else:
        msg="You have infected by POCOS"

    print("Result==",res)
    print("Message",msg)
    return render_template("main.html",result=msg,inputdata=inputdata)

    

        
@app.route("/logout")
def log_out():
    session.clear()
    return redirect(url_for('index'))
    



  
  
if __name__ == '__main__':
    socketio.run(app,debug=True,host='127.0.0.1', port=5000)
