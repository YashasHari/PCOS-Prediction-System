import numpy as np
import nltk
from sklearn.datasets import load_files
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
#nltk.download('stopwords')
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import VotingClassifier
from sklearn import model_selection
from sklearn.svm import SVC
import warnings
from nltk.tokenize import word_tokenize
import string 
from nltk.stem import WordNetLemmatizer
import sqlite3
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from random import seed
from random import randrange
from csv import reader
import csv
from pandas import read_csv
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
def process():
    df = pd.read_csv('data/fake_job_postings_cleaned.csv')

    X = df['text']
    y = df['fraudulent']
    cv = CountVectorizer(stop_words='english')
    X = cv.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=53)


    nb_classifier = MultinomialNB()
    nb_classifier.fit(X_train, y_train)
    pred = nb_classifier.predict(X_test)
    mse=mean_squared_error(y_test, pred)
    mae=mean_absolute_error(y_test, pred)
    r2=r2_score(y_test, pred)


    print("---------------------------------------------------------")
    print("MSE VALUE FOR Naviebayes IS %f "  % mse)
    print("MAE VALUE FOR Naviebayes IS %f "  % mae)
    print("R-SQUARED VALUE FOR Naviebayes IS %f "  % r2)
    rms = np.sqrt(mean_squared_error(y_test, pred))
    print("RMSE VALUE FOR Naviebayes IS %f "  % rms)
    ac=accuracy_score(y_test,pred)
    print ("ACCURACY VALUE Naviebayes IS %f" % ac)
    print("---------------------------------------------------------")


    result2=open('results/MNBMetrics.csv', 'w')
    result2.write("Parameter,Value" + "\n")
    result2.write("MSE" + "," +str(mse) + "\n")
    result2.write("MAE" + "," +str(mae) + "\n")
    result2.write("R-SQUARED" + "," +str(r2) + "\n")
    result2.write("RMSE" + "," +str(rms) + "\n")
    result2.write("ACCURACY" + "," +str(ac) + "\n")
    result2.close()


    df =  pd.read_csv('results/MNBMetrics.csv')
    acc = df["Value"]
    alc = df["Parameter"]
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
    explode = (0.1, 0, 0, 0, 0)  

    fig = plt.figure()
    plt.bar(alc, acc,color=colors)
    plt.xlabel('Parameter')
    plt.ylabel('Value')
    plt.title('Naviebayes Metrics Value')
    fig.savefig('results/MNBMetricsValue.png') 
    plt.pause(5)
    plt.show(block=False)
    plt.close()

    clf_log = SGDClassifier(loss='log').fit(X_train, y_train)
    pred_log = clf_log.predict(X_test)
    mse=mean_squared_error(y_test, pred_log)
    mae=mean_absolute_error(y_test, pred_log)
    r2=r2_score(y_test, pred_log)


    print("---------------------------------------------------------")
    print("MSE VALUE FOR SGDClassifier IS %f "  % mse)
    print("MAE VALUE FOR SGDClassifier IS %f "  % mae)
    print("R-SQUARED VALUE FOR SGDClassifier IS %f "  % r2)
    rms = np.sqrt(mean_squared_error(y_test, pred_log))
    print("RMSE VALUE FOR SGDClassifier IS %f "  % rms)
    ac=accuracy_score(y_test,pred_log)
    print ("ACCURACY VALUE SGDClassifier IS %f" % ac)
    print("---------------------------------------------------------")


    result2=open('results/SGDMetrics.csv', 'w')
    result2.write("Parameter,Value" + "\n")
    result2.write("MSE" + "," +str(mse) + "\n")
    result2.write("MAE" + "," +str(mae) + "\n")
    result2.write("R-SQUARED" + "," +str(r2) + "\n")
    result2.write("RMSE" + "," +str(rms) + "\n")
    result2.write("ACCURACY" + "," +str(ac) + "\n")
    result2.close()


    df =  pd.read_csv('results/SGDMetrics.csv')
    acc = df["Value"]
    alc = df["Parameter"]
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
    explode = (0.1, 0, 0, 0, 0)  

    fig = plt.figure()
    plt.bar(alc, acc,color=colors)
    plt.xlabel('Parameter')
    plt.ylabel('Value')
    plt.title('SGDClassifier Value')
    fig.savefig('results/SGDMetricsValue.png') 
    plt.pause(5)
    plt.show(block=False)
    plt.close()

    #Cleaning data

    #Model creation
    seed = 7
    kfold = model_selection.KFold(n_splits=10)
    estimators = []
    model1 = LogisticRegression()
    estimators.append(('logistic', model1))
    model2 = RandomForestClassifier()
    estimators.append(('cart', model2))
    model3 = SVC()
    estimators.append(('svm', model3))
    model4 = SGDClassifier(loss="hinge", penalty="l2", max_iter=5)
    estimators.append(('sgd', model4))

    warnings.simplefilter("ignore")
    # create the ensemble model
    classifier= VotingClassifier(estimators)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    mse=mean_squared_error(y_test, y_pred)
    mae=mean_absolute_error(y_test, y_pred)
    r2=r2_score(y_test, y_pred)


    print("---------------------------------------------------------")
    print("MSE VALUE FOR VotingClassifier IS %f "  % mse)
    print("MAE VALUE FOR VotingClassifier IS %f "  % mae)
    print("R-SQUARED VALUE FOR VotingClassifier IS %f "  % r2)
    rms = np.sqrt(mean_squared_error(y_test, y_pred))
    print("RMSE VALUE FOR VotingClassifier IS %f "  % rms)
    ac=accuracy_score(y_test,y_pred)
    print ("ACCURACY VALUE VotingClassifier IS %f" % ac)
    print("---------------------------------------------------------")


    result2=open('results/VCMetrics.csv', 'w')
    result2.write("Parameter,Value" + "\n")
    result2.write("MSE" + "," +str(mse) + "\n")
    result2.write("MAE" + "," +str(mae) + "\n")
    result2.write("R-SQUARED" + "," +str(r2) + "\n")
    result2.write("RMSE" + "," +str(rms) + "\n")
    result2.write("ACCURACY" + "," +str(ac) + "\n")
    result2.close()


    df =  pd.read_csv('results/VCMetrics.csv')
    acc = df["Value"]
    alc = df["Parameter"]
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
    explode = (0.1, 0, 0, 0, 0)  

    fig = plt.figure()
    plt.bar(alc, acc,color=colors)
    plt.xlabel('Parameter')
    plt.ylabel('Value')
    plt.title('VotingClassifier Metrics Value')
    fig.savefig('results/VCMetricsValue.png') 
    plt.pause(5)
    plt.show(block=False)
    plt.close()
process()
