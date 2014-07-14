from django.db import models


PACKING_TYPE=(
	("S","Strip"),
	("B","Bottle"),
	("P","Packet"),
)
class Medicine(models.Model):
	medid=models.AutoField(primary_key=True)
	name=models.CharField(max_length=50)
	solution=models.CharField(max_length=100)
	company=models.CharField(max_length=50)
	packing=models.CharField(max_length=1,choices=PACKING_TYPE)
	mfg=models.DateField()
	expiry=models.DateField()
	saltinfo=models.TextField()
	price=models.DecimalField( max_digits=7, decimal_places=2)
	
	def __unicode__(self):
		return self.name+"-"+self.solution
	
class Users(models.Model):
	userid=models.AutoField(primary_key=True)
	userfname=models.CharField(max_length=50)
	userlname=models.CharField(max_length=50) 
	gender=models.CharField(max_length=1,choices=(("M","Male"),("F","Female"),))
	useremail=models.EmailField()
	userpass=models.CharField(max_length=20)
	userph=models.IntegerField()
	useradd1=models.CharField(max_length=70)
	useradd2=models.CharField(max_length=50)
	def __unicode__(self):
		return self.userfname+" "+self.userlname

	
class Orders(models.Model):
	orderid=models.AutoField(primary_key=True)
	date=models.DateField()
	shipaddress=models.CharField(max_length=200)
	def __unicode__(self):
		return str(self.orderid)
	
	
class Purchase(models.Model):
	userid=models.ForeignKey(Users)
	item=models.ForeignKey(Medicine)
	quantity=models.IntegerField()
	def __unicode__(self):
		return "User: "+str(self.userid)+" Order: "+str(self.item)
