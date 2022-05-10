from django.shortcuts import render
from django.http import HttpResponse, request
from .models import *

from sklearn.naive_bayes import BernoulliNB
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC

from .Predict import getprediction

import xlrd
import numpy as np
import pandas as pd
import sys
import time
from sklearn import metrics
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
import matplotlib.pyplot as plt;
#from .urlaction import URLCheck
#from .Prediction import predict_nn


# Create your views here.
def home(request):
	return render(request, 'index.html')
def userlogin(request):
	return render(request, 'user.html')
def uregistraction(request):
	return render(request, 'ureg.html')
def uregaction(request):
	email=request.POST['mail']
	pwd=request.POST['pwd']
	zip=request.POST['zip']
	name=request.POST['name']
	age=request.POST['age']
	gen=request.POST['gen']

		
	d=user.objects.filter(email__exact=email).count()
	if d>0:
		return render(request, 'ureg.html',{'msg':"Email Already Registered"})
	else:
		d=user(name=name,email=email,pwd=pwd,zip=zip,gender=gen,age=age)
		d.save()
		return render(request, 'ureg.html',{'msg':"Register Success, You can Login.."})

	return render(request, 'ureg.html',{'msg':"Register Success, You can Login.."})


def ulogin(request):
	uid=request.POST['uid']
	pwd=request.POST['pwd']
	d=user.objects.filter(email__exact=uid).filter(pwd__exact=pwd).count()
		
	if d>0:
		d=user.objects.filter(email__exact=uid)
		request.session['email']=uid
		return render(request, 'uhome.html',{'data': d[0]})

	else:
		return render(request, 'user.html',{'msg':"Login Fail"})

def uhome(request):
	return render(request, 'uhome.html')

def ulogout(request):
	try:
		del request.session['email']
	except:
		pass
	return render(request, 'user.html')

	
def adminhomedef(request):
	if "adminid" in request.session:
		uid=request.session["adminid"]
		return render(request, 'admin_home.html')

	else:
		return render(request, 'admin.html')

	
def uhome(request):
	return render(request, 'uhome.html')
def newssearch(request):
	if "email" in request.session:
		return render(request, 'search.html')

	else:
		return render(request, 'user.html')

def adminlogoutdef(request):
	try:
		del request.session['adminid']
	except:
		pass
	return render(request, 'admin.html')	
	
def adminlogindef(request):
	return render(request, 'admin.html')

def adminloginactiondef(request):
	if request.method=='POST':
		uid=request.POST['uid']
		pwd=request.POST['pwd']
		
		if uid=='admin' and pwd=='admin':
			request.session['adminid']='admin'
			return render(request, 'admin_home.html')

		else:
			return render(request, 'admin.html',{'msg':"Login Fail"})

	else:
		return render(request, 'admin.html')
def uploaddataset(request):
	if "adminid" in request.session:
		

		return render(request, 'upload.html')

	else:
		return render(request, 'admin.html')
def xlupload(request):
	if "adminid" in request.session:
		file=request.POST['file']
		file=file
		book = xlrd.open_workbook(file)
		sheet = book.sheet_by_index(0)
		dataset.objects.all().delete()
		for r in range(1, sheet.nrows):
			f0 = sheet.cell(r, 0).value
			f1 = sheet.cell(r, 1).value
			f2 = sheet.cell(r, 2).value
			f3 = sheet.cell(r, 3).value
			f4 = sheet.cell(r, 4).value
			f5 = sheet.cell(r, 5).value
			f6 = sheet.cell(r, 6).value
			f7 = sheet.cell(r, 7).value
			f8 = sheet.cell(r, 8).value
			f9 = sheet.cell(r, 9).value
			f10 = sheet.cell(r, 10).value
			f11 = sheet.cell(r, 11).value
			f12 = sheet.cell(r, 12).value
			f13 = sheet.cell(r, 13).value
			f14 = sheet.cell(r, 14).value
			f15 = sheet.cell(r, 15).value
			f16 = sheet.cell(r, 16).value
			res = sheet.cell(r, 17).value
			d=dataset(v1=f0,v2=f1,v3=f2,v4=f3,v5=f4,v6=f5,v7=f6,v8=f7,v9=f8,v10=f9,v11=f10,v12=f11,v13=f12,v14=f13,v15=f14,v16=f15,v17=f16,res=res)
			d.save()
		return render(request, 'upload.html',{'msg':"Dataset Uploaded Successfully"})
	else:
		return render(request, 'admin.html')

def predictions(request):
	if "adminid" in request.session:
		
		return render(request, 'predictions.html')

	else:
		return render(request, 'admin.html')
def nntest(request):
	if "adminid" in request.session:
		return render(request, 'nntest.html')

	else:
		return render(request, 'admin.html')
def naivetest(request):
	if "adminid" in request.session:
		return render(request, 'naivetest.html')
	else:
		return render(request, 'admin.html')

def svmtest(request):
	if "adminid" in request.session:
		return render(request, 'svmtest.html')
	else:
		return render(request, 'admin.html')



def naiveprediction(request):
	if "adminid" in request.session:
		
		file=request.POST['tfile']
		file=file
		trainset = []
		y_train = []
		trainset.clear()
		y_train.clear()
            
		data=dataset.objects.all()
		for d in data:
			x_train = []
			x_train.clear()
			x_train.append(float(d.v1))
			x_train.append(float(d.v2))
			x_train.append(float(d.v3))
			x_train.append(float(d.v4))
			x_train.append(float(d.v5))
			x_train.append(float(d.v6))
			x_train.append(float(d.v7))
			x_train.append(float(d.v8))
			x_train.append(float(d.v9))
			x_train.append(float(d.v10))
			x_train.append(float(d.v11))
			x_train.append(float(d.v12))
			x_train.append(float(d.v13))
			x_train.append(float(d.v14))
			x_train.append(float(d.v15))
			x_train.append(float(d.v16))
			x_train.append(float(d.v17))
			
			y_train.append([d.res])
			trainset.append(x_train)

                
			#print(d.v1,d.v2)
		trainset = np.array(trainset)
		y_train = np.array(y_train)
		tf = pd.read_csv(file)
		print(tf)
		url = tf['URL']
		U1 = np.array(url)
		res = tf['Result']
		R1 = np.array(res)
		tf = tf.drop(['URL'], 1)
		tf = tf.drop(['Result'], 1)
		testdata = np.array(tf)
		print(testdata)
		testdata = testdata.reshape(len(testdata), -1)
		nv = BernoulliNB()
		nv.fit(trainset, y_train)
		s = time.clock()
		result = nv.predict(testdata)  # Predicting 
		print(result)
		
		act=[]
		for r in R1:
			r=float(r)
			act.append(str(r))

		print(act,'<<<<<<<<<<<<<<<<<<<<<<<<<<')
		accuracy = accuracy_score(act, result)
		f1=f1_score(act, result, pos_label='0.0')
		print(f1,'F1111111111111111111111111111111111111111111111111111111111111')
		accuracy=int(accuracy*100)
		print(accuracy,'Acuracy')

		#s=graph.objects.update(naive=accuracy)
		s=graph2.objects.all().delete()
		d=graph2(naive=accuracy,nn=0,svm=0)
		d.save()
		
                
		return render(request, 'nbresults.html',{'msg':accuracy})

	else:
		return render(request, 'admin.html')


def svmprediction(request):
	if "adminid" in request.session:
		
		
		file=request.POST['tfile']
		file=file
		trainset = []
		y_train = []
		trainset.clear()
		y_train.clear()
            
		data=dataset.objects.all()
		for d in data:
			x_train = []
			x_train.clear()
			x_train.append(float(d.v1))
			x_train.append(float(d.v2))
			x_train.append(float(d.v3))
			x_train.append(float(d.v4))
			x_train.append(float(d.v5))
			x_train.append(float(d.v6))
			x_train.append(float(d.v7))
			x_train.append(float(d.v8))
			x_train.append(float(d.v9))
			x_train.append(float(d.v10))
			x_train.append(float(d.v11))
			x_train.append(float(d.v12))
			x_train.append(float(d.v13))
			x_train.append(float(d.v14))
			x_train.append(float(d.v15))
			x_train.append(float(d.v16))
			x_train.append(float(d.v17))
			
			y_train.append([d.res])
			trainset.append(x_train)

                
			#print(d.v1,d.v2)
		trainset = np.array(trainset)
		y_train = np.array(y_train)
		tf = pd.read_csv(file)
		print(tf)
		url = tf['URL']
		U1 = np.array(url)
		res = tf['Result']
		R1 = np.array(res)
		tf = tf.drop(['URL'], 1)
		tf = tf.drop(['Result'], 1)
		testdata = np.array(tf)
		print(testdata)
		testdata = testdata.reshape(len(testdata), -1)
		from sklearn import svm


		nv = svm.SVC()
		nv.fit(trainset, y_train)
		s = time.clock()
		result = nv.predict(testdata)  # Predicting 
		print(result)
		
		act=[]
		for r in R1:
			r=float(r)
			act.append(str(r))

		print('<<<<<<<<<<<<<<<<<<<<<<<<<<')
		accuracy = accuracy_score(act, result)
		f1=f1_score(act, result, pos_label='0.0')
		print(accuracy,'Acuracy')
		print(f1,'F1111111111111111111111111111111111111111111111111111111111111')
		accuracy=int(accuracy*100)
		s=graph2.objects.update(svm=accuracy)
		#d=graph2(naive=accuracy,nn=0)
		d.save()
		
                
		return render(request, 'svmresults.html',{'msg':accuracy})

	else:
		return render(request, 'admin.html')


def nnprediction(request):
	if "adminid" in request.session:
		
		
		file=request.POST['tfile']
		file=file
		trainset = []
		y_train = []
		trainset.clear()
		y_train.clear()
            
		data=dataset.objects.all()
		for d in data:
			x_train = []
			x_train.clear()
			x_train.append(float(d.v1))
			x_train.append(float(d.v2))
			x_train.append(float(d.v3))
			x_train.append(float(d.v4))
			x_train.append(float(d.v5))
			x_train.append(float(d.v6))
			x_train.append(float(d.v7))
			x_train.append(float(d.v8))
			x_train.append(float(d.v9))
			x_train.append(float(d.v10))
			x_train.append(float(d.v11))
			x_train.append(float(d.v12))
			x_train.append(float(d.v13))
			x_train.append(float(d.v14))
			x_train.append(float(d.v15))
			x_train.append(float(d.v16))
			x_train.append(float(d.v17))
			
			y_train.append([d.res])
			trainset.append(x_train)

                
			#print(d.v1,d.v2)
		trainset = np.array(trainset)
		y_train = np.array(y_train)
		tf = pd.read_csv(file)
		url = tf['URL']
		U1 = np.array(url)
		res = tf['Result']
		R1 = np.array(res)
		tf = tf.drop(['URL'], 1)
		tf = tf.drop(['Result'], 1)
		testdata = np.array(tf)
		testdata = testdata.reshape(len(testdata), -1)
		nv = MLPClassifier()
		nv.fit(trainset, y_train)
		s = time.clock()
		result = nv.predict(testdata)  # Predicting 
		print(result)
		
		act=[]
		for r in R1:
			r=float(r)
			act.append(str(r))

		print(act,'<<<<<<<<<<<<<<<<<<<<<<<<<<')
		accuracy = accuracy_score(act, result)
		f1=f1_score(act, result, pos_label='0.0')
		print(accuracy,'Acuracy')
		print(f1,'F1111111111111111111111111111111111111111111111111111111111111')
		accuracy=int(accuracy*100)
		s=graph2.objects.update(nn=accuracy)
               
		return render(request, 'nnresults.html',{'msg':accuracy})
	else:
		return render(request, 'admin.html')

def graphview(request):
	if "adminid" in request.session:
		performance=[]
		row=graph2.objects.all()
		for r in row:
			performance.append(r.naive)
			performance.append(r.nn)
			performance.append(r.svm)
		objects = ('Naive Bayes','Neural Network','SVM')
		y_pos = np.arange(len(objects))
		print(performance)
		plt.bar(y_pos, performance, align='center', alpha=0.5)
		plt.xticks(y_pos, objects)
		plt.ylabel('Accuracy %')
		plt.title('Performance Algorithms')
		plt.savefig('graph.png')
		from PIL import Image
		im = Image.open('graph.png')
		im.show()
				
	return render(request, 'predictions.html')

def viewpprofile(request):
	if "email" in request.session:
		uid=request.session["email"]
		d=user.objects.filter(email__exact=uid)
		return render(request, 'viewpprofile.html',{'data': d[0]})

	else:
		return render(request, 'user.html')

def tweetssearch(request):

	if request.method=='POST':
		keys=request.POST['keys']

		'''if(str(keys).startswith("https")):
			x = "Not a phising website"
		else:
			x = "phising website"'''
    			

		from .GetTweets import GetTweets
		GetTweets.get(keys)
		
		print('Tweets collected')

		d = tweets.objects.filter().all()

		resu="No URL"
		for d1 in d:
			sno=d1.id
			url=''
			tw=d1.tweet
			uid=d1.userid
			tw2=''

			
			
			for line in tw.splitlines():
				tw2=tw2+' '+line

			#print(tw2)
			res=extracturl(tw2)
			#print(res,'------------------------------')
			if res==None:
				pass
			else:
				url=str(res[1])
				url=url.strip()
				print(type(url))
				print(url,'=====Extracted')

				
				try:
					
					if 'twitter' in url:
						resu='L'
						print('in if1')
					else:
						
						print('in else1')
						if 'https' in url:
							url=request.head(url).headers['location']
							print(url,']]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]')
							resu='L'
						elif 'http' in url:
							url=url
							print(url,'******************************************************')
							resu=getprediction(url)
							if resu=='P':
								d33=malwarebots(userid=uid)
								d33.save()
								dd=tweets.objects.filter(id = sno).update(status = 'Phishing')
								dd.save()
								
							else:
								print('in elseeeeeeeeeeeeeeeeeeeeeeeeeeee')


						print(resu)

				except:
					exception_type, exception_object, exception_traceback = sys.exc_info()
					filename = exception_traceback.tb_frame.f_code.co_filename
					line_number = exception_traceback.tb_lineno
					print("Exception type: ", exception_type)
					print("File name: ", filename)
					print("Line number: ", line_number)
        
					resu='L'
			print(resu)
		d = tweets.objects.filter().all()
		return render(request, 'results.html',{'tweets': d})
	else:
		return render(request, 'tweetssearch.html')

def extracturl(tweet):
	import re
	res=re.search("(?P<url>https?://[^\s]+)", tweet)
	return res


def viewmalw(request):
	d=malwarebots.objects.order_by().values('userid').distinct()
	return render(request, 'viewmal.html',{'tweets': d})
