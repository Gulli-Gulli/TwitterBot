from django.db import models

# Create your models here.
class user(models.Model):
	name=models.CharField(max_length=100);
	email=models.CharField(max_length=100);
	pwd=models.CharField(max_length=100);
	zip=models.CharField(max_length=100);
	gender=models.CharField(max_length=100);
	age=models.CharField(max_length=100);



class dataset(models.Model):
	v1=models.CharField(max_length=10);
	v2=models.CharField(max_length=10);
	v3=models.CharField(max_length=10);
	v4=models.CharField(max_length=10);
	v5=models.CharField(max_length=10);
	v6=models.CharField(max_length=10);
	v7=models.CharField(max_length=10);
	v8=models.CharField(max_length=10);
	v9=models.CharField(max_length=10);
	v10=models.CharField(max_length=10);
	v11=models.CharField(max_length=10);
	v12=models.CharField(max_length=10);
	v13=models.CharField(max_length=10);
	v14=models.CharField(max_length=10);
	v15=models.CharField(max_length=10);
	v16=models.CharField(max_length=10);
	v17=models.CharField(max_length=10);
	res=models.CharField(max_length=10);

class graph2(models.Model):
	naive=models.FloatField(max_length=1000)
	nn=models.FloatField(max_length=1000)
	svm=models.FloatField(max_length=1000)
	
class tweets(models.Model):
	tweet=models.CharField(max_length=10000);
	userid=models.CharField(max_length=1000);
	status=models.CharField(max_length=100);

class dtweets(models.Model):
	tweet=models.CharField(max_length=500);
	userid=models.CharField(max_length=1000);
	
class malwarebots(models.Model):
	userid=models.CharField(max_length=500);
	
