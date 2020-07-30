from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm
from sklearn import linear_model
from flask import Flask
from flask_cors import CORS
import data1
#import json
import pickle

#import random

app = Flask(__name__)

CORS(app)

'''
AP Chem, AP Psych, AP Physics C Mech, AP Physics C Elec, MBTI: 1 -- INTJ, 2 -- ESFP
Major list (Output1) & strength (Output2)
	1: Physics   1: Strong
	2: Psych     2: Medium
	3: Chem      3: Weak
'''
filename = 'model_source_major.sav'
filename2 = "cv_model_vectorizer.pickle_major"

def major_training():
	input_data = ['score1', 'score2', 'score3', 'score4', 'score5', 'score6', 'score7']
	cv = CountVectorizer()
	input_ = cv.fit_transform(input_data).toarray()
	output1 = [1, 1, 2, 1, 3, 2, 2]
	model = svm.SVC()
	model.fit(input_, output1)
	filename = 'model_source_major.sav'
	filename2 = "cv_model_vectorizer.sav"
	pickle.dump(model, open(filename, 'wb'))
	pickle.dump(cv, open(filename2, "wb"))

testML = ['3, 2, 0, 0, 2']
@app.route("/majorfit/<profile>")
def major_prediction(profile):
	test = profile
	filename = 'model_source_major.sav'
	filename2 = "cv_model_vectorizer.sav"
	loaded_model = pickle.load(open(filename, 'rb'))
	cv = pickle.load(open(filename2, "rb"))
	majorresult = loaded_model.predict(cv.transform(test).toarray())
	print(majorresult)
	return(str(majorresult[0]))

major_training()
major_prediction(testML)
