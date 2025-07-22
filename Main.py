import tkinter as tk
from tkinter import Message ,Text
from PIL import Image, ImageTk
import pandas as pd
from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as font
import tkinter.messagebox as tm
import matplotlib.pyplot as plt
import csv
import numpy as np
from PIL import Image, ImageTk
from tkinter import filedialog
import tkinter.messagebox as tm
import preprocess as pre
import Logisticregression as LR
import RF as RF
import DT as dt
import adaboost as ada
import GB as gb
import LGBM as lgbm
import MLP as mlp
import KNN as knn

bgcolor="#DAF7A6"
bgcolor1="#B7C526"
fgcolor="black"


def Home():
        global window
        def clear():
            print("Clear1")
            txt.delete(0, 'end')    
            
  



        window = tk.Tk()
        window.title("DIAGNOSIS OF  POLYCYSTIC OVARY SYNDROME USING MACHINE LEARNING ALGORITHMS")
        
 
        window.geometry('1580x960')
        window.configure(background=bgcolor)
        #window.attributes('-fullscreen', True)

        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)
        

        message1 = tk.Label(window, text="DIAGNOSIS OF  POLYCYSTIC OVARY SYNDROME USING ML" ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=2,font=('times', 30, 'italic bold underline')) 
        message1.place(x=100, y=1)

        lbl = tk.Label(window, text="Dataset",width=10  ,height=1  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl.place(x=1, y=100)
        
        txt = tk.Entry(window,width=10,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt.place(x=200, y=110)
        lbl1 = tk.Label(window, text="Age",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl1.place(x=1, y=150)

        txt1 = tk.Entry(window,width=5,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt1.place(x=200, y=165)

        lbl2 = tk.Label(window, text="Weight (Kg)",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl2.place(x=1, y=200)

        txt2 = tk.Entry(window,width=5,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt2.place(x=200, y=215)

        lbl3 = tk.Label(window, text="Height(Cm)",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl3.place(x=1, y=300)

        txt3 = tk.Entry(window,width=5,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt3.place(x=200, y=315)

        lbl4 = tk.Label(window, text="BMI",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl4.place(x=1, y=350)

        txt4 = tk.Entry(window,width=5,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt4.place(x=200, y=365)

        lbl5 = tk.Label(window, text="Blood Group",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl5.place(x=1, y=400)

        txt5 = tk.Entry(window,width=5,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt5.place(x=200, y=415)



        lbl6 = tk.Label(window, text="Pulse rate(bpm)",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl6.place(x=1, y=450)

        txt6 = tk.Entry(window,width=5,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt6.place(x=200, y=465)

        lbl7 = tk.Label(window, text="RR (breaths/min)",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl7.place(x=1, y=500)

        txt7 = tk.Entry(window,width=5,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt7.place(x=200, y=515)

        lbl8 = tk.Label(window, text="Hb(g/dl)",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl8.place(x=1, y=550)

        txt8 = tk.Entry(window,width=5,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt8.place(x=200, y=565)


        

        lbl9 = tk.Label(window, text="Cycle(R/I)",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl9.place(x=300, y=200)

        txt9 = tk.Entry(window,width=5,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt9.place(x=560, y=215)

        lbl10 = tk.Label(window, text="Cycle length(days)",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl10.place(x=300, y=250)

        txt10 = tk.Entry(window,width=5,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt10.place(x=560, y=265)


        lbl11 = tk.Label(window, text="Marraige Status (Yrs)",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl11.place(x=300, y=300)

        txt11 = tk.Entry(window,width=5,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt11.place(x=560, y=315)

        lbl12 = tk.Label(window, text="Pregnant(Y/N)",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl12.place(x=300, y=350)

        txt12 = tk.Entry(window,width=5,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt12.place(x=560, y=365)

        lbl13 = tk.Label(window, text="No. of aborptions",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl13.place(x=300, y=400)

        txt13 = tk.Entry(window,width=5,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt13.place(x=560, y=415)

        lbl14= tk.Label(window, text="I   beta-HCG(mIU/mL)",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl14.place(x=300, y=450)

        txt14 = tk.Entry(window,width=5,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt14.place(x=560, y=465)

        lbl15 = tk.Label(window, text="II    beta-HCG(mIU/mL)",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl15.place(x=300, y=500)

        txt15 = tk.Entry(window,width=5,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt15.place(x=560, y=515)

        lbl16 = tk.Label(window, text="FSH(mIU/mL)",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl16.place(x=300, y=550)

        txt16 = tk.Entry(window,width=5,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt16.place(x=560, y=565)



        lbl7 = tk.Label(window, text="LH(mIU/mL)",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl7.place(x=600, y=200)

        txt17 = tk.Entry(window,width=5,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt17.place(x=860, y=215)

        lbl18 = tk.Label(window, text="FSH/LH",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl18.place(x=600, y=250)

        txt18 = tk.Entry(window,width=5,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt18.place(x=860, y=265)


        lbl19 = tk.Label(window, text="Hip(inch)",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl19.place(x=600, y=300)

        txt19 = tk.Entry(window,width=5,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt19.place(x=860, y=315)

        lbl20 = tk.Label(window, text="Waist(inch)",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl20.place(x=600, y=350)

        txt20 = tk.Entry(window,width=5,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt20.place(x=860, y=365)

        lbl21 = tk.Label(window, text="Waist:Hip Ratio",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl21.place(x=600, y=400)

        txt21 = tk.Entry(window,width=5,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt21.place(x=860, y=415)

        lbl22= tk.Label(window, text="TSH (mIU/L)",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl22.place(x=600, y=450)

        txt22 = tk.Entry(window,width=5,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt22.place(x=860, y=465)

        lbl23 = tk.Label(window, text="AMH(ng/mL)",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl23.place(x=600, y=500)

        txt23 = tk.Entry(window,width=5,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt23.place(x=860, y=515)
        
        lbl24 = tk.Label(window, text="PRL(ng/mL)",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl24.place(x=600, y=500)

        txt24 = tk.Entry(window,width=5,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt24.place(x=860, y=515)
        
        lbl25 = tk.Label(window, text="Vit D3 (ng/mL)",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl25.place(x=600, y=550)

        txt25 = tk.Entry(window,width=5,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt25.place(x=860, y=565)



        lbl26 = tk.Label(window, text="PRG(ng/mL)",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl26.place(x=900, y=150)

        txt26 = tk.Entry(window,width=5,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt26.place(x=1160, y=165)

        lbl27 = tk.Label(window, text="RBS(mg/dl)",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl27.place(x=900, y=200)

        txt27 = tk.Entry(window,width=5,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt27.place(x=1160, y=215)

        lbl28 = tk.Label(window, text="Weight gain(Y/N)",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl28.place(x=900, y=250)

        txt28 = tk.Entry(window,width=5,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt28.place(x=1160, y=265)

        lbl29= tk.Label(window, text="hair growth(Y/N)",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl29.place(x=900, y=300)

        txt29 = tk.Entry(window,width=5,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt29.place(x=1160, y=315)

        lbl30 = tk.Label(window, text="Skin darkening (Y/N)",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl30.place(x=900, y=350)

        txt30 = tk.Entry(window,width=5,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt30.place(x=1160, y=365)
        
        lbl31 = tk.Label(window, text="Hair loss(Y/N)",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl31.place(x=900, y=400)

        txt31 = tk.Entry(window,width=5,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt31.place(x=1160, y=415)
        
        lbl32 = tk.Label(window, text="Pimples(Y/N)",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl32.place(x=900, y=450)

        txt33 = tk.Entry(window,width=5,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt33.place(x=1160, y=465)
        lbl34 = tk.Label(window, text="Fast food (Y/N)",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl34.place(x=900, y=500)

        txt34 = tk.Entry(window,width=5,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt34.place(x=1160, y=515)

        lbl35 = tk.Label(window, text="Reg.Exercise(Y/N)",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl35.place(x=900, y=550)

        txt35 = tk.Entry(window,width=5,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt35.place(x=1160, y=565)
        
        lbl36 = tk.Label(window, text="BP _Systolic (mmHg)",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl36.place(x=900, y=600)

        txt36 = tk.Entry(window,width=5,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt36.place(x=1160, y=615)
        
        lbl37 = tk.Label(window, text="BP _Diastolic (mmHg)",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl37.place(x=900, y=650)

        txt37 = tk.Entry(window,width=5,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt37.place(x=1160, y=665)
        
        lbl38 = tk.Label(window, text="Follicle No. (L)",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl38.place(x=1200, y=150)

        txt38 = tk.Entry(window,width=5,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt38.place(x=1460, y=165)
        lbl39 = tk.Label(window, text="Follicle No. (R)",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl39.place(x=1200, y=200)

        txt39 = tk.Entry(window,width=5,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt39.place(x=1460, y=215)
        lbl40 = tk.Label(window, text="Avg. F size (L) (mm)",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl40.place(x=1200, y=250)

        txt40 = tk.Entry(window,width=5,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt40.place(x=1460, y=265)
        lbl41 = tk.Label(window, text="Avg. F size (R) (mm)",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl41.place(x=1200, y=300)

        txt41 = tk.Entry(window,width=5,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt41.place(x=1460, y=315)
        lbl42 = tk.Label(window, text="Endometrium (mm)",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl42.place(x=1200, y=350)

        txt42 = tk.Entry(window,width=5,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt42.place(x=1460, y=365)

        


        def browse():
                path=filedialog.askopenfilename()
                print(path)
                txt.delete(0, 'end')
                txt.insert('end',path)
                if path !="":
                        print(path)
                else:
                        tm.showinfo("Input error", "Select Datset")     

        
        def preproc():
                pre.process()
                print("preprocess")
                tm.showinfo("Input", "Preprocess Successfully Finished")
                
        def LRprocess():
                sym=txt.get()
                if sym != "":
                        LR.process(sym)
                        tm.showinfo("Input", "Logistic Regression Successfully Finished")
                else:
                        tm.showinfo("Input error", "Select Dataset File")

        def RFprocess():
                sym=txt.get()
                if sym != "":
                        RF.process(sym)
                        tm.showinfo("Input", "Random Forest Successfully Finished")
                else:
                        tm.showinfo("Input error", "Select Dataset File")

        def adaboostprocess():
                sym=txt.get()
                if sym != "":
                        ada.process(sym)
                        tm.showinfo("Input", "Adaboost Successfully Finished")
                else:
                        tm.showinfo("Input error", "Select Dataset File")

        def DTprocess():
                sym=txt.get()
                if sym != "":
                        dt.process(sym)
                        tm.showinfo("Input", "Decision Tree Successfully Finished")
                else:
                        tm.showinfo("Input error", "Select Dataset File")
        def GBprocess():
                sym=txt.get()
                if sym != "":
                        gb.process(sym)
                        tm.showinfo("Input", "Garient Boosting Successfully Finished")
                else:
                        tm.showinfo("Input error", "Select Dataset File")
        def LGBMprocess():
                sym=txt.get()
                if sym != "":
                        lgbm.process(sym)
                        tm.showinfo("Input", "Light Garient Boosting Successfully Finished")
                else:
                        tm.showinfo("Input error", "Select Dataset File")
        def MLPprocess():
                sym=txt.get()
                if sym != "":
                        mlp.process(sym)
                        tm.showinfo("Input", "MLP Successfully Finished")
                else:
                        tm.showinfo("Input error", "Select Dataset File")
        def KNNprocess():
                sym=txt.get()
                if sym != "":
                        knn.process(sym)
                        tm.showinfo("Input", "KNN Successfully Finished")
                else:
                        tm.showinfo("Input error", "Select Dataset File")

        def Predictprocess():
                sym=txt2.get()
                if sym != "":
                        result=PR.process(sym)
                        tm.showinfo("Input", "Prediction : " +str(result))
                else:
                        tm.showinfo("Input error", "Select Audio File")

        browse = tk.Button(window, text="Browse", command=browse  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        browse.place(x=300, y=150)

        clearButton = tk.Button(window, text="Clear", command=clear  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=1 ,activebackground = "Red" ,font=('times', 15, ' bold '))
        clearButton.place(x=600, y=150)
         
        proc = tk.Button(window, text="Preprocess", command=preproc  ,fg=fgcolor   ,bg=bgcolor1   ,width=14  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        proc.place(x=10, y=600)
        

        LRbutton = tk.Button(window, text="LogisticRegression", command=LRprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=14  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        LRbutton.place(x=180, y=600)


        RFbutton = tk.Button(window, text="RandomForest", command=RFprocess  ,fg=fgcolor   ,bg=bgcolor1 ,width=14  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        RFbutton.place(x=355, y=600)

        SVMbutton = tk.Button(window, text="AdaBoost", command=adaboostprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=14  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        SVMbutton.place(x=525, y=600)

        SVM1button = tk.Button(window, text="Decision Tree", command=DTprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=16  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        SVM1button.place(x=700, y=600)

        PRbutton1 = tk.Button(window, text="GB", command=GBprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=14  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        PRbutton1.place(x=10, y=650)

        RFbutton1 = tk.Button(window, text="LGBM", command=LGBMprocess  ,fg=fgcolor   ,bg=bgcolor1 ,width=14  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        RFbutton1.place(x=180, y=650)

        SVMbutton1 = tk.Button(window, text="MLP", command=MLPprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=14  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        SVMbutton1.place(x=355, y=650)

        SVM1button1 = tk.Button(window, text="KNN", command=KNNprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=16  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        SVM1button1.place(x=525, y=650)

        

        quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg=fgcolor   ,bg=bgcolor1  ,width=15  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        quitWindow.place(x=700, y=650)

        window.mainloop()
Home()

